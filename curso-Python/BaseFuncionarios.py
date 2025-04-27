import pandas as pd

# Carregar a base de dados
df = pd.read_excel(r"C:\Users\israe\Downloads\BaseFuncionarios.xlsx")

# Filtrar os dados conforme os critérios:
# - Data de contratação antes de 31/12/2008
# - Sexo feminino ("F")
# - Estado civil casado ("C")
filtro = (
    (pd.to_datetime(df['Data de Contratacao']) < pd.to_datetime('2008-12-31')) &
    (df['Sexo'] == 'F') &
    (df['Estado Civil'] == 'C')
)

# Aplicar o filtro
funcionarias_filtradas = df[filtro]

# Calcular a soma dos impostos
soma_impostos = funcionarias_filtradas['Impostos'].sum()

# Listar os nomes das funcionárias
nomes_funcionarias = funcionarias_filtradas['Nome Completo'].tolist()

# Exibir os resultados
print(f"Soma total dos impostos: R$ {soma_impostos:.2f}")
print("\nLista de funcionárias que atendem aos critérios:")
for nome in nomes_funcionarias:
    print(nome)

# Exibir o número de funcionárias encontradas
print(f"\nTotal de funcionárias encontradas: {len(nomes_funcionarias)}")