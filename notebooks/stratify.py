from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
ROOT = Path(__file__).resolve().parent.parent
IRA = "Individual academic performance index (IRA)"

rng = np.random.default_rng(SEED)

df = pd.read_csv(ROOT / "data_en" / "experiment_Anon.csv")

threshold = df[IRA].median()

df["IRA band"] = np.where(df[IRA] >= threshold, "High", "Low")

def divide_groups(sub_df):
    sub_df = sub_df.sample(frac=1, random_state=rng).reset_index(drop=True)
    half = len(sub_df) // 2
    groups = np.array(["Control"] * half + ["Experimental"] * (len(sub_df) - half))
    rng.shuffle(groups)
    sub_df["Group"] = groups
    return sub_df

high = divide_groups(df[df["IRA band"] == "High"])
low = divide_groups(df[df["IRA band"] == "Low"])

final_df = pd.concat([high, low], ignore_index=True)

final_df = final_df.sample(frac=1, random_state=rng).reset_index(drop=True)

final_df.to_csv(ROOT / "notebooks" / "stratified_example.csv", index=False)
