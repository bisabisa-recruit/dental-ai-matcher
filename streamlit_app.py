import streamlit as st

st.title("🦷 Dental Assistant Match Platform")

user_type = st.sidebar.radio("I am a:", ["Employer", "Candidate"])

if user_type == "Employer":
    st.header("📄 Employer Job Post Form - Dental Assistant")

    st.subheader("Job Basics")
    location = st.text_input("Job Location (City, State or ZIP)")
    employment_type = st.multiselect("Employment Type", ["Full-time", "Part-time", "Temp"])
    schedule = st.text_input("Work Schedule (e.g., Mon–Thu, 7am–4pm)")
    pay_range = st.slider("Hourly Pay Range ($)", 10, 60, (20, 30))
    benefits = st.multiselect("Benefits Offered", ["Health", "PTO", "401k", "Bonuses", "CE Reimbursement"])

    st.subheader("What You’re Looking For")
    years_experience = st.number_input("Minimum Years of Experience Required", 0, 30, 1)
    certifications = st.multiselect("Must-Have Certifications", ["X-ray", "CPR", "RDA", "Other"])
    software = st.multiselect("Dental Software Used", ["Eaglesoft", "Dentrix", "OpenDental", "Other"])
    skills = st.multiselect("Key Skills", [
        "Communicates treatment clearly", "Understands clinical terms", "Works efficiently",
        "Takes initiative", "Coachable", "Chairside personality", "Can assist multiple providers"
    ])
    culture_keywords = st.text_input("Culture Keywords (comma-separated)")
    languages = st.text_input("Preferred Languages (optional)")

elif user_type == "Candidate":
    st.header("👤 Candidate Profile - Dental Assistant")

    st.subheader("Your Basics")
    zip_code = st.text_input("Your ZIP Code")
    commute = st.selectbox("Willing to Commute", ["<10mi", "<20mi", "Open to Relocate"])
    work_pref = st.multiselect("Work Preference", ["Full-time", "Part-time", "Temp"])

    st.subheader("Skills & Experience")
    years_experience = st.number_input("Years of Experience", 0, 30, 1)
    certifications = st.multiselect("Certifications", ["X-ray", "CPR", "RDA", "Other"])
    software = st.multiselect("Software Experience", ["Eaglesoft", "Dentrix", "OpenDental", "Other"])
    st.markdown("**Rate yourself (1–5)**")
    explain_rating = st.slider("Communicating treatment plans", 1, 5, 3)
    terms_rating = st.slider("Understanding clinical terms", 1, 5, 3)
    efficiency_rating = st.slider("Speed & efficiency", 1, 5, 3)
    coachability_rating = st.slider("Coachability", 1, 5, 3)
    initiative_rating = st.slider("Initiative", 1, 5, 3)
    chairside_rating = st.slider("Chairside personality", 1, 5, 3)

    st.subheader("Your Ideal Dental Home")
    wants = st.multiselect("I'm looking for", [
        "Trust-based environment", "Competitive pay/benefits", "Growth opportunities",
        "Continuing education", "Bonuses", "Knowledgeable leadership", "Job security"
    ])
    pref_schedule = st.text_input("Preferred Schedule (e.g., 4-day work week)")
    min_rate = st.number_input("Minimum Hourly Rate ($)", 10, 60, 20)
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
    employer_edu = employer.get("education_level", "").lower()
    candidate_edu = candidate.get("education_level", "").lower()
    if employer_edu and candidate_edu and employer_edu == candidate_edu:
        score += 10
        details["education_level"] = 10
    else:
        details["education_level"] = 0

    # Commute willingness
    if candidate.get("willing_to_relocate", False) or employer.get("location_zip") == candidate.get("location_zip"):
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
    st.title("Dental Assistant Hiring Match")

    st.header("Employer Job Criteria")
    employer = {}
    employer["role"] = "Dental Assistant"  # Fixed for now
    employer["location_zip"] = st.text_input("Practice ZIP Code", max_chars=5, key="employer_zip")
    employer["min_years_experience"] = st.number_input("Minimum Years of Experience", min_value=0, max_value=50, value=1, key="employer_exp")
    employer["required_skills"] = st.multiselect("Required Skills", 
        ["Eaglesoft", "X-ray cert", "Chairside personality", "CPR", "Spanish"], key="employer_skills")
    employer["availability"] = st.selectbox("Availability", ["Full-time", "Part-time", "Temporary"], key="employer_avail")
    employer["languages"] = st.multiselect("Required Languages", ["English", "Spanish", "Other"], key="employer_langs")
    employer["culture_fit"] = st.selectbox("Preferred Culture Fit", ["Team player", "Independent", "Fast-paced"], key="employer_culture")
    employer["education_level"] = st.selectbox("Minimum Education Level", ["High School Diploma", "Associate Degree", "Bachelor's Degree"], key="employer_edu")
    employer["bonus_skills"] = st.multiselect("Bonus Skills", ["CPR", "Spanish", "Leadership"], key="employer_bonus")

    st.markdown("---")

    st.header("Candidate Profile")
    candidate = {}
    candidate["role"] = "Dental Assistant"  # Fixed for now
    candidate["location_zip"] = st.text_input("Your ZIP Code", max_chars=5, key="candidate_zip")
    candidate["years_experience"] = st.number_input("Years of Experience", min_value=0, max_value=50, value=0, key="candidate_exp")
    candidate["skills"] = st.multiselect("Your Skills", 
        ["Eaglesoft", "X-ray cert", "Chairside personality", "CPR", "Spanish"], key="candidate_skills")
    candidate["availability"] = st.selectbox("Availability", ["Full-time", "Part-time", "Temporary"], key="candidate_avail")
    candidate["languages"] = st.multiselect("Languages You Speak", ["English", "Spanish", "Other"], key="candidate_langs")
    candidate["culture_fit"] = st.selectbox("Culture Fit You Prefer", ["Team player", "Independent", "Fast-paced"], key="candidate_culture")
    candidate["education_level"] = st.selectbox("Your Education Level", ["High School Diploma", "Associate Degree", "Bachelor's Degree"], key="candidate_edu")
    candidate["willing_to_relocate"] = st.checkbox("Willing to relocate?", key="candidate_relocate")

    if st.button("Calculate Match"):
        score, details = calculate_match_score(employer, candidate)
        st.subheader(f"Match Score: {score} / 120")
        st.write("Match Breakdown:")
        for factor, pts in details.items():
            st.write(f"- **{factor.capitalize().replace('_',' ')}**: {pts} points")

if __name__ == "__main__":
    main()


