import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna()

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(students)[students['name'].notnull()]

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.name.notnull()]