
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Como criar uma comunicação com o banco de dados:
# https://docs.sqlalchemy.org/en/14/core/engines.html
#
# Detalhes específicos ao MySQL
# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector
#
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
engine = create_engine('mysql+mysqlconnector://root:123321My@localhost:3306/agenda')

class Pessoa:

    id = None
    nome = None
    email = None

    def __init__(self, id, nome, email) -> None:
        self.id = id
        self.nome = nome
        self.email = email

def listPessoas(ordem='nome'):
    sessao = Session(engine)
    pessoas = sessao.execute(text(f'SELECT id, nome, email FROM pessoa ORDER BY {ordem}'))

    # Como cada registro retornado é uma tupla ordenada, é possível
    # utilizar a forma de enumeração de tuplas:
    l = []
    for (id, nome, email) in pessoas:
        p = Pessoa(id, nome, email)
        l.append(p)
    return l

def findPessoa(id):
    parametros = {
        'id': id
    }
    sessao = Session(engine)
    pessoa = sessao.execute(text(f'SELECT id, nome, email FROM pessoa WHERE id=:id'), parametros).first()
    if pessoa != None:
        return Pessoa(pessoa.id, pessoa.nome, pessoa.email)
    else:
        return None

def insertPessoa(pessoa):
    sessao = Session(engine)
    sessao.begin()
    p = {
        'nome': pessoa.nome,
        'email': pessoa.email
    }
    sessao.execute(text('INSERT INTO pessoa (nome, email) VALUES (:nome, :email)'), p)
    sessao.commit()





class Coin:

    id = None
    nome = None
    ticker = None
    price = None

    def __init__(self, id, nome, ticker, price) -> None:
        self.id = id
        self.nome = nome
        self.ticker = ticker
        self.price = price

def insertCoin(dic_coin):
    sessao = Session(engine)
    sessao.begin()
    sessao.execute(text('INSERT INTO coin (name, ticker, price) VALUES (:name, :ticker, :price)'), dic_coin)
    sessao.commit()
