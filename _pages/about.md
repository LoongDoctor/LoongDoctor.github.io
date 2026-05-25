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

<span class="anchor" id="about-me"></span>

<section class="academic-hero">
  <div class="academic-hero__content">
    <h1>Longbo Han</h1>
    <p class="academic-hero__title">Postdoctoral Researcher, Fudan University</p>
    <p class="academic-hero__subtitle">AI Security Testing Lead, Zhejiang Dong'an Testing Technology Co., Ltd.</p>
    <p class="academic-hero__lead">
      I work on security and privacy for AI systems, with a focus on generative AI security, lattice-based cryptography, zero-knowledge proofs, and privacy-preserving machine learning.
    </p>
    <div class="research-tags" aria-label="Research areas">
      <span>Generative AI Security</span>
      <span>Privacy Protection</span>
      <span>Lattice-based Cryptography</span>
      <span>Zero-Knowledge Proofs</span>
    </div>
    <div class="academic-actions">
      <a href="mailto:longbohan@fudan.edu.cn">Email</a>
      <a href="https://scholar.google.com/citations?user=sfSE38wAAAAJ">Google Scholar</a>
      <a href="https://github.com/LoongDoctor">GitHub</a>
    </div>
  </div>
  <aside class="academic-hero__panel" aria-label="Research snapshot">
    <div>
      <span class="snapshot-label">Current role</span>
      <strong>Postdoctoral Researcher</strong>
      <p>College of Computer Science and Artificial Intelligence, Fudan University</p>
    </div>
    <div>
      <span class="snapshot-label">Industry role</span>
      <strong>AI Security Testing Lead</strong>
      <p>Zhejiang Dong'an Testing Technology Co., Ltd.</p>
    </div>
    <div>
      <span class="snapshot-label">Focus</span>
      <strong>Secure AI systems</strong>
      <p>Security evaluation, privacy protection, and cryptographic methods for trustworthy AI.</p>
    </div>
  </aside>
</section>

<section class="academic-section">
  <h2>Biography</h2>
  <p>
    Dr. Longbo Han is a postdoctoral researcher at <strong>Fudan University</strong> and the AI Security Testing Lead at <strong>Zhejiang Dong'an Testing Technology Co., Ltd.</strong>. His research focuses on cybersecurity in AI applications, especially generative AI security, privacy protection, and cryptographic techniques.
  </p>
  <p>
    He received a Ph.D. in Cryptography from <strong>Hangzhou Dianzi University</strong>. His broader research interests include federated learning, blockchain technologies, data security, homomorphic encryption, and differential privacy.
  </p>
  <p>
    If you are interested in academic collaboration, please contact me at <a href="mailto:longbohan@fudan.edu.cn">longbohan@fudan.edu.cn</a> or <a href="mailto:longbohan@hdu.edu.cn">longbohan@hdu.edu.cn</a>.
  </p>
</section>

<span class="anchor" id="news"></span>

<section class="academic-section">
  <h2>News</h2>
  <div class="news-list">
    {% assign featured_news = site.data.news | slice: 0, 3 %}
    {% for item in featured_news %}
      <div class="news-item">
        <time>{{ item.date }}</time>
        <p>{{ item.text }}</p>
      </div>
    {% endfor %}
  </div>
  {% assign older_news = site.data.news | slice: 3, 20 %}
  {% if older_news.size > 0 %}
    <details class="news-more">
      <summary>More updates</summary>
      <div class="news-list">
        {% for item in older_news %}
          <div class="news-item">
            <time>{{ item.date }}</time>
            <p>{{ item.text }}</p>
          </div>
        {% endfor %}
      </div>
    </details>
  {% endif %}
</section>

<span class="anchor" id="publications"></span>

