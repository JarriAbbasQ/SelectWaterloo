import streamlit as st

st.set_page_config(
    page_title="University of Waterloo Admission Probability Evaluator",
    page_icon="🦅",
    layout="wide"
)

# ---------------------------------------------------------
# COMPREHENSIVE WATERLOO PROGRAM DATABASE (2025/2026 CYCLE)
# ---------------------------------------------------------
WATERLOO_PROGRAMS_DB = [
    # --- FACULTY OF ENGINEERING ---
    {
        "name": "Software Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 97.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 1 (Ultra-Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 98.0 else ("Medium (25-50%)" if avg >= 97.0 else ("Low (5-15%)" if avg >= 95.0 else "Very Low (<5%)")),
        "description": "Ultra-competitive cohort program. Accepts ~5% of applicants. High 90s, stellar AIF, and coding experience are mandatory."
    },
    {
        "name": "Biomedical Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 95.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 1 (Ultra-Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 96.5 else ("Medium (30-50%)" if avg >= 95.0 else ("Low (10-20%)" if avg >= 92.0 else "Very Low (<5%)")),
        "description": "Small cohort size with high volume of applicants aiming for medical and engineering fields."
    },
    {
        "name": "Computer Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 95.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 2 (High-Demand)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 96.0 else ("Medium (35-55%)" if avg >= 95.0 else ("Low (10-20%)" if avg >= 92.0 else "Very Low (<5%)")),
        "description": "Extremely high applicant volume. Acceptance chance drops sharply below the 95% threshold."
    },
    {
        "name": "Mechatronics Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 95.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 2 (High-Demand)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 96.0 else ("Medium (35-55%)" if avg >= 95.0 else ("Low (10-20%)" if avg >= 92.0 else "Very Low (<5%)")),
        "description": "Combines mechanical, electrical, software, and robotics engineering."
    },
    {
        "name": "Electrical Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 94.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 2 (High-Demand)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 95.5 else ("Medium (40-60%)" if avg >= 94.0 else ("Low (15-25%)" if avg >= 91.0 else "Very Low (<5%)")),
        "description": "Focuses on hardware, signals, circuits, and telecommunications."
    },
    {
        "name": "Systems Design Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 94.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 2 (High-Demand)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 95.5 else ("Medium (35-50%)" if avg >= 94.0 else ("Low (10-20%)" if avg >= 91.0 else "Very Low (<5%)")),
        "description": "Interdisciplinary design program requiring high problem-solving capability."
    },
    {
        "name": "Mechanical Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 92.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 3 (Moderate Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 94.0 else ("Medium (40-60%)" if avg >= 92.0 else ("Low (15-25%)" if avg >= 89.0 else "Very Low (<5%)")),
        "description": "Largest engineering cohort. Competitive averages sit solidly in the low 90s."
    },
    {
        "name": "Management Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 91.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 3 (Moderate Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 93.0 else ("Medium (45-65%)" if avg >= 91.0 else ("Low (20-30%)" if avg >= 88.0 else "Very Low (<5%)")),
        "description": "Focuses on software, data analytics, supply chain, and operations research."
    },
    {
        "name": "Chemical Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 88.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 3 (Accessible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 90.0 else ("Medium (50-70%)" if avg >= 88.0 else ("Low (20-35%)" if avg >= 85.0 else "Very Low (<5%)")),
        "description": "Applies chemistry, physics, and math to industrial chemical and bioprocesses."
    },
    {
        "name": "Civil Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 88.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 3 (Accessible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 90.0 else ("Medium (50-70%)" if avg >= 88.0 else ("Low (20-35%)" if avg >= 85.0 else "Very Low (<5%)")),
        "description": "Focuses on infrastructure, structural design, and urban transportation."
    },
    {
        "name": "Environmental Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 87.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 3 (Accessible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 89.0 else ("Medium (50-70%)" if avg >= 87.0 else ("Low (20-35%)" if avg >= 84.0 else "Very Low (<5%)")),
        "description": "Clean energy, water resources, and environmental sustainability."
    },
    {
        "name": "Architectural Engineering (B.A.Sc.)",
        "faculty": "Faculty of Engineering",
        "min_avg": 88.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SPH4U", "SCH4U"],
        "tier": "Tier 3 (Moderate Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 91.0 else ("Medium (45-65%)" if avg >= 88.0 else ("Low (20-30%)" if avg >= 85.0 else "Very Low (<5%)")),
        "description": "Structural engineering combined with modern building design technology."
    },

    # --- FACULTY OF MATHEMATICS ---
    {
        "name": "Computer Science (B.C.S. / B.Math)",
        "faculty": "Faculty of Mathematics",
        "min_avg": 96.5,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U"],
        "tier": "Tier 1 (Ultra-Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 98.0 else ("Medium (20-40%)" if avg >= 96.5 else ("Low (5-15%)" if avg >= 94.0 else "Very Low (<5%)")),
        "description": "Acceptance rate under 5%. Averages of 96.5%+ are required to reach target cutoff."
    },
    {
        "name": "Computer Science / Business (Double Degree UW/WLU)",
        "faculty": "Faculty of Mathematics",
        "min_avg": 97.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U"],
        "tier": "Tier 1 (Ultra-Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 98.5 else ("Medium (20-40%)" if avg >= 97.0 else ("Low (5-10%)" if avg >= 94.5 else "Very Low (<5%)")),
        "description": "Awards B.C.S. from Waterloo and BBA from Laurier. Requires high 90s."
    },
    {
        "name": "Computing and Financial Management (B.C.F.M.)",
        "faculty": "Faculty of Mathematics",
        "min_avg": 95.5,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U"],
        "tier": "Tier 1 (Ultra-Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 97.0 else ("Medium (30-50%)" if avg >= 95.5 else ("Low (10-20%)" if avg >= 93.0 else "Very Low (<5%)")),
        "description": "Combines Computer Science with Financial Management. Highly selective."
    },
    {
        "name": "Mathematics (Honours B.Math)",
        "faculty": "Faculty of Mathematics",
        "min_avg": 93.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U"],
        "tier": "Tier 2 (High-Demand)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 95.0 else ("Medium (45-65%)" if avg >= 93.0 else ("Low (15-30%)" if avg >= 90.0 else "Very Low (<5%)")),
        "description": "Entry pathway for Actuarial Science, Statistics, Combinatorics, and Pure Math."
    },
    {
        "name": "Math / Business Administration (Double Degree UW/WLU)",
        "faculty": "Faculty of Mathematics",
        "min_avg": 93.5,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U"],
        "tier": "Tier 2 (High-Demand)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 95.5 else ("Medium (40-60%)" if avg >= 93.5 else ("Low (15-25%)" if avg >= 90.0 else "Very Low (<5%)")),
        "description": "Dual B.Math (Waterloo) and BBA (Laurier) degrees."
    },

    # --- FACULTY OF SCIENCE ---
    {
        "name": "Biomedical Sciences (B.Sc.)",
        "faculty": "Faculty of Science",
        "min_avg": 88.0,
        "prereqs": ["ENG4U", "MHF4U", "SBI4U", "SCH4U"],
        "tier": "Tier 3 (Moderate Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 91.0 else ("Medium (45-65%)" if avg >= 88.0 else ("Low (20-30%)" if avg >= 84.0 else "Very Low (<5%)")),
        "description": "Primary pre-med and pre-optometry pathway."
    },
    {
        "name": "Biotechnology & CPA (B.Sc./CPA)",
        "faculty": "Faculty of Science",
        "min_avg": 89.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U", "SCH4U"],
        "tier": "Tier 3 (Moderate Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 92.0 else ("Medium (45-65%)" if avg >= 89.0 else ("Low (20-30%)" if avg >= 85.0 else "Very Low (<5%)")),
        "description": "Combines science and commercial accounting credentials."
    },
    {
        "name": "Honours Science (B.Sc.)",
        "faculty": "Faculty of Science",
        "min_avg": 80.0,
        "prereqs": ["ENG4U", "MHF4U", "SCH4U"],
        "tier": "Tier 5 (Flexible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 83.0 else ("Medium (50-70%)" if avg >= 80.0 else ("Low (20-35%)" if avg >= 76.0 else "Very Low (<5%)")),
        "description": "Flexible science curriculum."
    },

    # --- FACULTY OF HEALTH ---
    {
        "name": "Health Sciences (B.Sc.)",
        "faculty": "Faculty of Health",
        "min_avg": 87.0,
        "prereqs": ["ENG4U", "MHF4U", "SBI4U", "SCH4U"],
        "tier": "Tier 3 (Moderate Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 90.0 else ("Medium (45-65%)" if avg >= 87.0 else ("Low (20-30%)" if avg >= 83.0 else "Very Low (<5%)")),
        "description": "Human health, epidemiology, and health policy."
    },
    {
        "name": "Kinesiology (B.Sc.)",
        "faculty": "Faculty of Health",
        "min_avg": 84.0,
        "prereqs": ["ENG4U", "MHF4U", "SBI4U"],
        "tier": "Tier 4 (Accessible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 87.0 else ("Medium (50-70%)" if avg >= 84.0 else ("Low (20-35%)" if avg >= 80.0 else "Very Low (<5%)")),
        "description": "Biomechanics, exercise science, and human physiology."
    },

    # --- FACULTY OF ENVIRONMENT ---
    {
        "name": "Planning (B.E.S.)",
        "faculty": "Faculty of Environment",
        "min_avg": 84.0,
        "prereqs": ["ENG4U"],
        "tier": "Tier 4 (Accessible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 86.0 else ("Medium (50-70%)" if avg >= 84.0 else ("Low (20-35%)" if avg >= 80.0 else "Very Low (<5%)")),
        "description": "Accredited professional urban planning program."
    },
    {
        "name": "Sustainability and Financial Management (S.F.M.)",
        "faculty": "Faculty of Environment",
        "min_avg": 88.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U"],
        "tier": "Tier 3 (Moderate Competitive)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 91.0 else ("Medium (45-65%)" if avg >= 88.0 else ("Low (20-30%)" if avg >= 84.0 else "Very Low (<5%)")),
        "description": "ESG reporting and sustainable finance program offered with SAF."
    },

    # --- FACULTY OF ARTS ---
    {
        "name": "Accounting and Financial Management (A.F.M.)",
        "faculty": "Faculty of Arts",
        "min_avg": 90.0,
        "prereqs": ["ENG4U", "MHF4U", "MCV4U"],
        "tier": "Tier 2 (High-Demand)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 92.5 else ("Medium (40-60%)" if avg >= 90.0 else ("Low (15-30%)" if avg >= 87.0 else "Very Low (<5%)")),
        "description": "Selective business degree. Requires SAFAA online interview & video submission."
    },
    {
        "name": "Global Business and Digital Arts (G.B.D.A.)",
        "faculty": "Faculty of Arts",
        "min_avg": 83.0,
        "prereqs": ["ENG4U"],
        "tier": "Tier 4 (Accessible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 86.0 else ("Medium (50-70%)" if avg >= 83.0 else ("Low (20-35%)" if avg >= 79.0 else "Very Low (<5%)")),
        "description": "Combines UX/UI design, digital media, and business at Stratford Campus."
    },
    {
        "name": "Honours Arts (B.A.)",
        "faculty": "Faculty of Arts",
        "min_avg": 78.0,
        "prereqs": ["ENG4U"],
        "tier": "Tier 5 (Flexible Entry)",
        "probability_function": lambda avg: "High (>70%)" if avg >= 81.0 else ("Medium (50-70%)" if avg >= 78.0 else ("Low (20-35%)" if avg >= 74.0 else "Very Low (<5%)")),
        "description": "Broad humanities and social science entry pathway."
    }
]

