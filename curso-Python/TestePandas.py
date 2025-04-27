dados = {"Estado": ["SP", "RJ", "MG", "BA", "PR"],
        "População": [45.9, 17.4, 21.0, 14.8, 11.1],
        "Taxa de emprego": [9.5, 11.2, 10.1, 12.3, 8.7],}

#print(dados)

from pandas import DataFrame

df = DataFrame(dados)

print(df.head())

#print(type(df))

df2 = DataFrame(dados,
                columns=["Estado", "População", "Taxa de emprego", "Ano"],
                index=["SP", "RJ", "MG", "BA", "PR"])

df2["Ano"] = [2023, 2023, 2023, 2023, 2023]

print(df2.head())