---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a Ph.D. researcher in Computer Science at the [University of Sheffield](https://www.sheffield.ac.uk/), UK, **with my thesis submitted and viva pending**, supervised by Professor Po Yang and Professor Vitaveska Lanfranchi.

My research focuses on **general-purpose, trustworthy white-box deep learning grounded in information theory**. I also have extensive experience and a strong interest in developing **machine learning algorithms for healthcare**, particularly disease progression modelling and biomarker identification.

I received my M.Sc. in Computer Science from [Yunnan University](http://www.sei.ynu.edu.cn/) (2020–2023), where I studied Alzheimer's disease progression using multi-task learning, and my B.S. in Software Engineering from [Sun Yat-sen University](https://cse.sysu.edu.cn/) (2013–2017).

I welcome research collaborations and opportunities in trustworthy AI and machine learning for healthcare. Please [get in touch](mailto:menghui.zhou@sheffield.ac.uk).

<span class='anchor' id='research'></span>

# 🔬 Research

### Trustworthy White-Box Machine Learning

I develop learning systems whose objectives, representations, architecture and inference process are explicit and interpretable. My research addresses four complementary levels:

- **Learning objectives:** Clarifying what a model learns to achieve and why its objectives are meaningful.
- **Representation structure:** Making the organisation of learned representations explicit and understandable.
- **Model architecture:** Explaining the roles of model components and their interactions.
- **Inference process:** Making the reasoning behind model outputs traceable.

This work brings together information theory, coding theory, representation learning, robustness to label noise and out-of-distribution generalisation.

### Machine Learning for Healthcare

I develop multi-task and statistical learning methods for **single-disease and cross-disease progression modelling**, biomarker identification, wearable sensor analysis and medical imaging, including 3D MRI. My work spans Alzheimer's disease, Parkinson's disease and mobility-related conditions.

<span class='anchor' id='news'></span>

# 🔥 News

- **2026.10:** My Ph.D. thesis has been submitted; I am awaiting my viva.
- **2026.09:** My paper *Less Structure is More: Minimal Representations for Supervised Learning* was accepted by NeurIPS 2026.
- **2026.09:** Our preprint [On the Limits of Maximal Coding Rate Reduction for Out-of-Distribution Generalisation](https://arxiv.org/abs/2609.21001) is available on arXiv (17 September 2026).
- **2026.08:** Our preprint [DeMMO: Longitudinal and Cross-Disease Modelling of Digital Mobility Outcomes via Multi-Task Learning](https://arxiv.org/abs/2608.25073) is available on arXiv (25 August 2026).
- **2026.06:** Our paper *Beyond Single Scores: A Multi-Cognitive Objective Learning for AD Progression Prediction*, on which I am a co-corresponding author, was accepted by *Pattern Recognition*.
- **2025.05:** Co-corresponding-author paper on joint image synthesis and fusion accepted by *Engineering Applications of Artificial Intelligence*.
- **2024.12:** Four papers accepted by the IEEE International Conference on Bioinformatics and Biomedicine (BIBM).

<span class='anchor' id='publications'></span>

# 📝 Selected Publications

Google Scholar citations: **<span id="total_cit" title="Last checked: {{ site.data['google-scholar'].updated | slice: 0, 10 }}">{{ site.data['google-scholar'].citedby }}</span>** · [Google Scholar](https://scholar.google.com/citations?user=t8Y_gnsAAAAJ&hl=en)

- **NeurIPS 2026** — [Less Structure is More: Minimal Representations for Supervised Learning](https://openreview.net/forum?id=yt1Bywu2lu)<br>
  **Menghui Zhou**, Vitaveska Lanfranchi, Po Yang.<br>
  *Conference on Neural Information Processing Systems (NeurIPS), 2026.*

- **TKDE 2024** — [Integrating Visualised Automatic Temporal Relation Graph into Multi-Task Learning for Alzheimer's Disease Progression Prediction](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10495318)<br>
  **Menghui Zhou**, Xulong Wang, Tong Liu, Yun Yang, Po Yang.<br>
  *IEEE Transactions on Knowledge and Data Engineering (TKDE), 2024.*

- **KDD 2023** — [Automatic Temporal Relation in Multi-Task Learning](https://dl.acm.org/doi/pdf/10.1145/3580305.3599261)<br>
  **Menghui Zhou**, Po Yang.<br>
  *ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2023.*

- **AAAI 2023** — [Robust Temporal Smoothness in Multi-Task Learning](https://ojs.aaai.org/index.php/AAAI/article/view/26351)<br>
  **Menghui Zhou**, Yu Zhang, Yun Yang, Tong Liu, Po Yang.<br>
  *AAAI Conference on Artificial Intelligence (AAAI), 2023.*

- **BIBM 2024** — [Learning Interpretable Continuous Representation for Alzheimer's Disease Classification](https://doi.org/10.1109/BIBM62325.2024.10821731)<br>
  **Menghui Zhou**, Mingxia Wang, Yu Zhang, Zhipeng Yuan, Vitaveska Lanfranchi, Po Yang.<br>
  *IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2024.*

- **BIBM 2023** — Integrating Automatic Temporal Relation Graph into Multi-Task Learning for Alzheimer's Disease Progression Prediction<br>
  **Menghui Zhou**, T. Liu, X. Wang, K. Liu, Y. Zhang, P. Yang.<br>
  *IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2023.*

- **CIKM 2022** — [Multi-task Learning with Adaptive Global Temporal Structure for Predicting Alzheimer's Disease Progression](https://doi.org/10.1145/3511808.3557406)<br>
  **Menghui Zhou**, Yu Zhang, Tong Liu, Yun Yang, Po Yang.<br>
  *ACM International Conference on Information and Knowledge Management (CIKM), 2022.*

- **MSN 2021** — [Modeling Disease Progression Flexibly with Nonlinear Disease Structure via Multi-task Learning](https://doi.org/10.1109/MSN53354.2021.00063)<br>
  **Menghui Zhou**, Xulong Wang, Yun Yang, Fengtao Nan, Yu Zhang, Jun Qi, Po Yang.<br>
  *IEEE International Conference on Mobility, Sensing and Networking (MSN), 2021.*

See my [Google Scholar profile](https://scholar.google.com/citations?user=t8Y_gnsAAAAJ) for the full publication record.

<span class='anchor' id='service'></span>

# 🌈 Professional Activities

- **Conference reviewing / programme committee service:** ICML, NeurIPS, ICLR, AAAI and KDD.
- **Journal reviewing:** IEEE Transactions on Knowledge and Data Engineering (TKDE), IEEE Transactions on Neural Networks and Learning Systems (TNNLS), Pattern Recognition (PR), Knowledge-Based Systems (KBS) and Engineering Applications of Artificial Intelligence (EAAI).

<span class='anchor' id='awards'></span>

# 🎖 Honors and Awards

- **2024:** First Prize, Ph.D. Poster Competition, University of Sheffield.
- **2024:** IEEE BIBM Travel Grant.
- **2023:** EPSRC Ph.D. Scholarship.
- **2023:** Outstanding Master's Thesis Award, Yunnan University.
- **2022:** China National Scholarship.

<hr>
<div style="height: 25px;"></div>
<center>
<script type="text/javascript" src="https://widget.supercounters.com/ssl/map.js"></script>
<script type="text/javascript">var sc_map_var = sc_map_var || [];sc_map(1739176,"ffffff","b22222",80)</script><br>
<noscript><a href="https://www.supercounters.com/">Visitor map</a></noscript>
</center>



<div style="height: 50px;"></div>
