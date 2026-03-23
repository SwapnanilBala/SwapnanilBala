<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Swapnanil Bala</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Sora:wght@300;400;600;700&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #f9f8f6;
    --surface: #ffffff;
    --border: #e8e6e0;
    --border-strong: #d0cec8;
    --text-primary: #1a1916;
    --text-secondary: #5c5a55;
    --text-muted: #9b9990;
    --accent: #1a1916;
    --live-bg: #ecfdf5;
    --live-border: #a7f3d0;
    --live-text: #065f46;
    --tag-bg: #f1efe9;
    --tag-text: #6b6964;
    --info-bg: #eff6ff;
    --info-border: #bfdbfe;
    --info-text: #1d4ed8;
    --featured-border: #c7d2fe;
  }

  body {
    font-family: 'Sora', sans-serif;
    background: var(--bg);
    color: var(--text-primary);
    min-height: 100vh;
    padding: 3rem 1.5rem;
  }

  .container {
    max-width: 900px;
    margin: 0 auto;
  }

  /* TOP HEADER */
  .header {
    display: flex;
    align-items: flex-start;
    gap: 1.75rem;
    padding-bottom: 2rem;
    margin-bottom: 2.5rem;
    border-bottom: 1px solid var(--border);
  }

  .avatar {
    width: 72px; height: 72px;
    border-radius: 50%;
    background: var(--info-bg);
    border: 1.5px solid var(--info-border);
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; font-weight: 700;
    color: var(--info-text);
    flex-shrink: 0;
    letter-spacing: -0.5px;
  }

  .header-text h1 {
    font-size: 26px; font-weight: 700;
    color: var(--text-primary);
    line-height: 1.2;
    margin-bottom: 5px;
  }

  .tagline {
    font-size: 13px;
    color: var(--text-secondary);
    font-weight: 300;
    margin-bottom: 4px;
  }

  .univ {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-muted);
    margin-bottom: 12px;
  }

  .link-row {
    display: flex; gap: 8px; flex-wrap: wrap;
  }

  .link-pill {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    padding: 4px 12px;
    border-radius: 100px;
    border: 1px solid var(--info-border);
    background: var(--info-bg);
    color: var(--info-text);
    text-decoration: none;
  }

  .link-pill:hover { opacity: 0.75; }

  /* SECTION */
  .section { margin-bottom: 2.5rem; }

  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 1rem;
  }

  .about-text {
    font-size: 14px;
    line-height: 1.85;
    color: var(--text-secondary);
    font-weight: 300;
  }

  .about-text strong {
    font-weight: 600;
    color: var(--text-primary);
  }

  hr.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin-bottom: 2.5rem;
  }

  /* CARDS */
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 12px;
  }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.1rem 1.25rem;
    position: relative;
  }

  .card.featured {
    border-color: var(--featured-border);
  }

  .card:hover {
    border-color: var(--border-strong);
  }

  .live-badge {
    position: absolute;
    top: 14px; right: 14px;
    display: flex; align-items: center; gap: 5px;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: var(--live-text);
    background: var(--live-bg);
    border: 1px solid var(--live-border);
    padding: 2px 8px;
    border-radius: 100px;
  }

  .live-dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: var(--live-text);
  }

  .card-icon { font-size: 18px; margin-bottom: 8px; }

  .card-title {
    font-size: 14px; font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 5px;
    padding-right: 60px;
  }

  .card-desc {
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.65;
    font-weight: 300;
    margin-bottom: 12px;
  }

  .tag-row { display: flex; flex-wrap: wrap; gap: 5px; }

  .tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 5px;
    background: var(--tag-bg);
    color: var(--tag-text);
    border: 1px solid var(--border);
  }

  /* SKILLS TABLE */
  .skills-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }

  .skills-table tr {
    border-bottom: 1px solid var(--border);
  }

  .skills-table tr:last-child { border-bottom: none; }

  .skills-table td {
    padding: 11px 0;
    vertical-align: top;
  }

  .skills-table td:first-child {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    width: 130px;
    padding-right: 20px;
    padding-top: 13px;
  }

  .skills-table td:last-child {
    color: var(--text-secondary);
    font-weight: 300;
    line-height: 1.75;
  }

  .skills-table td:last-child em {
    font-style: normal;
    font-weight: 600;
    color: var(--text-primary);
  }

  /* FOOTER */
  .footer {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-muted);
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    margin-top: 1rem;
  }
