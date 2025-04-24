import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result = animals[animals["weight"] > 100]
    find = result.sort_values(by="weight", ascending=False)
    return find[["name"]]