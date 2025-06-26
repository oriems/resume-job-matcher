import streamlit as st
import json
from pathlib import Path

# Load memory from file or fall back
save_path = Path("resume_memory.json")
if save_path.exists():
    with open(save_path, "r") as f:
        resume_memory = json.load(f)
else:
    resume_memory = []

st.set_page_config(page_title="Resume Intelligence Tool", layout="wide")
st.title("🧠 Resume Intelligence Tool")

# --- Navbar style selection ---
view = st.radio("Navigation", ["Resume Viewer", "Job Matcher"], horizontal=True)

if view == "Resume Viewer":
    st.header("📄 Resume Viewer")

    # Sidebar list of jobs
    job_labels = [f"{job['company']}\n{job['title']}\n{job['start_date']} - {job['end_date']}" for job in resume_memory]
    selected_job = st.selectbox("Select a job to view/edit:", options=job_labels)
    selected_index = job_labels.index(selected_job)
    job = resume_memory[selected_index]

    st.subheader("✏️ Job Details")

    job["company"] = st.text_input("Company", value=job.get("company", ""))
    job["title"] = st.text_input("Title", value=job.get("title", ""))
    job["start_date"] = st.text_input("Start Date", value=job.get("start_date", ""))
    job["end_date"] = st.text_input("End Date", value=job.get("end_date", ""))

    st.subheader("🛠 Tools Used")
    tools = job.get("tools", {"advisor": [], "builder": [], "informed": []})
    for role in ["advisor", "builder", "informed"]:
        tools[role] = st.text_area(f"{role.capitalize()} Tools (comma-separated)", 
                                   value=", ".join(tools.get(role, []))).split(",")
        tools[role] = [t.strip() for t in tools[role] if t.strip()]
    job["tools"] = tools

    st.subheader("📌 Project Info")
    project = job.get("project", {})
    project["description"] = st.text_area("Project Description", value=project.get("description", ""))
    project["impact"] = st.text_area("Impact (bullet points, new line per bullet)", 
                                      value="\n".join(project.get("impact", []))).split("\n")
    project["impact"] = [line.strip() for line in project["impact"] if line.strip()]
    job["project"] = project

    resume_memory[selected_index] = job

    if st.button("💾 Save Changes"):
        with open(save_path, "w") as f:
            json.dump(resume_memory, f, indent=2)
        st.success("Saved successfully!")
