import streamlit as st
import streamlit.components.v1 as components
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="The Future Runs On Math",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CAREER DATA
# =========================================================

careers = [

    {
        "title": "DATA SCIENTIST",
        "salary": "R25K - R45K",
        "growth": "HIGH",
        "description": "Use AI, mathematics and coding to predict trends and solve problems.",
        "skills": ["Python", "Machine Learning", "AI", "Statistics"],
        "youtube": "zD73uHl4k8w"
    },

    {
        "title": "MACHINE LEARNING ENGINEER",
        "salary": "R35K - R60K",
        "growth": "VERY HIGH",
        "description": "Build intelligent AI systems that learn automatically.",
        "skills": ["Deep Learning", "AI", "Python", "TensorFlow"],
        "youtube": "bWOozHQtnY0"
    },

    {
        "title": "DATA ANALYST",
        "salary": "R20K - R40K",
        "growth": "HIGH",
        "description": "Transform data into insights and business decisions.",
        "skills": ["Power BI", "SQL", "Excel", "Analytics"],
        "youtube": "XtwXnDNbEKM"
    },

    {
        "title": "ACTUARY",
        "salary": "R35K - R70K",
        "growth": "VERY HIGH",
        "description": "Use advanced mathematics to predict and manage financial risk.",
        "skills": ["Risk", "Finance", "Probability", "Statistics"],
        "youtube": "THQWhMkij2E"
    }

]

# =========================================================
# SLIDESHOW LOGIC
# =========================================================

if "career_index" not in st.session_state:
    st.session_state.career_index = 0

career = careers[st.session_state.career_index]

# =========================================================
# SKILLS HTML
# =========================================================

skills_html = ""

for skill in career["skills"]:
    skills_html += f"""
    <div class="skill">{skill}</div>
    """

# =========================================================
# FULL HTML UI
# =========================================================

