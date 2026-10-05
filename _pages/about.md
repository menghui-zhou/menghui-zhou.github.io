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

- **2026:** My Ph.D. thesis has been submitted; I am awaiting my viva.
- **2026:** First-author paper *Less Structure is More: Minimal Representations for Supervised Learning* at NeurIPS 2026.
- **2026:** Co-corresponding-author paper *Beyond Single Scores: A Multi-Cognitive Objective Learning for AD Progression Prediction* published in *Pattern Recognition*.
- **2025.05:** Co-corresponding-author paper on joint image synthesis and fusion accepted by *Engineering Applications of Artificial Intelligence*.
- **2024.12:** Four papers accepted by the IEEE International Conference on Bioinformatics and Biomedicine (BIBM).

<span class='anchor' id='publications'></span>

# 📝 Selected Publications

**Bold** identifies my name; \* marks co-corresponding authors.

### First-Author Papers

- **NeurIPS 2026** — [Less Structure is More: Minimal Representations for Supervised Learning](https://openreview.net/forum?id=yt1Bywu2lu)<br>
  **Menghui Zhou**, Vitaveska Lanfranchi, Po Yang.<br>
  *Conference on Neural Information Processing Systems (NeurIPS).*<br>
  Research on minimal representations for supervised learning, connecting to my work on trustworthy white-box learning.

<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">TKDE 2024</div>
<img src='images/tkde2024-500x300.png' alt="Overview of the published learning framework" width="100%">
</div>
</div>
<div class='paper-box-text' markdown="1">

[Integrating Visualised Automatic Temporal Relation
Graph into Multi-Task Learning for Alzheimer’s
Disease Progression Prediction](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10495318)

**Menghui Zhou**, Xulong Wang, Tong Liu, Yun Yang, Po Yang

- IEEE Transactions on Knowledge and Data Engineering (TKDE), 2024
- This paper proposes a novel multi-task learning framework, MAGPP, which integrates an automatically learned
  temporal relation graph and sparse group Lasso to improve Alzheimer’s
  disease progression prediction using MRI data.

</div>
</div>


<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">KDD 2023</div>
<img src='images/kdd2023-500x300.png' alt="Overview of the published learning framework" width="100%">
</div>
</div>
<div class='paper-box-text' markdown="1">

[Automatic Temporal Relation in Multi-Task Learning](https://dl.acm.org/doi/pdf/10.1145/3580305.3599261)

**Menghui Zhou**, Po Yang

- ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2023
- This paper proposes AutoTR, a novel automatic temporal relation mechanism for multi-task learning
  that directly learns complex and asymmetric temporal relations between tasks
  from data leading to improved prediction performance and high efficiency.
</div>
</div>


<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">AAAI 2023</div>
<img src='images/aaai2023-500x300.png' alt="Overview of the published learning framework" width="100%">
</div>
</div>
<div class='paper-box-text' markdown="1">

[Robust Temporal Smoothness in Multi-Task Learning](https://ojs.aaai.org/index.php/AAAI/article/view/26351)

**Menghui Zhou**, Yu Zhang, Yun Yang, Tong Liu, Po Yang

- AAAI Conference on Artificial Intelligence (AAAI), 2023
- The paper proposes two Robust Temporal Smoothness (RoTS) frameworks for multi-task learning that jointly capture
  temporal smoothness across tasks and detect outlier tasks, outperforming traditional
  smoothness-based methods without increasing computational complexity.

</div>
</div>

- **BIBM 2024** — [Learning Interpretable Continuous Representation for Alzheimer's Disease Classification](https://doi.org/10.1109/BIBM62325.2024.10821731)<br>
  **Menghui Zhou**, Mingxia Wang, Yu Zhang, Zhipeng Yuan, Vitaveska Lanfranchi, Po Yang.<br>
  *IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2024.*

- **BIBM 2023** — Integrating Automatic Temporal Relation Graph into Multi-Task Learning for Alzheimer's Disease Progression Prediction<br>
  **M. Zhou**, T. Liu, X. Wang, K. Liu, Y. Zhang, P. Yang.<br>
  *IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2023.*

- **CIKM 2022** — [Multi-task Learning with Adaptive Global Temporal Structure for Predicting Alzheimer's Disease Progression](https://doi.org/10.1145/3511808.3557406)<br>
  **Menghui Zhou**, Yu Zhang, Tong Liu, Yun Yang, Po Yang.<br>
  *ACM International Conference on Information and Knowledge Management (CIKM), 2022.*

- **MSN 2021** — [Modeling Disease Progression Flexibly with Nonlinear Disease Structure via Multi-task Learning](https://doi.org/10.1109/MSN53354.2021.00063)<br>
  **Menghui Zhou**, Xulong Wang, Yun Yang, Fengtao Nan, Yu Zhang, Jun Qi, Po Yang.<br>
  *IEEE International Conference on Mobility, Sensing and Networking (MSN), 2021.*

### Corresponding-Author Papers

- **PR 2026** — [Beyond Single Scores: A Multi-Cognitive Objective Learning for AD Progression Prediction](https://scholar.google.com/citations?user=t8Y_gnsAAAAJ&citation_for_view=t8Y_gnsAAAAJ:_Qo2XoVZTnwC&view_op=view_citation)<br>
  X. Fan, **M. Zhou**\*, Y. Zhang, J. Qi, Y. Yang, P. Yang\*.<br>
  *Pattern Recognition (PR), 2026.*

- **EAAI 2025** — [Joint Image Synthesis and Fusion with Converted Features for Alzheimer's Disease Diagnosis](https://doi.org/10.1016/j.engappai.2025.111102)<br>
  Zhaodong Chen, Mingxia Wang, Fengtao Nan, Yun Yang, Shunbao Li, **Menghui Zhou**\*, Jun Qi, Hanwen Wang, Po Yang\*.<br>
  *Engineering Applications of Artificial Intelligence (EAAI), 2025.*

- **KBS 2024** — [Informative Relationship Multi-task Learning: Exploring Pairwise Contribution Across Tasks' Sharing Knowledge](https://doi.org/10.1016/j.knosys.2024.112187)<br>
  Xiangchao Chang, **Menghui Zhou**\*, Xulong Wang, Yun Yang, Po Yang\*.<br>
  *Knowledge-Based Systems (KBS), 2024.*

- **BIBM 2024** — [Adaptive Multi-Cognitive Objective Temporal Task Approach for Predicting AD Progression](https://doi.org/10.1109/BIBM62325.2024.10822758)<br>
  Xuanhan Fan, **Menghui Zhou**\*, Yu Zhang, Jun Qi, Yun Yang, Po Yang\*.<br>
  *IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2024.*

- **IJCNN 2024** — A Multi-target Multi-task Approach Based on Correlated Multiple Cognitive Scores for AD Progression Prediction<br>
  Xuanhan Fan, **Menghui Zhou**\*, Jun Qi, Yun Yang, Po Yang\*.<br>
  *IEEE International Joint Conference on Neural Networks (IJCNN), 2024.*

See my [Google Scholar profile](https://scholar.google.com/citations?user=t8Y_gnsAAAAJ) for the full publication record.

<span class='anchor' id='projects'></span>

# 🧪 Research Projects and Experience

### Mobilise-D · University of Sheffield

Developed machine learning methods using free-living gait estimates across multiple disease conditions, including disease severity prediction and feature importance analysis to identify informative mobility measures.

### PDWearML · Yunnan University

Contributed to Parkinson's disease severity assessment using wrist-worn sensor data and the release of an open dataset. The [IEEE DataPort dataset](https://ieee-dataport.org/documents/pdwearml-leveraging-daily-activities-fast-parkinsons-disease-severity-assessment-wearable) recorded **11,885 downloads as of 4 October 2026**.

### AI-Enabled Climate-Smart Fertiliser Practice · University of Sheffield

Developed multi-task learning methods to balance winter wheat yield and greenhouse gas emissions, with validation through agricultural field trials.

### Teaching and Research Mentoring

Supported the teaching of machine learning theory and practical programming at the University of Sheffield. Mentored international master's students alongside Professor Po Yang on research ideas, manuscript writing, submission and revision.

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
<div align="center">
<a href='https://clustrmaps.com/site/1bw4v'  title='Visit tracker'>
<img src='//clustrmaps.com/map_v2.png?cl=ffffff&w=a&t=tt&d=QjzhdT3Oe4EwddJpt7uzrPc4x5n47N6UfVJ4LdvZFKI'/></a>
</div>



<div style="height: 50px;"></div>
