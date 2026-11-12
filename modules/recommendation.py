import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from modules.skill_matching import calculate_skill_match


def calculate_text_similarity(student_text, internship_text):
    """
    Calculate TF-IDF cosine similarity between
    student preferences/skills and internship requirements.
    """

    student_text = str(student_text)
    internship_text = str(internship_text)

    if not student_text.strip() or not internship_text.strip():
        return 0.0

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(
        [student_text, internship_text]
    )

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def calculate_domain_match(student_domain, internship_domain):
    """
    Compare student's preferred domain with internship domain.
    """

    if not student_domain or not internship_domain:
        return 0

    if str(student_domain).strip().lower() == \
            str(internship_domain).strip().lower():
        return 100

    return 0


def calculate_location_match(student_location, internship_location):
    """
    Compare student's preferred location with internship location.
    """

    student_location = str(student_location).strip().lower()
    internship_location = str(internship_location).strip().lower()

    if student_location == internship_location:
        return 100

    if internship_location == "remote":
        return 100

    return 0


def calculate_work_mode_match(student_mode, internship_mode):
    """
    Compare student's preferred work mode with internship work mode.
    """

    student_mode = str(student_mode).strip().lower()
    internship_mode = str(internship_mode).strip().lower()

    if student_mode == internship_mode:
        return 100

    return 0


def calculate_compensation_match(
    expected_stipend,
    internship_stipend
):
    """
    Compare student's expected stipend with
    internship stipend.
    """

    try:
        expected = float(expected_stipend)
        offered = float(internship_stipend)

        if expected <= 0:
            return 100

        if offered >= expected:
            return 100

        difference = expected - offered

        score = max(
            0,
            100 - ((difference / expected) * 100)
        )

        return round(score, 2)

    except (ValueError, TypeError):
        return 50


def calculate_suitability(cgpa):
    """
    Calculate student suitability score from CGPA.
    """

    try:
        cgpa = float(cgpa)

        score = (cgpa / 10) * 100

        return round(
            min(score, 100),
            2
        )

    except (ValueError, TypeError):
        return 50


def calculate_recommendation_score(
    student,
    internship
):
    """
    Calculate the complete hybrid recommendation score.

    Weights:
    TF-IDF + Cosine Similarity = 35%
    Skill Matching             = 25%
    Career/Domain Matching     = 15%
    Location Matching          = 10%
    Compensation Matching      = 5%
    Student Suitability        = 5%
    Employer Rating            = 5%
    """

    # -----------------------------------------
    # 1. TF-IDF + Cosine Similarity - 35%
    # -----------------------------------------

    student_text = " ".join([
        str(student.get("skills", "")),
        str(student.get("preferred_domain", "")),
        str(student.get("preferred_work_mode", ""))
    ])

    internship_text = " ".join([
        str(internship.get("required_skills", "")),
        str(internship.get("domain", "")),
        str(internship.get("work_mode", ""))
    ])

    text_score = calculate_text_similarity(
        student_text,
        internship_text
    )

    # -----------------------------------------
    # 2. Skill Matching - 25%
    # -----------------------------------------

    skill_score, matched_skills, missing_skills = \
        calculate_skill_match(
            student.get("skills", ""),
            internship.get("required_skills", "")
        )

    # -----------------------------------------
    # 3. Career/Domain Matching - 15%
    # -----------------------------------------

    domain_score = calculate_domain_match(
        student.get("preferred_domain", ""),
        internship.get("domain", "")
    )

    # -----------------------------------------
    # 4. Location Matching - 10%
    # -----------------------------------------

    location_score = calculate_location_match(
        student.get("preferred_location", ""),
        internship.get("location", "")
    )

    # -----------------------------------------
    # 5. Compensation Matching - 5%
    # -----------------------------------------

    compensation_score = calculate_compensation_match(
        student.get("expected_stipend", 0),
        internship.get("stipend", 0)
    )

    # -----------------------------------------
    # 6. Student Suitability - 5%
    # -----------------------------------------

    suitability_score = calculate_suitability(
        student.get("cgpa", 0)
    )

    # -----------------------------------------
    # 7. Employer Rating - 5%
    # -----------------------------------------

    try:
        employer_rating = float(
            internship.get("employer_rating", 3)
        )

        employer_score = min(
            (employer_rating / 5) * 100,
            100
        )

    except (ValueError, TypeError):
        employer_score = 60

    # -----------------------------------------
    # Final Hybrid Score
    # -----------------------------------------

    final_score = (
        (text_score * 0.35)
        + (skill_score * 0.25)
        + (domain_score * 0.15)
        + (location_score * 0.10)
        + (compensation_score * 0.05)
        + (suitability_score * 0.05)
        + (employer_score * 0.05)
    )

    return {
        "score": round(final_score, 2),
        "text_similarity": text_score,
        "skill_match": skill_score,
        "domain_match": domain_score,
        "location_match": location_score,
        "compensation_match": compensation_score,
        "suitability": suitability_score,
        "employer_rating": employer_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }


def recommend_internships(student, internships):
    """
    Generate recommendations for one student.
    """

    recommendations = []

    for _, internship in internships.iterrows():

        result = calculate_recommendation_score(
            student,
            internship
        )

        recommendation = internship.to_dict()

        recommendation.update(result)

        recommendations.append(
            recommendation
        )

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations