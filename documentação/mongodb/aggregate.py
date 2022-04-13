from datetime import datetime
# importação da ferramenta de conexão com o MongoDB
from pymongo import MongoClient
# importa ferramenta de regex
import re

# cria a conexão com o mongo
connection = MongoClient("localhost", 27017)
# conecta no banco 'topicos'
db = connection['topicos']
# escolhe a coleção 'teacher'
collection = db['teacher']

# a operação de aggregate no MongoDB é similar ao JOIN do SQL
# agrupa valores de vários documentos juntos
# realiza operações nos dados agrupados e retorna um resultado
res = collection.aggregate(
    [
        # busca os CPFs com final 00
        {
            '$match': {
                'cpf': {
                    '$regex': re.compile(r"00$")
                }
            }
        },
        # agrupa o resultado da operação anterior
        {
            '$group': {
                # agrupa por gênero
                '_id': '$gender',
                # conta o número de ocorrências
                'count': {
                    '$count': {}
                }
            }
        }
    ]
)
