import pandas as pd


def load_internships():
    return pd.read_csv("data/internships.csv")


def load_students():
    return pd.read_csv("data/students.csv")