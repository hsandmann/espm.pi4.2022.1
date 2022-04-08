import db

pessoas = db.listPessoas()
for p in pessoas:
    print(p.id, p.nome, p.email)

p1 = db.Pessoa(None, 'Humberto', 'humberto@espm.br')
db.insertPessoa(p1)
print(f'{p1.nome} foi inserido')

pessoas = db.listPessoas()
for p in pessoas:
    print(p.id, p.nome, p.email)

print(db.findPessoa(5).nome)
