import streamlit as st
import pandas as pd

from modules.data import load_internships, load_students
from modules.recommendation import recommend_internships
from modules.learning import (
    load_courses,
    get_learning_recommendations,
)
from modules.quiz import (
    load_quizzes,
    get_quiz_by_topic,
    calculate_quiz_score,
)
from modules.company import load_companies, add_internship
from modules.analytics import calculate_statistics


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI-Based Internship Recommendation System",
    page_icon="🎓",
    layout="wide",
)


# ============================================================
# LOAD DATA
# ============================================================

internships = load_internships()
students = load_students()
courses = load_courses()
quizzes = load_quizzes()
companies = load_companies()


# ============================================================
# SESSION STATE
# ============================================================

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if "selected_student" not in st.session_state:
    st.session_state.selected_student = None

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = None

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎓 Internship AI")

st.sidebar.markdown(
    "### AI-Based Internship Recommendation System"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Student Portal",
        "Company Portal",
        "Learning Path",
        "Quiz",
        "Analytics",
    ],
)


# ============================================================
# HOME
# ============================================================

if page == "Home":

    st.title("AI-Based Internship Recommendation System")

    st.markdown(
        """
        ### Find internships that match your skills and career goals.

        This system uses a hybrid recommendation approach to compare
        student profiles with internship opportunities.
        """
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Internships",
            len(internships)
        )

    with col2:
        st.metric(
            "Students",
            len(students)
        )

    with col3:
        st.metric(
            "Companies",
            len(companies)
        )

    with col4:
        st.metric(
            "Courses",
            len(courses)
        )

    st.divider()

    st.subheader("System Features")

    feature_col1, feature_col2 = st.columns(2)

    with feature_col1:

        st.markdown(
            """
            **Student Features**

            - Student profile
            - AI internship recommendations
            - Skill matching
            - Skill-gap analysis
            - Learning recommendations
            - Quiz and assessment
            - Progress tracking
            """
        )

    with feature_col2:

        st.markdown(
            """
            **Company Features**

            - Company profile
            - Internship posting
            - Required skill specification
            - Internship management
            - Candidate matching
            """
        )

    st.divider()

    st.info(
        "Select Student Portal or Company Portal from the sidebar to begin."
    )


# ============================================================
# STUDENT PORTAL
# ============================================================

elif page == "Student Portal":

    st.title("🎓 Student Portal")

    st.write(
        "Enter your student information to generate personalized internship recommendations."
    )

    student_id = st.selectbox(
        "Select Student",
        students["student_id"].tolist()
    )

    student = students[
        students["student_id"] == student_id
    ].iloc[0]

    st.divider()

    # Student profile

    st.subheader("Student Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Name**")
        st.write(student["name"])

        st.write("**Degree**")
        st.write(student["degree"])

    with col2:
        st.write("**Branch**")
        st.write(student["branch"])

        st.write("**CGPA**")
        st.write(student["cgpa"])

    with col3:
        st.write("**Preferred Domain**")
        st.write(student["preferred_domain"])

        st.write("**Preferred Location**")
        st.write(student["preferred_location"])

    st.write("**Skills**")
    st.write(student["skills"])

    st.write("**Preferred Work Mode**")
    st.write(student["preferred_work_mode"])

    st.write("**Expected Stipend**")
    st.write(f"₹{student['expected_stipend']}")

    st.divider()

    if st.button(
        "Generate AI Recommendations",
        type="primary"
    ):

        recommendations = recommend_internships(
            student,
            internships
        )

        st.session_state.recommendations = recommendations
        st.session_state.selected_student = student_id

    # Display recommendations

    if (
        st.session_state.recommendations
        and st.session_state.selected_student == student_id
    ):

        st.subheader("Recommended Internships")

        recommendations = st.session_state.recommendations

        for index, recommendation in enumerate(
            recommendations[:5],
            start=1
        ):

            score = recommendation["score"]

            with st.expander(
                f"{index}. {recommendation['role']} - "
                f"{recommendation['company']} | "
                f"Match: {score}%"
            ):

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Company:** "
                        f"{recommendation['company']}"
                    )

                    st.write(
                        f"**Role:** "
                        f"{recommendation['role']}"
                    )

                    st.write(
                        f"**Domain:** "
                        f"{recommendation['domain']}"
                    )

                    st.write(
                        f"**Location:** "
                        f"{recommendation['location']}"
                    )

                    st.write(
                        f"**Work Mode:** "
                        f"{recommendation['work_mode']}"
                    )

                with col2:

                    st.write(
                        f"**Stipend:** "
                        f"₹{recommendation['stipend']}"
                    )

                    st.write(
                        f"**Employer Rating:** "
                        f"{recommendation['employer_rating']:.1f}/100"
                    )

                    st.write(
                        f"**Skill Match:** "
                        f"{recommendation['skill_match']}%"
                    )

                    st.write(
                        f"**Domain Match:** "
                        f"{recommendation['domain_match']}%"
                    )

                    st.write(
                        f"**Location Match:** "
                        f"{recommendation['location_match']}%"
                    )

                st.write(
                    "**Required Skills:** "
                    + str(
                        recommendation["required_skills"]
                    )
                )

                matched = recommendation[
                    "matched_skills"
                ]

                missing = recommendation[
                    "missing_skills"
                ]

                st.write(
                    "**Matched Skills:** "
                    + (
                        ", ".join(matched)
                        if matched
                        else "None"
                    )
                )

                if missing:

                    st.warning(
                        "**Skill Gap:** "
                        + ", ".join(missing)
                    )

                else:

                    st.success(
                        "You have all required skills "
                        "for this internship."
                    )


