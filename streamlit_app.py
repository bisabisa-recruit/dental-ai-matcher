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
            "Salary transpare







