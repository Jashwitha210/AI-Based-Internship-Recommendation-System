import pandas as pd


def load_quizzes():
    return pd.read_csv("data/quizzes.csv")


def get_quiz_by_topic(quizzes, topic):
    return quizzes[
        quizzes["topic"].str.lower() == topic.lower()
    ]


def calculate_quiz_score(questions, answers):
    if not questions:
        return 0

    correct = 0

    for question, answer in zip(questions, answers):
        if question["answer"].lower() == answer.lower():
            correct += 1

    return round((correct / len(questions)) * 100, 2)