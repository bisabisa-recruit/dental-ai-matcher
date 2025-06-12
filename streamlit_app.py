import streamlit as st

# Sample candidate and job data for demonstration
candidates = [
    {
        "name": "Alice",
        "role": "Dental Hygienist",
        "experience_years": 4,
        "state_license": True,
        "location": "Jackson, MS",
        "preferred_office_style": "family-focused",
        "soft_skills": ["punctual", "team-oriented"],
        "specialty_experience": ["pediatrics"]
    },
    {
        "name": "Brandon",
        "role": "Dental Assistant",
        "experience_years": 3,
        "state_license": False,
        "location": "Jackson, MS",
        "preferred_office_style": "fast-paced",
        "soft_skills": ["adaptable", "reliable"],
        "specialty_experience": ["orthodontics"]
    },
    {
        "name": "Chloe",
        "role": "Dental Hygienist",
        "experience_years": 5,
        "state_license": True,
        "location": "Jackson, MS",
        "preferred_office_style": "family-focused",
        "soft_skills": ["team-oriented", "punctual"],
        "specialty_experience": ["pediatrics", "geriatrics"]
    }
]

def calculate_match_score(candidate, job):
    score = 0
    if candidate["role"] == job["role"]:
        score += 10
    if candidate["experience_years"] >= job["required_experience"]:
        score += 10
    if candidate["state_license"] == job["state_license_required"]:
        score += 10
    if candidate["location"] == job["location"]:
        score += 10
    if candidate["preferred_office_style"] == job["office_style"]:
        score += 5
    skill_overlap = set(candidate["soft_skills"]) & set(job["preferred_skills"])
    score += len(skill_overlap) * 3
    specialty_overlap = set(candidate["specialty_experience"]) & set(job["specialty"])
    score += len(specialty_overlap) * 5
    return score

# UI
st.title("🦷 Dental Hire Match AI")
st.write("Use AI to evaluate how well dental candidates match your open role.")

# Job input form
with st.form("job_form"):
    role = st.selectbox("Role", ["Dental Hygienist", "Dental Assistant"])
    required_experience = st.slider("Required Experience (Years)", 0, 10, 2)
    license_required = st.checkbox("License Required", value=True)
    location = st.text_input("Location", "Jackson, MS")
    office_style = st.selectbox("Office Style", ["family-focused", "fast-paced", "luxury", "pediatric"])
    preferred_skills = st.multiselect("Preferred Soft Skills", ["punctual", "team-oriented", "adaptable", "reliable"])
    specialties = st.multiselect("Specialty Needs", ["pediatrics", "orthodontics", "geriatrics"])
    submitted = st.form_submit_button("Calculate Match Scores")

if submitted:
    job_posting = {
        "role": role,
        "required_experience": required_experience,
        "state_license_required": license_required,
        "location": location,
        "office_style": office_style,
        "preferred_skills": preferred_skills,
        "specialty": specialties
    }

    st.subheader("🧑‍⚕️ Candidate Match Scores")
    for candidate in candidates:
        score = calculate_match_score(candidate, job_posting)
        st.write(f"**{candidate['name']}** - Match Score: {score}/60")