# ============================================================
# COMPANY PORTAL
# ============================================================

elif page == "Company Portal":

    st.title("🏢 Company Portal")

    st.write(
        "Companies can view their profile and post internship opportunities."
    )

    company_names = companies[
        "company_name"
    ].tolist()

    selected_company = st.selectbox(
        "Select Company",
        company_names
    )

    company = companies[
        companies["company_name"] == selected_company
    ].iloc[0]

    st.divider()

    st.subheader("Company Profile")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.write("**Company Name**")
        st.write(company["company_name"])

    with col2:

        st.write("**Industry**")
        st.write(company["industry"])

    with col3:

        st.write("**Location**")
        st.write(company["location"])

    st.divider()

    st.subheader("Post New Internship")

    with st.form("internship_form"):

        internship_id = st.text_input(
            "Internship ID"
        )

        role = st.text_input(
            "Internship Role"
        )

        domain = st.text_input(
            "Domain"
        )

        required_skills = st.text_input(
            "Required Skills",
            placeholder="Python, SQL, Git"
        )

        location = st.text_input(
            "Location"
        )

        work_mode = st.selectbox(
            "Work Mode",
            [
                "Remote",
                "Hybrid",
                "On-site"
            ]
        )

        stipend = st.number_input(
            "Stipend",
            min_value=0,
            step=1000
        )

        employer_rating = st.slider(
            "Employer Rating",
            min_value=1.0,
            max_value=5.0,
            value=4.0,
            step=0.1
        )

        submitted = st.form_submit_button(
            "Post Internship"
        )

    if submitted:

        if (
            internship_id
            and role
            and domain
            and required_skills
            and location
        ):

            new_internship = {
                "internship_id": internship_id,
                "company": selected_company,
                "role": role,
                "domain": domain,
                "required_skills": required_skills,
                "location": location,
                "work_mode": work_mode,
                "stipend": stipend,
                "employer_rating": employer_rating,
            }

            internships = add_internship(
                new_internship,
                internships
            )

            st.success(
                "Internship posted successfully."
            )

        else:

            st.error(
                "Please fill in all required fields."
            )

    st.divider()

    st.subheader("Available Internships")

    company_internships = internships[
        internships["company"] == selected_company
    ]

    if not company_internships.empty:

        st.dataframe(
            company_internships,
            use_container_width=True
        )

    else:

        st.info(
            "No internships are currently posted by this company."
        )


# ============================================================
# LEARNING PATH
# ============================================================

