from datetime import datetime
# importação da ferramenta de conexão com o MongoDB
from pymongo import MongoClient

# cria a conexão com o mongo
connection = MongoClient("localhost", 27017)
# conecta no banco 'topicos'
db = connection['topicos']
# escolhe a coleção 'teacher'
collection = db['teacher']

print(datetime.now())
# apaga os dados encontrados com o filtro, na coleção escolhida
res = collection.delete_many({"name": {"$regex": '^João'}})
print(datetime.now())
print(str(res.deleted_count) + " arquivos deletados")