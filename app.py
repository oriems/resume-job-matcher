import streamlit as st
from datetime import date

# Step 1: Define your structured resume memory
resume_memory = [
    {
        "company": "Norwest Venture Partners",
        "title": "Senior Data Scientist",
        "start": "2021-08",
        "end": "2025-05",
        "tools": ["Python", "dbt (seeds/models/snapshots)", "Dagster", "Tableau", "Metabase", "Sigma", "pydantic", "scikit-learn", "Hugging Face"],
        "impact": [
            "Created 10,000+ sourced leads with 20%+ investor conversation rate",
            "Built scoring models with 30+ non-public features",
            "Developed scalable pipelines across 80+ tables",
            "Implemented LLMs to extract entities and improve search relevance"
        ]
    },
    {
        "company": "PitchBook Data",
        "title": "Director, Data Science & Software Engineering",
        "start": "2017-07",
        "end": "2021-07",
        "tools": ["Python", "AWS", "SQL", "Excel", "REST APIs", "Machine Learning", "JIRA", "Flask"],
        "impact": [
            "Increased data coverage by 60%, reduced headcount by ⅓",
            "Led 10–30 person technical teams across 6 years",
            "Built the automated sourcing engine pre-LLM tools",
            "Implemented scalable ML and cloud microservices"
        ]
    }
]

# Step 2: Start Streamlit app
st.set_page_config(page_title="Resume Intelligence Tool", layout="wide")

st.title("🧠 Resume Memory Viewer")

# Sidebar navigation
page = st.sidebar.selectbox("Select View", ["Resume Viewer", "Job Matcher"])

# === Resume Viewer ===
if page == "Resume Viewer":
    st.header("📄 Resume Memory Viewer")
    for job in resume_memory:
        with st.expander(f"{job['title']} at {job['company']} ({job['start']} to {job['end']})"):
            st.markdown("**Tools Used:** " + ", ".join(job["tools"]))
            st.markdown("**Impact:**")
            for bullet in job["impact"]:
                st.markdown(f"- {bullet}")

# === Job Matcher ===
elif page == "Job Matcher":
    st.header("📌 Job Description Matcher")
    jd_text = st.text_area("Paste a job description here", height=300)

    if jd_text:
        # Very basic keyword check for now
        jd_keywords = [word.lower() for word in jd_text.split()]
        match_score = 0
        matched_tools = []

        for job in resume_memory:
            for tool in job["tools"]:
                if tool.lower() in jd_keywords:
                    match_score += 1
                    matched_tools.append(tool)

        st.markdown(f"✅ **Tool Match Score:** {match_score}")
        if matched_tools:
            st.markdown("🔍 **Matched Tools from Your Resume:**")
            st.write(", ".join(set(matched_tools)))
        else:
            st.markdown("❌ No direct tool matches found.")
        