elif page == "Learning Path":

    st.title("📚 Personalized Learning Path")

    st.write(
        "Identify missing skills and find learning resources to improve your profile."
    )

    student_id = st.selectbox(
        "Select Student",
        students["student_id"].tolist(),
        key="learning_student"
    )

    student = students[
        students["student_id"] == student_id
    ].iloc[0]

    recommendations = recommend_internships(
        student,
        internships
    )

    if recommendations:

        best_match = recommendations[0]

        st.subheader(
            "Top Recommended Internship"
        )

        st.success(
            f"{best_match['role']} at "
            f"{best_match['company']}"
        )

        missing_skills = best_match[
            "missing_skills"
        ]

        st.write(
            "**Missing Skills:**"
        )

        if missing_skills:

            st.warning(
                ", ".join(missing_skills)
            )

            learning_recommendations = \
                get_learning_recommendations(
                    missing_skills,
                    courses
                )

            st.subheader(
                "Recommended Learning Resources"
            )

            if learning_recommendations:

                for course in learning_recommendations:

                    st.markdown(
                        f"""
                        ### {course['course_name']}

                        **Skills:** {course['skills']}

                        **Platform:** {course['platform']}

                        **Level:** {course['level']}
                        """
                    )

                    st.divider()

            else:

                st.info(
                    "No matching learning resources found."
                )

        else:

            st.success(
                "You already have all required skills for the top recommendation."
            )


# ============================================================
# QUIZ
# ============================================================

elif page == "Quiz":

    st.title("📝 Skill Assessment Quiz")

    topics = sorted(
        quizzes["topic"].unique()
    )

    selected_topic = st.selectbox(
        "Select Topic",
        topics
    )

    topic_questions = get_quiz_by_topic(
        quizzes,
        selected_topic
    )

    st.write(
        f"Number of questions: "
        f"{len(topic_questions)}"
    )

    answers = []

    for index, (_, question) in enumerate(
        topic_questions.iterrows(),
        start=1
    ):

        st.subheader(
            f"Question {index}"
        )

        st.write(
            question["question"]
        )

        answer = st.radio(
            "Choose an answer:",
            [
                question["option_a"],
                question["option_b"],
                question["option_c"],
                question["option_d"],
            ],
            key=f"question_{question['question_id']}"
        )

        option_map = {
            question["option_a"]:
                "A",
            question["option_b"]:
                "B",
            question["option_c"]:
                "C",
            question["option_d"]:
                "D",
        }

        answers.append(
            option_map[answer]
        )

    if st.button(
        "Submit Quiz",
        type="primary"
    ):

        question_records = (
            topic_questions
            .to_dict("records")
        )

        score = calculate_quiz_score(
            question_records,
            answers
        )

        st.session_state.quiz_score = score
        st.session_state.quiz_submitted = True

    if st.session_state.quiz_submitted:

        score = st.session_state.quiz_score

        st.divider()

        st.subheader("Quiz Result")

        st.metric(
            "Your Score",
            f"{score}%"
        )

        if score >= 80:

            st.success(
                "Excellent performance!"
            )

        elif score >= 60:

            st.info(
                "Good performance. Keep practicing."
            )

        else:

            st.warning(
                "You should review this topic and try again."
            )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "Analytics":

    st.title("📊 Analytics Dashboard")

    recommendations = []

    for _, student in students.iterrows():

        student_recommendations = \
            recommend_internships(
                student,
                internships
            )

        recommendations.extend(
            student_recommendations
        )

    statistics = calculate_statistics(
        internships,
        recommendations
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Internships",
            statistics["total_internships"]
        )

    with col2:

        st.metric(
            "Total Recommendations",
            statistics["total_recommendations"]
        )

    with col3:

        st.metric(
            "Average Recommendation Score",
            f"{statistics['average_score']}%"
        )

    st.divider()

    st.subheader(
        "Internships by Domain"
    )

    domain_counts = (
        internships["domain"]
        .value_counts()
    )

    st.bar_chart(
        domain_counts
    )

    st.subheader(
        "Internships by Work Mode"
    )

    work_mode_counts = (
        internships["work_mode"]
        .value_counts()
    )

    st.bar_chart(
        work_mode_counts
    )

    st.subheader(
        "Internship Stipend Distribution"
    )

    st.bar_chart(
        internships[
            [
                "role",
                "stipend"
            ]
        ].set_index("role")
    )

    st.divider()

    st.subheader(
        "Internship Dataset"
    )

    st.dataframe(
        internships,
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.sidebar.divider()

st.sidebar.caption(
    "AI-Based Internship Recommendation System"
)

st.sidebar.caption(
    "B.Tech CSE (AIML) Special Project"
)