ALL_FACULTIES = [
    "Faculty of Engineering",
    "Faculty of Mathematics",
    "Faculty of Science",
    "Faculty of Health",
    "Faculty of Environment",
    "Faculty of Arts"
]

def parse_percentage_input(val_str):
    if not val_str or val_str.strip() == "":
        return 0.0
    try:
        val = float(val_str.strip())
        return val if 0.0 <= val <= 100.0 else 0.0
    except ValueError:
        return 0.0

def calculate_top6_avg(courses_dict):
    valid_marks = [v for v in courses_dict.values() if v > 0]
    if not valid_marks:
        return 0.0
    valid_marks.sort(reverse=True)
    top_6 = valid_marks[:6]
    return sum(top_6) / len(top_6)

def check_prereqs(student_courses, program_prereqs):
    student_keys = set(student_courses.keys())
    missing = [req for req in program_prereqs if req not in student_keys]
    return len(missing) == 0, missing

# ---------------------------------------------------------
# MAIN APP INTERFACE
# ---------------------------------------------------------
st.title("🦅 University of Waterloo Admission Probability Evaluator")
st.markdown("Designed for **Ontario High School Students (OUAC 101 / Grade 12 4U/4M)** using realistic historical admission probabilities.")

st.sidebar.header("📋 Student Profile & Filters")
student_name = st.sidebar.text_input("Student Name", "")
st.sidebar.markdown("---")
selected_faculties = st.sidebar.multiselect("Filter Faculties", ALL_FACULTIES, default=ALL_FACULTIES)

