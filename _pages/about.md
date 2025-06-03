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

I am Menghui Zhou, a second-year PhD student in the Pervasive Computing Group at the University of Sheffield, UK,
working under the supervision of [Prof. Po Yang](https://scholar.google.com/citations?hl=en&user=RdK3cwgAAAAJ).
I hold a bachelor’s degree from the School of Computer Science and Engineering
at [Sun Yat-sen University](https://cse.sysu.edu.cn/),
and a master’s degree from the School of Software at [Yunnan University](http://www.sei.ynu.edu.cn/),
where I worked closely with [Prof. Yun Yang](https://scholar.google.com/citations?user=pUBf8LwAAAAJ)
and [Prof. Po Yang](https://scholar.google.com/citations?hl=en&user=RdK3cwgAAAAJ).

My research primarily focuses on interpretable machine learning and its applications in healthcare and smart
agriculture.

Please drop me an email if you are interested in collaborating with me.

# 🔥 News

- *2025.05*: &nbsp;🎉🎉 One paper was accepted by the journal Engineering Applications of Artificial Intelligence.
- *2024.12*: &nbsp;🎉🎉 Four papers were accepted by the International Conference on
   Bioinformatics and Biomedicine (BIBM).

# 📝 Publications

**As the First Author:**

<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">TKDE 2024</div>
<img src='images/tkde2024-500x300.png' alt="sym" width="100%">
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
<img src='images/kdd2023-500x300.png' alt="sym" width="100%">
</div>
</div>
<div class='paper-box-text' markdown="1">

[Automatic Temporal Relation in Multi-Task Learning](https://dl.acm.org/doi/pdf/10.1145/3580305.3599261)

**Menghui Zhou**, Po Yang

- ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2023
- This paper introduces Auto-TR, an automated framework that jointly learns temporal relation graphs
  and predictive models for disease progression using longitudinal data,
  achieving state-of-the-art performance while enhancing model interpretability.

</div>
</div>


<div class='paper-box'>
<div class='paper-box-image'>
<div>
<div class="badge">AAAI 2023</div>
<img src='images/aaai2023-500x300.png' alt="sym" width="100%">
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


- `BIBM 2024` [Learning Interpretable Continuous Representation for Alzheimer’s Disease Classification](https://doi.org/10.1109/BIBM62325.2024.10821731);
**Menghui Zhou**, Mingxia Wang, Yu Zhang, Zhipeng Yuan, Vitaveska Lanfranchi, Po Yang;
Published in *2024 IEEE International Conference on Bioinformatics and Biomedicine*
- `NCA 2023` [Efficient multi-task learning with adaptive temporal structure for progression prediction](https://link.springer.com/article/10.1007/s00521-023-08461-9);
      **Menghui Zhou**, Yu Zhang, Tong Liu, Yun Yang, Po Yang;
    Published in *Neural Computing and Applications*
- `CIKM 2022` [Multi-task Learning with Adaptive Global Temporal Structure for Predicting Alzheimer's Disease Progression](https://doi.org/10.1145/3511808.3557406);
    **Menghui Zhou**, Yu Zhang, Tong Liu, Yun Yang, Po Yang;
    Published in *The 31st ACM International Conference on Information & Knowledge*
- `MSN 2021` [Modeling disease progression flexibly with nonlinear disease structure via multi-task learning](https://doi.org/10.1109/MSN53354.2021.00063);
   **Menghui Zhou**, Xulong Wang, Yun Yang, Fengtao Nan, Yu Zhang, Jun Qi, Po Yang;
   Published in *The 17th International Conference on Mobility, Sensing and Networking*

**As the Corresponding Author:**

- `EAAI 2025` [Joint image synthesis and fusion with converted features for Alzheimer’s disease diagnosis](https://doi.org/10.1016/j.engappai.2025.111102);  
  Zhaodong Chen, Mingxia Wang, Fengtao Nan, Yun Yang, Shunbao Li, Menghui Zhou*, Jun Qi, Hanwen Wang, Po Yang*;  
  Published in *Engineering Applications of Artificial Intelligence*

- `BIBM 2024` [Adaptive Multi-Cognitive Objective Temporal Task Approach for Predicting AD Progression](https://doi.org/10.1109/BIBM62325.2024.10822758);  
  Xuanhan Fan, Menghui Zhou*, Yu Zhang, Jun Qi, Yun Yang, Po Yang*;  
  Published in *2024 IEEE International Conference on Bioinformatics and Biomedicine*

- `KBS 2024` [Informative relationship multi-task learning: Exploring pairwise contribution across tasks’ sharing knowledge](https://doi.org/10.1016/j.knosys.2024.112187);  
  Xiangchao Chang, Menghui Zhou*, Xulong Wang, Yun Yang, Po Yang*;  
  Published in *Knowledge-Based Systems*

# 🎖 Honors and Awards

- *2024* BIBM Travel Grant
- *2023* EPSRC Scholarship, UK
- *2022* China National Scholarship.

<!-- 

# 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.


-->

<hr>
<div style="height: 25px;"></div>
<div align="center">
  <a href='https://clustrmaps.com/site/1bw4v'  title='Visit tracker'>
    <img src='//clustrmaps.com/map_v2.png?cl=ffffff&w=300&t=t&d=QjzhdT3Oe4EwddJpt7uzrPc4x5n47N6UfVJ4LdvZFKI&co=2d78ad&ct=ffffff'/>
  </a>
</div>



<div style="height: 50px;"></div>