html_code = f"""

<!DOCTYPE html>
<html>

<head>

<style>

* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

body {{
    background:#020617;
    color:white;
    font-family:Arial, sans-serif;
    overflow-x:hidden;
}}

/* =====================================================
BACKGROUND ANIMATION
===================================================== */

.background {{
    position:fixed;
    width:100%;
    height:100%;
    top:0;
    left:0;
    z-index:-1;

    background:
        radial-gradient(circle at top left, #0f172a, #020617 60%);
}}

.background::before {{
    content:'';
    position:absolute;
    width:100%;
    height:100%;

    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);

    background-size:50px 50px;

    animation:moveGrid 15s linear infinite;
}}

@keyframes moveGrid {{

    0% {{
        transform:translateY(0px);
    }}

    100% {{
        transform:translateY(50px);
    }}
}}

.main-container {{
    padding:20px;
}}

/* =====================================================
TITLE
===================================================== */

.title {{
    text-align:center;
    font-size:85px;
    font-weight:900;
    line-height:0.95;

    background:linear-gradient(
        90deg,
        #22d3ee,
        #38bdf8,
        #8b5cf6,
        #ec4899
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    margin-top:10px;

    text-shadow:0px 0px 25px rgba(34,211,238,0.4);
}}

.subtitle {{
    text-align:center;
    color:#cbd5e1;
    font-size:24px;
    margin-top:15px;
    margin-bottom:30px;
}}

/* =====================================================
TIMER
===================================================== */

.timer {{
    position:absolute;
    top:20px;
    right:30px;

    background:#111827;

    border:1px solid #8b5cf6;

    border-radius:20px;

    padding:20px 30px;

    box-shadow:0px 0px 25px rgba(139,92,246,0.25);
}}

.timer-title {{
    color:#cbd5e1;
    font-size:16px;
}}

.timer-value {{
    font-size:42px;
    font-weight:bold;
    color:#22d3ee;
}}

/* =====================================================
MAIN GRID
===================================================== */

.grid {{
    display:grid;
    grid-template-columns:1fr 1.3fr;
    gap:25px;
}}

/* =====================================================
CARDS
===================================================== */

.card {{
    background:rgba(15,23,42,0.75);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:28px;

    padding:30px;

    backdrop-filter:blur(10px);

    box-shadow:
        0px 0px 30px rgba(34,211,238,0.1);
}}

/* =====================================================
CAREER TITLE
===================================================== */

.career-title {{
    font-size:58px;
    font-weight:900;
    color:#22d3ee;
}}

.description {{
    margin-top:20px;

    font-size:25px;

    line-height:1.6;

    color:#e2e8f0;
}}

/* =====================================================
STATS
===================================================== */

.stats {{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:15px;

    margin-top:30px;
}}

.stat {{
    background:#111827;

    border-radius:20px;

    padding:20px;

    text-align:center;

    border:1px solid rgba(255,255,255,0.08);
}}

.stat-title {{
    color:#94a3b8;
    font-size:15px;
}}

.stat-value {{
    margin-top:10px;

    font-size:28px;
    font-weight:bold;

    color:#22d3ee;
}}

/* =====================================================
SKILLS
===================================================== */

.skills-title {{
    margin-top:30px;

    font-size:24px;
    font-weight:bold;

    color:#22d3ee;
}}

.skills {{
    display:flex;
    flex-wrap:wrap;
    gap:12px;

    margin-top:15px;
}}

.skill {{
    background:#111827;

    border:1px solid rgba(255,255,255,0.08);

    border-radius:14px;

    padding:12px 18px;

    font-size:18px;
}}

/* =====================================================
VIDEO
===================================================== */

.video-container {{
    overflow:hidden;
}}

.video-container iframe {{

    width:100%;
    height:650px;

    border:none;

    border-radius:22px;

    box-shadow:
        0px 0px 35px rgba(34,211,238,0.2);
}}

/* =====================================================
BOTTOM CAREERS
===================================================== */

.bottom-title {{
    text-align:center;

    margin-top:35px;
    margin-bottom:20px;

    font-size:34px;
    font-weight:bold;
}}

.career-cards {{

    display:grid;

    grid-template-columns:repeat(4,1fr);

    gap:15px;
}}

.small-card {{

    background:#0f172a;

    border-radius:20px;

    padding:22px;

    border:1px solid rgba(255,255,255,0.08);

    transition:0.3s;
}}

.small-card:hover {{

    transform:translateY(-5px);

    border:1px solid #22d3ee;

    box-shadow:
        0px 0px 20px rgba(34,211,238,0.25);
}}

.small-title {{
    color:#22d3ee;

    font-size:22px;
    font-weight:bold;
}}

.small-salary {{
    margin-top:12px;

    color:#cbd5e1;

    font-size:18px;
}}

/* =====================================================
FOOTER
===================================================== */

.footer {{

    margin-top:30px;

    background:#0f172a;

    border-radius:20px;

    padding:22px;

    text-align:center;

    font-size:30px;
    font-weight:bold;

    color:#22d3ee;

    border:1px solid rgba(255,255,255,0.08);
}}

</style>

</head>

<body>

<div class="background"></div>

<div class="main-container">

<div class="timer">

<div class="timer-title">
NEXT CAREER IN
</div>

<div class="timer-value">
10
</div>

</div>

<div class="title">
THE FUTURE<br>
RUNS ON MATH
</div>

<div class="subtitle">
Department of Mathematics & Physics |
Qualification: Mathematical Science
</div>

<div class="grid">

<!-- LEFT -->

<div class="card">

<div class="career-title">
{career["title"]}
</div>

<div class="description">
{career["description"]}
</div>

<div class="stats">

<div class="stat">
<div class="stat-title">STARTING SALARY</div>
<div class="stat-value">{career["salary"]}</div>
</div>

<div class="stat">
<div class="stat-title">JOB GROWTH</div>
<div class="stat-value">{career["growth"]}</div>
</div>

<div class="stat">
<div class="stat-title">FUTURE DEMAND</div>
<div class="stat-value">HIGH</div>
</div>

</div>

<div class="skills-title">
SKILLS YOU WILL USE
</div>

<div class="skills">
{skills_html}
</div>

</div>

<!-- RIGHT -->

<div class="card video-container">

<iframe

src="https://www.youtube.com/embed/{career["youtube"]}?autoplay=1&mute=1&controls=0&loop=1&playlist={career["youtube"]}&modestbranding=1&showinfo=0&rel=0"

allow="autoplay"

allowfullscreen>

</iframe>

</div>

</div>

<!-- BOTTOM -->

<div class="bottom-title">
EXPLORE CAREERS IN MATHEMATICAL SCIENCE
</div>

<div class="career-cards">

<div class="small-card">
<div class="small-title">DATA SCIENTIST</div>
<div class="small-salary">R25K - R45K</div>
</div>

<div class="small-card">
<div class="small-title">ML ENGINEER</div>
<div class="small-salary">R35K - R60K</div>
</div>

<div class="small-card">
<div class="small-title">DATA ANALYST</div>
<div class="small-salary">R20K - R40K</div>
</div>

<div class="small-card">
<div class="small-title">ACTUARY</div>
<div class="small-salary">R35K - R70K</div>
</div>

</div>

<div class="footer">
YOUR MATH. YOUR FUTURE. YOUR IMPACT.
</div>

</div>

</body>
</html>

"""

components.html(
    html_code,
    height=1200,
    scrolling=False
)

# =========================================================
# AUTO ROTATE EVERY 10 SECONDS
# =========================================================

time.sleep(10)

st.session_state.career_index = (
    st.session_state.career_index + 1
) % len(careers)

st.rerun()