st.header("📊 Grade 12 (4U/4M) Course Marks Input")
tab_math_sci, tab_humanities, tab_electives = st.tabs(["📐 Math & Sciences", "📖 English & Social Sci", "💻 Business & Tech"])

with tab_math_sci:
    c1, c2, c3 = st.columns(3)
    mhf4u = c1.text_input("MHF4U (Advanced Functions)", value="", placeholder="e.g. 92", key="mhf4u")
    mcv4u = c2.text_input("MCV4U (Calculus & Vectors)", value="", placeholder="e.g. 90", key="mcv4u")
    mdm4u = c3.text_input("MDM4U (Data Management)", value="", placeholder="", key="mdm4u")
    sph4u = c1.text_input("SPH4U (Physics)", value="", placeholder="e.g. 88", key="sph4u")
    sch4u = c2.text_input("SCH4U (Chemistry)", value="", placeholder="e.g. 85", key="sch4u")
    sbi4u = c3.text_input("SBI4U (Biology)", value="", placeholder="", key="sbi4u")

with tab_humanities:
    c1, c2, c3 = st.columns(3)
    eng4u = c1.text_input("ENG4U (Grade 12 English)", value="", placeholder="e.g. 90", key="eng4u")
    cia4u = c2.text_input("CIA4U (Economics)", value="", placeholder="", key="cia4u")
    cgw4u = c3.text_input("CGW4U (World Issues)", value="", placeholder="", key="cgw4u")

