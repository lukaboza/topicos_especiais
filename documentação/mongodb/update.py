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
# procura na coleção escolhida pelo filtro
# atualiza o nome dos documentos encontrados
res = collection.update_many(
    {"name": {
        "$regex": '^Eloah'
    }},
    {"$set": {
        "name": "Elias"
    }}
)
print(datetime.now())

print(str(res.matched_count) + " arquivos encontrados")
print(str(res.modified_count) + " arquivos modificados")
