import pandas as pd


def load_companies():
    return pd.read_csv("data/companies.csv")


def add_internship(internship, internships):
    new_row = pd.DataFrame([internship])

    updated = pd.concat(
        [internships, new_row],
        ignore_index=True
    )

    return updated