with tab_electives:
    c1, c2, c3 = st.columns(3)
    bat4m = c1.text_input("BAT4M (Accounting)", value="", placeholder="", key="bat4m")
    ics4u = c2.text_input("ICS4U (Computer Science)", value="", placeholder="", key="ics4u")
    elec1 = c3.text_input("Elective 1 (4U/4M)", value="", placeholder="e.g. 88", key="elec1")

all_raw_courses = {
    "ENG4U": parse_percentage_input(eng4u),
    "MHF4U": parse_percentage_input(mhf4u),
    "MCV4U": parse_percentage_input(mcv4u),
    "MDM4U": parse_percentage_input(mdm4u),
    "SPH4U": parse_percentage_input(sph4u),
    "SCH4U": parse_percentage_input(sch4u),
    "SBI4U": parse_percentage_input(sbi4u),
    "ICS4U": parse_percentage_input(ics4u),
    "CIA4U": parse_percentage_input(cia4u),
    "CGW4U": parse_percentage_input(cgw4u),
    "BAT4M": parse_percentage_input(bat4m),
    "Elective 1": parse_percentage_input(elec1),
}

student_courses = {k: v for k, v in all_raw_courses.items() if v > 0.0}
top6_avg = calculate_top6_avg(student_courses)

st.markdown("---")
st.header("🎯 Program Admission Probability Breakdown")

m1, m2, m3 = st.columns(3)
m1.metric("Student Name", student_name if student_name else "Candidate")
m2.metric("Courses Entered", f"{len(student_courses)}")
m3.metric("Calculated Top 6 Average", f"{top6_avg:.1f}%" if student_courses else "N/A")

if len(student_courses) < 3:
    st.info("💡 Enter marks for at least 3 to 6 Grade 12 (4U/4M) courses above to generate probability projections.")
