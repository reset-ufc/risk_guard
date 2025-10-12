import pandas as pd
import numpy as np

# 1. Ler o arquivo CSV
df = pd.read_excel(r"..\data\experimento.xlsx", sheet_name="amostragem")

# 2. Calcular a mediana (ou Q3 se quiser mudar)
threshold = df["Nota do IRA Individual"].median()

# 3. Classificar IRA Alto ou Baixo
df["Faixa IRA"] = np.where(df["Nota do IRA Individual"] >= threshold, "Alto", "Baixo")

# 4. Divisão balanceada em Controle e Experimental
# Separar Alto e Baixo
alto = df[df["Faixa IRA"] == "Alto"].sample(frac=1, random_state=42).reset_index(drop=True)
baixo = df[df["Faixa IRA"] == "Baixo"].sample(frac=1, random_state=42).reset_index(drop=True)

# Função para dividir metade em cada grupo
def dividir_grupos(sub_df):
    metade = len(sub_df) // 2
    grupos = ["Controle"] * metade + ["Experimental"] * (len(sub_df) - metade)
    np.random.shuffle(grupos)
    sub_df["Grupo"] = grupos
    return sub_df

# 5. Aplicar a divisão balanceada
alto = dividir_grupos(alto)
baixo = dividir_grupos(baixo)

# 6. Concatenar de volta
final_df = pd.concat([alto, baixo], ignore_index=True)

# 7. Embaralhar linhas para não ficar agrupado
final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)

# 8. Salvar resultado final
final_df.to_excel(r"..\data\classificacao_final.xlsx", index=False)

print("✅ Classificação concluída e salva em classificacao_final.xlsx")