<section class="academic-section">
  <div class="section-heading-row">
    <h2>Selected Publications</h2>
    <a class="scholar-badge" href="https://scholar.google.com/citations?user=sfSE38wAAAAJ"><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FLoongDoctor%2FLoongDoctor.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar citations"></a>
  </div>
  <div class="publication-list">
    <article class="publication-card">
      <div class="publication-year">2026</div>
      <h3><a href="https://ieeexplore.ieee.org/document/11408819">ZebraCPA: Decentralized, Post-Quantum Conditional Privacy-Preserving Authentication for VANETs via Traceable ZK Ring Signatures</a></h3>
      <p class="publication-authors"><strong>Longbo Han</strong>, Xiaoting Li, Lin You, Gengran Hu, Feifei Xia, Jindong Huang, Yuyang Kuang, and Min Guo.</p>
      <p class="publication-details">IEEE Internet of Things Journal, early access, 2026.</p>
      <div class="publication-rankings" aria-label="Journal rankings">
        <span>中科院 1区</span>
        <span>JCR Q1</span>
      </div>
    </article>
    <article class="publication-card">
      <div class="publication-year">2025</div>
      <h3><a href="https://ieeexplore.ieee.org/document/11141403">SurroFL: Sketch-Based Defense Against Poisoning in Privacy-Preserving Federated Learning</a></h3>
      <p class="publication-authors">Yuyang Kuang, Weinan Liu, <strong>Longbo Han</strong>, Jindong Huang, Peng Cao, and Lin You.</p>
      <p class="publication-details">IEEE Internet of Things Journal, 12(23): 49417-49430, 2025.</p>
      <div class="publication-rankings" aria-label="Journal rankings">
        <span>中科院 1区</span>
        <span>JCR Q1</span>
      </div>
    </article>
    <article class="publication-card">
      <div class="publication-year">2025</div>
      <h3><a href="https://ieeexplore.ieee.org/abstract/document/10922084">A Novel Lattice-based Blockchain Infrastructure and its Application on Trusted Data Management</a></h3>
      <p class="publication-authors"><strong>Longbo Han</strong>, Gengran Hu, Xiaoting Li, Feifei Xia, Shengbao Wang, and Lin You.</p>
      <p class="publication-details">IEEE Transactions on Network Science and Engineering, 12(4): 2524-2536, 2025.</p>
      <div class="publication-rankings" aria-label="Journal rankings">
        <span>中科院 2区</span>
        <span>JCR Q1</span>
      </div>
    </article>
    <article class="publication-card">
      <div class="publication-year">2020</div>
      <h3><a href="https://ieeexplore.ieee.org/abstract/document/9258891">Privacy protection of VANET based on traceable ring signature on ideal lattice</a></h3>
      <p class="publication-authors"><strong>Longbo Han</strong>, Suzhen Cao, Xiaodong Yang, and Zhiqiang Zhang.</p>
      <p class="publication-details">IEEE Access, 8: 206581-206591, 2020.</p>
      <div class="publication-rankings" aria-label="Journal rankings">
        <span>中科院 2区</span>
        <span>JCR Q1/Q2</span>
      </div>
    </article>
    <article class="publication-card">
      <div class="publication-year">2021</div>
      <h3><a href="https://doi.org/10.1007/s12083-021-01195-2">An efficient outsourcing attribute-based encryption scheme in 5G mobile network environments</a></h3>
      <p class="publication-authors">Zhiqiang Zhang, Suzhen Cao, Xiaodong Yang, Xueyan Liu, and <strong>Longbo Han</strong>.</p>
      <p class="publication-details">Peer-to-Peer Networking and Applications, 14(6): 3488-3501, 2021.</p>
      <div class="publication-rankings" aria-label="Journal rankings">
        <span>中科院 3区</span>
        <span>JCR Q2</span>
      </div>
    </article>
  </div>
</section>

<span class="anchor" id="honors-and-awards"></span>

