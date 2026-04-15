# Importar as libs que serão utilizadas
import random
import pandas as pd
from faker import Faker

# Configurando a lib Faker
fake=Faker('pt_BR')


# Lero o excel
df_excel = pd.read_excel("base_dados.xlsx")

# Mostrar os CPFs duplicados
print('\nCPFs duplicados:')
print(df_excel["cpf"].duplicated().sum())

# Mostrar quantos funcionarios por setor
print('\nFuncionários por setor:')
print(df_excel["setor"].value_counts())

# Mostrar a media salarial
print('\nMédia salarial:')
print(df_excel["salario"].mean())

# Mostrar os primeiros funcionarios do TI
print('\nFuncionários do TI:')
print(df_excel[df_excel["setor"] == "TI"].head())