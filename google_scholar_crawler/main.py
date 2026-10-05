"""Fetch the public Google Scholar citation total without extra dependencies."""

import json
import os
import re
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class CitationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_stat_cell = False
        self.values = []

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_stat_cell = 'gsc_rsb_std' in dict(attrs).get('class', '').split()

    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_stat_cell = False

    def handle_data(self, data):
        if self.in_stat_cell and data.strip():
            self.values.append(data.strip())


def parse_total(html):
    parser = CitationParser()
    parser.feed(html)
    if len(parser.values) < 6:
        raise ValueError('Google Scholar did not return the citation statistics table.')
    total = parser.values[0].replace(',', '').replace('\xa0', '')
    if not total.isdecimal():
        raise ValueError('Google Scholar returned an invalid citation total.')
    return int(total)


def main():
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 't8Y_gnsAAAAJ')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', scholar_id):
        raise ValueError('Invalid Google Scholar profile ID.')
    url = 'https://scholar.google.com/citations?' + urlencode({'user': scholar_id, 'hl': 'en'})
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or 'utf-8'
        total = parse_total(response.read().decode(charset, errors='replace'))
    # A failed request or invalid response leaves the last successful data intact.
    result = {
        'scholar_id': scholar_id,
        'citedby': total,
        'updated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'source': url,
    }
    output = Path('_data/google-scholar.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    temporary.replace(output)
    print(f'Google Scholar total citations: {total}')


if __name__ == '__main__':
    main()
