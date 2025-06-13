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

