import pandas as pd
import numpy as np

df = pd.read_excel(r"..\data\experimento_Anon.xlsx", sheet_name="amostragem")

threshold = df["Nota do IRA Individual"].median()

df["Faixa IRA"] = np.where(df["Nota do IRA Individual"] >= threshold, "Alto", "Baixo")

high = df[df["Faixa IRA"] == "Alto"].sample(frac=1, random_state=42).reset_index(drop=True)
low = df[df["Faixa IRA"] == "Baixo"].sample(frac=1, random_state=42).reset_index(drop=True)

def divide_groups(sub_df):
    half = len(sub_df) // 2
    groups = ["Controle"] * half + ["Experimental"] * (len(sub_df) - half)
    np.random.shuffle(groups)
    sub_df["Grupo"] = groups
    return sub_df

high = divide_groups(high)
low = divide_groups(low)

final_df = pd.concat([high, low], ignore_index=True)

final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)

final_df.to_excel(r"..\data\final_classification.xlsx", index=False)
