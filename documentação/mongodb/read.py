from datetime import datetime
# importação da ferramenta de conexão com o MongoDB
from pymongo import MongoClient, ASCENDING

# cria a conexão com o mongo
connection = MongoClient("localhost", 27017)
# conecta no banco 'topicos'
db = connection['topicos']
# escolhe a coleção 'teacher'
collection = db['teacher']

print(datetime.now())
# procura na coleção escolhida
# ordena por ordem alfabética
# limita a 10 documentos
res = collection.find({
    "name": {
        "$regex": '^Ana'
    }
}).sort([("name",
          ASCENDING)]).limit(10)
print(datetime.now())

print(list(res))
