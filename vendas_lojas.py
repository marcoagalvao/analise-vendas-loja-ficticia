import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de estilo
sns.set_theme(style="whitegrid")

# Carregar o conjunto de dados com o delimitador correto
df = pd.read_csv("dados_vendas_lojas.csv", delimiter=";")

# Converter a coluna de data para o formato datetime
df["Data"] = pd.to_datetime(df["Data"])

# Remover duplicatas
df = df.drop_duplicates()

#----------------------------------------------------------------

# 1. Vendas Totais por Mês
vendas_mensais = df.resample("M", on="Data")["Valor_Total"].sum()

# Gráfico de Vendas Totais por Mês
plt.figure(figsize=(12, 6))
sns.lineplot(x=vendas_mensais.index, y=vendas_mensais.values, marker="o", color="royalblue")
plt.title("Vendas Totais por Mês", fontsize=16)
plt.xlabel("Mês", fontsize=14)
plt.ylabel("Valor Total (R$)", fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------

# 2. Vendas Mensais por Categoria
vendas_mensais_categoria = df.groupby([df["Data"].dt.to_period("M"), "Categoria"])["Valor_Total"].sum().unstack()

# Gráfico de Vendas Mensais por Categoria (Barras Agrupadas)
plt.figure(figsize=(12, 6))
sns.barplot(data=vendas_mensais_categoria.reset_index().melt(id_vars="Data"), 
            x="Data", y="value", hue="Categoria", palette="Set2")
plt.title("Vendas Mensais por Categoria (Barras Agrupadas)", fontsize=16)
plt.xlabel("Mês", fontsize=14)
plt.ylabel("Valor Total (R$)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Categoria")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------

# 3. Vendas Mensais por Região
vendas_mensais_regiao = df.groupby([df["Data"].dt.to_period("M"), "Regiao"])["Valor_Total"].sum().unstack()

# Gráfico de Vendas Mensais por Região (Barras Agrupadas)
plt.figure(figsize=(12, 6))
sns.barplot(data=vendas_mensais_regiao.reset_index().melt(id_vars="Data"), 
            x="Data", y="value", hue="Regiao", palette="Accent")
plt.title("Vendas Mensais por Região (Barras Agrupadas)", fontsize=16)
plt.xlabel("Mês", fontsize=14)
plt.ylabel("Valor Total (R$)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Região")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------

# 4. Vendas Mensais por Método de Pagamento
vendas_mensais_pagamento = df.groupby([df["Data"].dt.to_period("M"), "Metodo_Pagamento"])["Valor_Total"].sum().unstack()

# Gráfico de Vendas Mensais por Método de Pagamento (Barras Agrupadas)
plt.figure(figsize=(12, 6))
sns.barplot(data=vendas_mensais_pagamento.reset_index().melt(id_vars="Data"), 
            x="Data", y="value", hue="Metodo_Pagamento", palette="Dark2")
plt.title("Vendas Mensais por Método de Pagamento (Barras Agrupadas)", fontsize=16)
plt.xlabel("Mês", fontsize=14)
plt.ylabel("Valor Total (R$)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Método de Pagamento")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------

# Verificar se a categoria "Acessorio" realmente teve a maior queda nas vendas
vendas_mensais_categoria = df.groupby([df["Data"].dt.to_period("M"), "Categoria"])["Valor_Total"].sum().unstack()
variacao_acumulada_categoria = (vendas_mensais_categoria.iloc[-1] - vendas_mensais_categoria.iloc[0]) / vendas_mensais_categoria.iloc[0] * 100
maior_queda_categoria = variacao_acumulada_categoria.idxmin()

# Verificar se a região "Leste" realmente teve a maior queda nas vendas
vendas_mensais_regiao = df.groupby([df["Data"].dt.to_period("M"), "Regiao"])["Valor_Total"].sum().unstack()
variacao_acumulada_regiao = (vendas_mensais_regiao.iloc[-1] - vendas_mensais_regiao.iloc[0]) / vendas_mensais_regiao.iloc[0] * 100
maior_queda_regiao = variacao_acumulada_regiao.idxmin()

# Verificar se o método de pagamento tem relação com a queda
vendas_mensais_pagamento = df.groupby([df["Data"].dt.to_period("M"), "Metodo_Pagamento"])["Valor_Total"].sum().unstack()
correlacao_pagamento = vendas_mensais_pagamento.corr()

# Exibir os resultados
print(f"Categoria com maior queda: {maior_queda_categoria}")
print(f"Região com maior queda: {maior_queda_regiao}")
print("Correlação entre métodos de pagamento:")
print(correlacao_pagamento)
