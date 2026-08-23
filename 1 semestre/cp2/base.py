# Importar as libs que serão utilizadas
import random
import pandas as pd
from faker import Faker

# Configurando a lib Faker
fake=Faker('pt_BR')

# Adicionando os dados em listas que serão utilizados no projeto
nomes_masculinos = ["Rafael", "Carlos", "Marcos", "Lucas", "Gabriel", "Pedro",
"João", "Bruno", "Felipe", "Gustavo", "Diego", "Thiago",
"Leonardo", "Rodrigo", "Matheus"]
nomes_femininos = ["Ana", "Julia", "Fernanda", "Beatriz", "Mariana", "Larissa",
"Camila", "Amanda", "Patricia", "Renata", "Juliana", "Bianca",
"Vanessa", "Aline", "Carolina"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira",
"Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes",
"Soares", "Fernandes", "Vieira", "Barbosa", "Rocha", "Dias", "Monteiro", "Mendes",
"Freitas", "Cardoso", "Teixeira", "Correia", "Castro", "Araujo", "Nascimento", "Moreira",
"Barros", "Pinto", "Machado", "Batista", "Campos", "Andrade", "Borges", "Moura",
"Rezende", "Cavalcante", "Farias", "Peixoto", "Queiroz", "Tavares", "Duarte", "Medeiros",
"Aguiar", "Coelho"]
setores = ["TI", "RH", "Financeiro", "Marketing", "Vendas", "Logística"]
cargos = ["Analista", "Assistente", "Gerente", "Supervisor", "Estagiário"]
turnos = ["Manhã", "Tarde", "Noite"]
promovido=["Sim", "Não"]
nivel=["Junior", "Pleno", "Senior"]
carga=[20, 30, 40, 44]

# Criando as listas e sets para adicionar no excel
dados=[]
nomes_usados=set()
cpfs_usados=set()

# Enquanto o tamanho da lista dados for menor que 150
while len(dados)<150:
    # Sorteia o nome e o sobrenome
    # escolher gênero + nome coerente
    if random.choice([True, False]):
        nome = random.choice(nomes_masculinos)
        genero = "Masculino"
    else:
        nome = random.choice(nomes_femininos)
        genero = "Feminino"
    sobrenome=random.choice(sobrenomes)
    # Cria nome completo (nome+sobrenome)
    nome_completo=f'{nome} {sobrenome}'
    # Se o nome completo nao estiver no set nomes_usados
    if nome_completo not in nomes_usados:
        nomes_usados.add(nome_completo)
    
    # Cria um cpf
    cpf=fake.cpf()
    # Se o cpf criado não estiver no set de cpfs_usados
    if cpf not in cpfs_usados:
        cpfs_usados.add(cpf)
        
    # Sorteia uma idade entre 18 e 60 anos
    idade=random.randint(18,60)
    
    # Cria a data de nascimento baseado na idade, usando fake
    data_nascimento=fake.date_of_birth(minimum_age=idade, maximum_age=idade)
    
    # Cria o registro(linhas)
    registro={
        'id_funcionario':len(dados)+1,
        'cpf':cpf,
        'nome':nome,
        'sobrenome':sobrenome,
        'genero':genero,
        'idade':idade,
        'data_nascimento':data_nascimento,

        'rua':fake.street_name(),
        'numero':fake.building_number(),
        'bairro':fake.bairro(),
        'cidade':fake.city(),
        'estado':fake.state(),
        'cep':fake.postcode(),
        
        'setor':random.choice(setores),
        'cargo':random.choice(cargos),
        'salario':random.randint(1500, 12000),
        'tempo_empresa (anos)':random.randint(1, 30),
        'turno':random.choice(turnos),
        'avaliacao_desempenho':random.randint(1, 10),
        'faltas':random.randint(0, 15),
        'bonus':random.randint(0, 3000),
        'promovido':random.choice(promovido),
        'carga_horaria':random.choice(carga),
        'nivel':random.choice(nivel)
    }
    
    # Adiciona os registros na tabela dados
    dados.append(registro)
    

# Cria o DataFrame
df=pd.DataFrame(dados)

# Salva o dataframe no excel
# OBS: index=False quer dizer que a tabela não tera um id do Dataframe
df.to_excel("base_dados.xlsx", index=False)

# ----------Validação dos dados----------

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