<section class="academic-section">
  <h2>Honors and Awards</h2>
  <div class="honor-list">
    <div class="honor-item">
      <time>2023.10</time>
      <p><strong>National Scholarship</strong> <span>Top 3%; 杭州电子科技大学博士研究生国家奖学金.</span></p>
    </div>
    <div class="honor-item">
      <time>2023.10</time>
      <p><strong>The First Prize Scholarship</strong> <span>Top 30%; 杭州电子科技大学学业一等奖学金.</span></p>
    </div>
    <div class="honor-item">
      <time>2022.10</time>
      <p><strong>The First Prize Scholarship</strong> <span>Top 30%; 杭州电子科技大学学业一等奖学金.</span></p>
    </div>
    <div class="honor-item">
      <time>2020.10</time>
      <p><strong>Excellent Student Cadre</strong> <span>Only one in a college; 西北师范大学优秀学生干部奖.</span></p>
    </div>
    <div class="honor-item">
      <time>2020.10</time>
      <p><strong>The Second Prize Scholarship</strong> <span>Top 30%; 西北师范大学学业二等奖学金.</span></p>
    </div>
    <div class="honor-item">
      <time>2019.10</time>
      <p><strong>Prize for the Practice Vanguard</strong> <span>Only one in a college; 西北师范大学实践先锋奖.</span></p>
    </div>
    <div class="honor-item">
      <time>2019.10</time>
      <p><strong>The Second Prize Scholarship</strong> <span>Top 30%; 西北师范大学学业二等奖学金.</span></p>
    </div>
    <div class="honor-item">
      <time>2016.11</time>
      <p><strong>National Third Prize</strong> <span>新道杯沙盘模拟运营大赛国赛三等奖.</span></p>
    </div>
    <div class="honor-item">
      <time>2016.07</time>
      <p><strong>Chongqing First Prize</strong> <span>新道杯沙盘模拟运营大赛重庆市一等奖.</span></p>
    </div>
    <div class="honor-item">
      <time>2015.07</time>
      <p><strong>Chongqing First Prize</strong> <span>挑战杯全国大学生课外学术科技作品竞赛.</span></p>
    </div>
  </div>
</section>

<span class="anchor" id="projects"></span>

<section class="academic-section">
  <h2>Projects</h2>
  <div class="project-list">
    <article>
      <div class="project-type">National research projects</div>
      <h3>National Natural Science Foundation of China Projects</h3>
      <p>Topics include multimodal biometric cryptography, attribute-based data access control, privacy-preserving multiparty cryptographic algorithms, big-data integrity verification, and lattice-computing complexity.</p>
      <div class="project-tags">
        <span>61772166</span>
        <span>61662071</span>
        <span>61562077</span>
        <span>61662069</span>
        <span>61602143</span>
      </div>
    </article>
    <article>
      <div class="project-type">Provincial research project</div>
      <h3>Natural Science Foundation of Zhejiang Province</h3>
      <p>Key information security technologies based on the Internet and multimodal biometric identification.</p>
      <div class="project-tags">
        <span>LZ17F020002</span>
      </div>
    </article>
    <article>
      <div class="project-type">Open research fund</div>
      <h3>Key Laboratory of Cryptography of Zhejiang Province</h3>
      <p>Scalability technology and applications for blockchain cross-chain systems.</p>
      <div class="project-tags">
        <span>ZCL21005</span>
      </div>
    </article>
  </div>
</section>

<span class="anchor" id="experience"></span>

<section class="academic-section">
  <h2>Experience</h2>
  <div class="experience-list">
    <article>
      <time>2025-Present</time>
      <div>
        <h3>AI Security Testing Lead</h3>
        <p>Zhejiang Dong'an Testing Technology Co., Ltd.</p>
      </div>
    </article>
    <article>
      <time>2020.10-2021.03</time>
      <div>
        <h3>Security Technology Internship</h3>
        <p><a href="http://www.xbcisp.com/">Gansu Anju Technology Security Co.</a>, China.</p>
      </div>
    </article>
  </div>
</section>
