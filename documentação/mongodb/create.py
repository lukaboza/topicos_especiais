from datetime import datetime
# importação da biblioteca para gerar dados aleatórios
from faker import Faker, providers
# importação da ferramenta de conexão com o MongoDB
from pymongo import MongoClient

# cria a conexão com o mongo
connection = MongoClient("localhost", 27017)

# instancia a classe para criar dados aleatórios
# cria dados baseados em portugês do Brasil
fake = Faker('pt_BR')
# adiciona nº de telefones
fake.add_provider(providers.phone_number)
# adiciona endereços
fake.add_provider(providers.address)
# inicia lista para conter os dados a ser inseridos
data = []
for _ in range(10000):
    # popula a lista com os dados de cadastro aleatórios
    data.append(
        {
            "name": fake.name(),
            "rg": fake.rg() + "00",
            "cpf": fake.cpf(),
            "gender": "M",
            "email": fake.company_email(),
            "phone": fake.cellphone_number(),
            "city": fake.city(),
            "address": fake.street_address(),
            "birthday": str(fake.date_of_birth(minimum_age=12)),
            "bound": {
                "association": fake.company(),
                "cnpj": fake.cnpj(),
            }
        }
    )
# conecta no banco 'topicos'. Caso não exista, é criado
db = connection['topicos']
# escolhe a coleção teacher. Caso não exista, é criado
collection = db['teacher']
print(datetime.now())
# insere os dados no banco e coleção previamente escolhidos
# e salva o resutado da inserção na variável
res = collection.insert_many(data)
print(datetime.now())
# verifica se houve êxito na operação
if(res.acknowledged):
    print("Dados inseridos com sucesso")
else:
    print("Falha ao inserir dados")