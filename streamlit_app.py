import streamlit as st

# Define role-specific criteria
def get_role_criteria(role):
    if role == "Dental Assistant":
        return [
            "Critical thinking",
            "Works with any provider",
            "Chairside personality",
            "Understands clinical language",
            "Communicates treatment effectively",
            "Takes initiative",
            "Accepts feedback",
            "Years of experience",
            "Certifications (e.g., x-ray)",
            "Bonus skills",
        ]
    elif role == "Dental Hygienist":
        return [
            "Perio charting",
            "Scaling and Root Planing",
            "Patient education",
            "Co-diagnosis with dentist",
            "Chairside personality",
            "Autonomous work style",
            "Experience with Eaglesoft/Dentrix",
            "Languages spoken",
            "Leadership",
            "Bonus skills",
        ]
    elif role == "Front Office Coordinator":
        return [
            "Articulate with patients",
            "Great phone etiquette",
            "Multi-tasking",
            "Prioritization skills",
            "Optimistic attitude",
            "Outgoing personality",
            "Tech savvy",
            "Schedule optimization",
            "Experience with dental software",
            "Bonus skills",
        ]
    elif role == "Office Manager":
        return [
            "Leadership",
            "Conflict resolution",
            "Emotional intelligence",
            "Business acumen",
            "Understands key practice metrics",
            "Insurance fluency",
            "Bridges front and back office",
            "Understands clinical processes",
            "Effective communicator",
            "Treatment planning expertise",
            "Relationship-building with team and dentist",
            "Flexibility",
            "Self-motivation",
            "Bonus skills",
        ]
    elif role == "Insurance Coordinator":
        return [
            "Experience in dental insurance",
            "Knowledge of dental codes",
            "Understands downgrades",
            "Can verify with breakdown",
            "Checks eligibility daily",
            "Updates dental contracts",
            "Negotiates insurance fees",
            "Keeps provider info updated",
            "Bonus skills",
        ]
    elif role == "Treatment Plan Coordinator":
        return [
            "Understands presenting vs selling",
            "Knowledge of financing options",
            "Meets patients where they are",
            "Efficient treatment presentation",
            "Provides cost before appointments",
            "Quick same-day treatment costs",
            "Understands quadrant dentistry",
            "Understands priority dentistry",
            "Knows revenue impact of same-day care",
            "Bonus skills",
        ]
    else:
        return []

# Define candidate preferences
def get_candidate_preferences(role):
    if role == "Dental Assistant":
        return [
            "Trust in leadership",
            "Competitive pay",
            "Work hours",
            "Upward mobility",
            "Continued education",
            "Bonuses",
            "Knowledgeable leadership",
            "Job security",
        ]
    elif role == "Dental Hygienist":
        return [
            "Autonomy",
            "Team collaboration",
            "Fair scheduling",
            "Modern equipment",
            "Continued education",
            "Respect and support",
            "Pay structure",
            "Job security",
        ]
    elif role == "Front Office Coordinator":
        return [
            "Easeful work atmosphere",
            "Listening supervisor",
            "Great work hours",
            "Bonus capability",
            "PTO",
            "Upward mobility",
            "Trusting work environment",
            "Team environment",
        ]
    elif role == "Office Manager":
        return [
            "Trustworthy company",
            "Respect",
            "Salary transparency",
            "Comprehensive benefits",
            "Dentists they trust",
            "Supportive leadership",
            "Patient-first philosophy",
            "Work-life balance",
            "Autonomy",
        ]
    elif role in ["Insurance Coordinator", "Treatment Plan Coordinator"]:
        return [
            "Quiet work area for insurance calls",
            "Ability to earn raises",
            "Not being micromanaged",
            "Focus on insurance-only tasks",
            "Autonomy",
            "Trust from employer",
        ]
    else:
        return []

# UI Starts Here
st.title("Dental HireMatch")
st.markdown("AI-powered matching for dental employers and job seekers")

role = st.selectbox("Select Role", [
    "Dental Assistant", 
    "Dental Hygienist", 
    "Front Office Coordinator", 
    "Office Manager",
    "Insurance Coordinator",
    "Treatment Plan Coordinator"
])

st.header("Employer Criteria")
role_criteria = get_role_criteria(role)
selected_criteria = [st.checkbox(c, key=c) for c in role_criteria]

st.header("Candidate Preferences")
candidate_prefs = get_candidate_preferences(role)
selected_prefs = [st.checkbox(p, key=p) for p in candidate_prefs]
# Resume Upload Section
st.header("Upload Your Resume (PDF)")
uploaded_resume = st.file_uploader("Choose a file", type=["pdf"])

if uploaded_resume is not None:
    import os
    os.makedirs("resumes", exist_ok=True)
    with open(f"resumes/{uploaded_resume.name}", "wb") as f:
        f.write(uploaded_resume.getbuffer())
    st.success(f"Uploaded: {uploaded_resume.name}")


if st.button("Find Match"):
    score = sum(selected_criteria) + sum(selected_prefs)
    st.success(f"Matching score for {role}: {score} out of {len(role_criteria) + len(candidate_prefs)}")








