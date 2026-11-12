import pandas as pd


def load_courses():
    return pd.read_csv("data/courses.csv")


def get_learning_recommendations(missing_skills, courses):
    recommendations = []

    missing = {
        skill.strip().lower()
        for skill in missing_skills
        if skill.strip()
    }

    for _, course in courses.iterrows():
        course_skills = {
            skill.strip().lower()
            for skill in str(course["skills"]).split(",")
        }

        if missing.intersection(course_skills):
            recommendations.append(course.to_dict())

    return recommendations