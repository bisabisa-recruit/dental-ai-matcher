import streamlit as st

def calculate_match_score(employer, candidate):
    score = 0
    details = {}
    role = employer.get("role")

    # Shared Matching Factors
    if employer.get("role") == candidate.get("role"):
        score += 20
        details["role"] = 20
    else:
        details["role"] = 0

    if employer.get("location_zip") == candidate.get("location_zip"):
        score += 10
        details["location"] = 10
    else:
        details["location"] = 0

    exp_diff = candidate.get("years_experience", 0) - employer.get("min_years_experience", 0)
    if exp_diff >= 0:
        score += 15
        details["experience"] = 15
    else:
        details["experience"] = 0

    required_skills = set(employer.get("required_skills", []))
    candidate_skills = set(candidate.get("skills", []))
    skills_matched = required_skills.intersection(candidate_skills)
    skill_score = int((len(skills_matched) / max(len(required_skills), 1)) * 20)
    score += skill_score
    details["skills"] = skill_score

    if employer.get("availability") == candidate.get("availability"):
        score += 10
        details["availability"] = 10
    else:
        details["availability"] = 0

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

    if employer.get("culture_fit") == candidate.get("culture_fit"):
        score += 10
        details["culture_fit"] = 10
    else:
        details["culture_fit"] = 0

    if employer.get("education_level") == candidate.get("education_level"):
        score += 10
        details["education_level"] = 10
    else:
        details["education_level"] = 0

    if candidate.get("willing_to_relocate") or employer.get("location_zip") == candidate.get("location_zip"):
        score += 5
        details["commute"] = 5
    else:
        details["commute"] = 0

    bonus_skills = set(employer.get("bonus_skills", []))
    bonus_matched = bonus_skills.intersection(candidate_skills)
    bonus_score = int((len(bonus_matched) / max(len(bonus_skills), 1)) * 10)
    score += bonus_score
    details["bonus_skills"] = bonus_score

    return score, details

def main():
    st.set_page_config(page_title="DentalMatch AI", layout="wide")
    st.title("🦷 DentalMatch AI")
    st.subheader("Smart Matching for Dental Hiring")

    role = st.selectbox("Select Role", ["Dental Assistant", "Dental Hygienist"])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧑‍⚕️ Employer Job Criteria")
        employer = {"role": role}
        employer["location_zip"] = st.text_input("Practice ZIP Code", max_chars=5, key="employer_zip")
        employer["min_years_experience"] = st.number_input("Minimum Years of Experience", 0, 50, key="employer_exp")
        employer["required_skills"] = st.multiselect("Required Skills", ["Eaglesoft", "Dentrix", "X-ray cert", "Perio charting", "SRPs", "Chairside personality"], key="employer_skills")
        employer["bonus_skills"] = st.multiselect("Bonus Skills", ["Leadership", "Spanish", "Digital X-rays"], key="employer_bonus")
        employer["education_level"] = st.selectbox("Minimum Education Level", ["High School Diploma", "Associate Degree", "Bachelor's Degree"], key="employer_edu")
        employer["availability"] = st.selectbox("Availability", ["Full-time", "Part-time", "Temporary"], key="employer_avail")
        employer["languages"] = st.multiselect("Required Languages", ["English", "Spanish", "Other"], key="employer_langs")
        employer["culture_fit"] = st.selectbox("Preferred Culture Fit", ["Team player", "Independent", "Fast-paced"], key="employer_culture")

    with col2:
        st.markdown("### 👤 Candidate Profile")
        candidate = {"role": role}
        candidate["location_zip"] = st.text_input("Your ZIP Code", max_chars=5, key="candidate_zip")
        candidate["years_experience"] = st.number_input("Years of Experience", 0, 50, key="candidate_exp")
        candidate["skills"] = st.multiselect("Your Skills", ["Eaglesoft", "Dentrix", "X-ray cert", "Perio charting", "SRPs", "Chairside personality"], key="candidate_skills")
        candidate["education_level"] = st.selectbox("Your Education Level", ["High School Diploma", "Associate Degree", "Bachelor's Degree"], key="candidate_edu")
        candidate["availability"] = st.selectbox("Availability", ["Full-time", "Part-time", "Temporary"], key="candidate_avail")
        candidate["languages"] = st.multiselect("Languages You Speak", ["English", "Spanish", "Other"], key="candidate_langs")
        candidate["culture_fit"] = st.selectbox("Culture Fit You Prefer", ["Team player", "Independent", "Fast-paced"], key="candidate_culture")
        candidate["willing_to_relocate"] = st.checkbox("Willing to relocate?", key="candidate_relocate")

    st.markdown("---")

    if st.button("🎯 Calculate Match"):
        score, details = calculate_match_score(employer, candidate)
        st.success(f"Match Score: {score} / 120")

        st.markdown("### Match Breakdown:")
        for factor, pts in details.items():
            st.markdown(f"- **{factor.replace('_', ' ').capitalize()}**: `{pts} pts`")

if __name__ == "__main__":
    main()





