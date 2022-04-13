# importação da ferramenta de conexão com o MongoDB
from pymongo import MongoClient



def create_collection(coll_name):
    # cria a conexão com o mongo
    connection = MongoClient("localhost", 27017)
    # conecta no banco 'topicos'
    db = connection['topicos']
    result = db.create_collection(coll_name, validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['name', 'cpf', 'rg'],
            'properties': {
                'name': {
                    'bsonType': 'string',
                    'description': 'Nome do instrutor'
                },
                'cpf': {
                    'bsonType': 'string',
                    'description': 'CPF do instrutor'
                },
                'rg': {
                    'bsonType': 'string',
                    'description': 'RG do instrutor'
                }
            }
        }
    })

    print(result)


if __name__ == '__main__':
    create_collection('teacher')