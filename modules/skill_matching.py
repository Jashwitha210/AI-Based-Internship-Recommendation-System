def clean_skills(skills):
    if not skills:
        return []

    return [
        skill.strip().lower()
        for skill in str(skills).split(",")
        if skill.strip()
    ]


def calculate_skill_match(student_skills, required_skills):
    student = set(clean_skills(student_skills))
    required = set(clean_skills(required_skills))

    if not required:
        return 0, [], []

    matched = sorted(student.intersection(required))
    missing = sorted(required - student)

    score = (len(matched) / len(required)) * 100

    return round(score, 2), matched, missing