</style>
</head>
<body>
<div class="container">

  <!-- HEADER -->
  <div class="header">
    <div class="avatar">SB</div>
    <div class="header-text">
      <h1>Swapnanil Bala</h1>
      <div class="tagline">Builder · Data Scientist · Full-Stack &amp; Mobile Developer</div>
      <div class="univ">M.S. Data Science — Khoury College of Computer Sciences, Northeastern University</div>
      <div class="link-row">
        <a class="link-pill" href="https://www.linkedin.com/in/swapnanil-bala-854b722a7/" target="_blank">↗ LinkedIn</a>
        <a class="link-pill" href="https://github.com/SwapnanilBala" target="_blank">↗ GitHub</a>
        <a class="link-pill" href="https://www.instagram.com/frost.plays.lifts/" target="_blank">↗ Instagram</a>
      </div>
    </div>
  </div>

  <!-- ABOUT -->
  <div class="section">
    <div class="section-label">About</div>
    <p class="about-text">
      I'm a data science grad student who actually ships things. My work lives at the intersection of
      <strong>data engineering, applied ML, and product development</strong> — from training classifiers on real datasets
      to deploying full-stack web and mobile apps that real users have tried and given feedback on.<br/><br/>
      I build fast, leaning into <strong>AI-assisted development</strong> to accelerate the full stack: backends, databases,
      frontends, and native mobile. I ship to iOS and Android without compromising on code quality. I'm equally
      at home in a Jupyter notebook and a React Native codebase.<br/><br/>
      Outside of code: <strong>motorcycle rides</strong>, <strong>gym sessions</strong>, <strong>piano</strong> (ABRSM Grade 3 &amp; 4), and thinking too hard about astrophysics.
    </p>
  </div>

  <hr class="divider"/>

  <!-- LIVE PROJECTS -->
  <div class="section">
    <div class="section-label">Live &amp; Deployed</div>
    <div class="grid">

      <div class="card featured">
        <div class="live-badge"><span class="live-dot"></span>live</div>
        <div class="card-icon">🌌</div>
        <div class="card-title">Astro App</div>
        <div class="card-desc">Cross-platform iOS &amp; Android astrology app. Ephemeris-based chart generation, palm reading via Claude Vision API (webcam + file upload), and RAG-powered interpretations backed by Supabase pgvector.</div>
        <div class="tag-row">
          <span class="tag">React Native</span>
          <span class="tag">Expo</span>
          <span class="tag">TypeScript</span>
          <span class="tag">FastAPI</span>
          <span class="tag">Supabase</span>
          <span class="tag">Claude Vision</span>
        </div>
      </div>

      <div class="card featured">
        <div class="live-badge"><span class="live-dot"></span>live</div>
        <div class="card-icon">🤖</div>
        <div class="card-title">AI Training Platform</div>
        <div class="card-desc">Full-stack web + mobile app for AI-assisted training workflows. Python/FastAPI backend, Supabase auth, Next.js frontend deployed on Vercel. In active use.</div>
        <div class="tag-row">
          <span class="tag">Next.js</span>
          <span class="tag">TypeScript</span>
          <span class="tag">FastAPI</span>
          <span class="tag">Supabase</span>
          <span class="tag">Vercel</span>
        </div>
      </div>

      <div class="card featured">
        <div class="live-badge"><span class="live-dot"></span>live</div>
        <div class="card-icon">🏥</div>
        <div class="card-title">Medical Booking Platform</div>
        <div class="card-desc">Production-grade patient-facing booking system. Appointment scheduling, real-time availability, and a clean responsive UI. Backed by Neon serverless Postgres and Supabase auth.</div>
        <div class="tag-row">
          <span class="tag">Next.js</span>
          <span class="tag">TypeScript</span>
          <span class="tag">Neon</span>
          <span class="tag">Supabase</span>
          <span class="tag">Tailwind</span>
        </div>
      </div>

    </div>
  </div>

  <hr class="divider"/>

  <!-- PORTFOLIO -->
  <div class="section">
    <div class="section-label">Academic &amp; Portfolio</div>
    <div class="grid">

      <div class="card">
        <div class="card-icon">🎮</div>
        <div class="card-title">GridWorld Search Visualizer</div>
        <div class="card-desc">Live visual replay of BFS, DFS, UCS, A*, Bidirectional Search on custom maps. Per-run metrics: expanded nodes, frontier size, path length. Built for CS 5100 at Northeastern.</div>
        <div class="tag-row"><span class="tag">Python</span><span class="tag">Pygame</span></div>
      </div>

      <div class="card">
        <div class="card-icon">📊</div>
        <div class="card-title">BRFSS Health Dashboard</div>
        <div class="card-desc">CDC-style interactive dashboard on chronic health indicators. Demographic breakouts, prevalence trends, filterable and presentation-ready.</div>
        <div class="tag-row"><span class="tag">R</span><span class="tag">Shiny</span></div>
      </div>

      <div class="card">
        <div class="card-icon">🧠</div>
        <div class="card-title">TikTok Copyright Analyzer</div>
        <div class="card-desc">End-to-end NLP pipeline for copyright risk classification. Logistic Regression, Random Forest, SVM, Gradient Boosting — full ML pipeline, not just a notebook.</div>
        <div class="tag-row"><span class="tag">Python</span><span class="tag">NLP</span><span class="tag">scikit-learn</span></div>
      </div>

      <div class="card">
        <div class="card-icon">🚕</div>
        <div class="card-title">NYC TLC Tip Predictor</div>
        <div class="card-desc">Classifier on NYC taxi data for generous-tip likelihood. Feature engineering, cross-validation, XGBoost + Random Forest + Logistic Regression.</div>
        <div class="tag-row"><span class="tag">Python</span><span class="tag">XGBoost</span><span class="tag">scikit-learn</span></div>
      </div>

      <div class="card">
        <div class="card-icon">🍋</div>
        <div class="card-title">Little Lemon DB</div>
        <div class="card-desc">Full relational schema for a restaurant system. Normalization, complex queries, stored procedures, and referential integrity.</div>
        <div class="tag-row"><span class="tag">SQL</span><span class="tag">Relational DB</span></div>
      </div>

      <div class="card">
        <div class="card-icon">🧹</div>
        <div class="card-title">Room Cleanliness Detector</div>
        <div class="card-desc">ML classifier predicting room cleanliness from image input. Full CV pipeline: preprocessing, feature extraction, model training and evaluation.</div>
        <div class="tag-row"><span class="tag">Python</span><span class="tag">Computer Vision</span></div>
      </div>

    </div>
  </div>

  <hr class="divider"/>

  <!-- STACK -->
  <div class="section">
    <div class="section-label">Stack</div>
    <table class="skills-table">
      <tr>
        <td>Languages</td>
        <td>Python, <em>TypeScript</em>, JavaScript, SQL, R, Dart</td>
      </tr>
      <tr>
        <td>Frontend</td>
        <td><em>Next.js</em>, React Native (Expo), Tailwind CSS, HTML/CSS</td>
      </tr>
      <tr>
        <td>Backend</td>
        <td><em>FastAPI</em>, Node.js, REST APIs</td>
      </tr>
      <tr>
        <td>Databases</td>
        <td><em>Supabase</em> (Postgres + Auth), <em>Neon</em> (serverless Postgres), PostgreSQL</td>
      </tr>
      <tr>
        <td>ML &amp; Data</td>
        <td>scikit-learn, PyTorch, XGBoost, Gradient Boosting, SVM, NLP, CV, Pandas, NumPy</td>
      </tr>
      <tr>
        <td>Mobile</td>
        <td><em>React Native</em>, Expo, iOS &amp; Android</td>
      </tr>
      <tr>
        <td>Deployment</td>
        <td>Vercel, GitHub Actions</td>
      </tr>
      <tr>
        <td>AI Dev</td>
        <td><em>Claude Code</em>, Claude Vision API, AI-assisted full-stack &amp; mobile development</td>
      </tr>
      <tr>
        <td>Tools</td>
        <td>Git/GitHub, VS Code, Jupyter</td>
      </tr>
    </table>
  </div>

  <div class="footer">
    I build things that work, ship things that matter, and keep learning. — github.com/SwapnanilBala
  </div>

</div>
</body>
</html>
