import streamlit as st

def calculate_match_score(employer, candidate):
    score = 0
    details = {}

    # Role match
    if employer.get("role") == candidate.get("role"):
        score += 20
        details["role"] = 20
    else:
        details["role"] = 0

    # Location
    if employer.get("location_zip") == candidate.get("location_zip"):
        score += 10
        details["location"] = 10
    else:
        details["location"] = 0

    # Experience
    exp_diff = candidate.get("years_experience", 0) - employer.get("min_years_experience", 0)
    if exp_diff >= 0:
        score += 15
        details["experience"] = 15
    else:
        details["experience"] = 0

    # Skills
    required_skills = set(employer.get("required_skills", []))
    candidate_skills = set(candidate.get("skills", []))
    skills_matched = required_skills.intersection(candidate_skills)
    skill_match_ratio = len(skills_matched) / max(len(required_skills), 1)
    skill_score = int(skill_match_ratio * 20)
    score += skill_score
    details["skills"] = skill_score

    # Availability
    if employer.get("availability") == candidate.get("availability"):
        score += 10
        details["availability"] = 10
    else:
        details["availability"] = 0

    # Language
    required_langs = set(employer.get("languages", []))
    candidate_langs = set(candidate.get("languages", []))
    if required_langs and required_langs.intersection(candidate_langs):
        score += 10
        details["language"] = 10
    elif not required_langs:
        score += 5
        details["language"] = 5
    else:
        details["language"] = 0

    # Culture fit
    if employer.get("culture_fit") == candidate.get("culture_fit"):
        score += 10
        details["culture_fit"] = 10
    else:
        details["culture_fit"] = 0

    # Education level
    if employer.get("education_level") == candidate.get("education_level"):
        score += 10
        details["education_level"] = 10
    else:
        details["education_level"] = 0

    # Commute
    if candidate.get("willing_to_relocate") or employer.get("location_zip") == candidate.get("location_zip"):
        score += 5
        details["commute"] = 5
    else:
        details["commute"] = 0

    # Bonus skills
    bonus_skills = set(employer.get("bonus_skills", []))
    bonus_matched = bonus_skills.intersection(candidate_skills)
    bonus_score = int((len(bonus_matched) / max(len(bonus_skills), 1)) * 10)
    score += bonus_score
    details["bonus_skills"] = bonus_score

    return score, details

def main():
    st.set_page_config(page_title="DentalMatch AI", layout="wide")

    # Custom Styling
    st.markdown(
        """
        <style>
            body { background-color: #f5f9ff; }
            .stButton>button {
                background-color: #2E86AB;
                color: white;
                border-radius: 8px;
                height: 3em;
                font-size: 16px;
            }
            .block-container {
                padding-top: 2rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # App Header
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color:#2C3E50;">🦷 DentalMatch AI</h1>
            <p style="font-size:18px; color:#444;">Smarter Hiring for Dental Practices</p>
        </div>
        """, unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧑‍⚕️ Employer Job Criteria")
        employer = {}
        employer["role"] = "Dental Assistant"
        employer["location_zip"] = st.text_input("Practice ZIP Code", max_chars=5, key="employer_zip")
        employer["min_years_experience"] = st.number_input("Minimum Years of Experience", min_value=0, max_value=50, value=1, key="employer_exp")
        
        with st.expander("🧠 Skills & Experience", expanded=True):
            employer["required_skills"] = st.multiselect("Required Skills", 
                ["Eaglesoft", "X-ray cert", "Chairside personality", "CPR", "Spanish"], key="employer_skills")
            employer["bonus_skills"] = st.multiselect("Bonus Skills", ["CPR", "Spanish", "Leadership"], key="employer_bonus")
            employer["education_level"] = st.selectbox("Minimum Education Level", ["High School Diploma", "Associate Degree", "Bachelor's Degree"], key="employer_edu")

        with st.expander("💬 Communication & Culture", expanded=True):
            employer["availability"] = st.selectbox("Availability", ["Full-time", "Part-time", "Temporary"], key="employer_avail")
            employer["languages"] = st.multiselect("Required Languages", ["English", "Spanish", "Other"], key="employer_langs")
            employer["culture_fit"] = st.selectbox("Preferred Culture Fit", ["Team player", "Independent", "Fast-paced"], key="employer_culture")

    with col2:
        st.subheader("👤 Candidate Profile")
        candidate = {}
        candidate["role"] = "Dental Assistant"
        candidate["location_zip"] = st.text_input("Your ZIP Code", max_chars=5, key="candidate_zip")
        candidate["years_experience"] = st.number_input("Years of Experience", min_value=0, max_value=50, value=0, key="candidate_exp")
        
        with st.expander("🧠 Your Skills & Background", expanded=True):
            candidate["skills"] = st.multiselect("Your Skills", 
                ["Eaglesoft", "X-ray cert", "Chairside personality", "CPR", "Spanish"], key="candidate_skills")
            candidate["education_level"] = st.selectbox("Your Education Level", ["High School Diploma", "Associate Degree", "Bachelor's Degree"], key="candidate_edu")

        with st.expander("💬 Preferences & Communication", expanded=True):
            candidate["availability"] = st.selectbox("Availability", ["Full-time", "Part-time", "Temporary"], key="candidate_avail")
            candidate["languages"] = st.multiselect("Languages You Speak", ["English", "Spanish", "Other"], key="candidate_langs")
            candidate["culture_fit"] = st.selectbox("Culture Fit You Prefer", ["Team player", "Independent", "Fast-paced"], key="candidate_culture")
            candidate["willing_to_relocate"] = st.checkbox("Willing to relocate?", key="candidate_relocate")

    st.markdown("---")

    if st.button("🎯 Calculate Match"):
        score, details = calculate_match_score(employer, candidate)
        st.success(f"🔎 Match Score: **{score} / 120**")

        st.markdown("### 📊 Match Breakdown:")
        for factor, pts in details.items():
            st.markdown(f"- **{factor.replace('_', ' ').capitalize()}**: `{pts} pts`")

if __name__ == "__main__":
    main()