else:
    filtered_programs = [p for p in WATERLOO_PROGRAMS_DB if p["faculty"] in selected_faculties]

    target_met = []
    reach_met = []
    missing_prereq_progs = []

    for prog in filtered_programs:
        has_prereqs, missing = check_prereqs(student_courses, prog["prereqs"])
        prob_str = prog["probability_function"](top6_avg)

        # STRICT TARGET RULE: Average MUST meet or exceed the competitive baseline AND probability cannot be Low/Very Low
        is_target_avg = top6_avg >= prog["min_avg"]
        is_medium_or_high_prob = any(tag in prob_str for tag in ["High", "Medium"])

        if not has_prereqs:
            missing_prereq_progs.append((prog, missing, prob_str))
        elif is_target_avg and is_medium_or_high_prob:
            target_met.append((prog, prob_str))
        else:
            reach_met.append((prog, prob_str))

    # GREEN CIRCLE SECTION
    st.subheader("🟢 Competitive & Realistic Target Options (Average >= Baseline)")
    if target_met:
        for prog, prob in target_met:
            with st.expander(f"🟢 **{prog['name']}** | Admission Probability: **{prob}** | Competitive Cutoff: ~{prog['min_avg']:.1f}%"):
                st.write(f"**Faculty:** {prog['faculty']} ({prog['tier']})")
                st.write(f"**Required Prerequisites:** {', '.join(prog['prereqs'])}")
                st.write(f"**Overview:** {prog['description']}")
                st.success(f"✔ **Estimated Chance of Offer:** **{prob}**. Your top 6 average (**{top6_avg:.1f}%**) meets or exceeds the baseline threshold (**{prog['min_avg']:.1f}%**).")
    else:
        st.write("No programs currently fall into the Target tier. (Your average is below the realistic competitive baselines for selected options).")

    # BLUE CIRCLE SECTION
    st.subheader("🔵 Reach / Below Baseline Options (Average < Baseline or Low Probability)")
    if reach_met:
        for prog, prob in reach_met:
            gap = prog["min_avg"] - top6_avg
            with st.expander(f"🔵 **{prog['name']}** | Admission Probability: **{prob}** | Competitive Cutoff: ~{prog['min_avg']:.1f}%"):
                st.write(f"**Faculty:** {prog['faculty']} ({prog['tier']})")
                st.write(f"**Required Prerequisites:** {', '.join(prog['prereqs'])}")
                st.write(f"**Overview:** {prog['description']}")
                if gap > 0:
                    st.warning(f"⚠️ **Estimated Chance of Offer:** **{prob}**. Your average (**{top6_avg:.1f}%**) is **-{gap:.1f}%** below the competitive baseline (**{prog['min_avg']:.1f}%**).")
                else:
                    st.warning(f"⚠️ **Estimated Chance of Offer:** **{prob}**. High competition level for this program makes admission a reach.")
    else:
        st.write("No reach programs flagged.")

    # RED CIRCLE SECTION
    st.subheader("🔴 Missing Mandatory Prerequisite Courses")
    if missing_prereq_progs:
        for prog, missing, prob in missing_prereq_progs:
            with st.expander(f"🔴 **{prog['name']}** | Missing: {', '.join(missing)} | Estimated Probability if Completed: **{prob}**"):
                st.write(f"**Faculty:** {prog['faculty']}")
                st.write(f"**Required Prerequisites:** {', '.join(prog['prereqs'])}")
                st.error(f"❌ **You cannot receive an offer without:** {', '.join(missing)}")
                st.write(f"If prerequisites are fulfilled, your estimated probability based on your current top 6 average ({top6_avg:.1f}%) would be **{prob}**.")
    else:
        st.write("No programs currently flagged for missing prerequisites.")

# DISCLAIMER
st.markdown("---")
st.markdown("""
### 📌 Admissions Disclaimer & Important Notes
* **Statistical Probabilities:** Admission probability projections are modeled from historical **University of Waterloo admissions data (2022–2026 cycles)**.
* **Non-Grade Admissions Variables:**
  * **AIF (Admission Information Form):** Adds up to **5% equivalent** to an application score in Engineering and CS.
  * **High School Adjustment Factors:** Engineering applies variable adjustment factors depending on historical school performance.
  * **Contests:** Strong performance on the **Euclid** and **CSMC** math contests significantly enhances Math/CS application outcomes.
""")
