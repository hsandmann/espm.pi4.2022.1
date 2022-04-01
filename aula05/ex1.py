alunos = {
    'joao': {
        'ra': 1234,
        'notas': {
            'parcial': 7,
            'final': 3
        }
    },
    'elton': {
        'ra': 6925,
        'notas': {
            'parcial': 8,
            'final': 6
        }
    }
}

print('---------')
print(alunos['elton']['notas'])
print('---------')
for k, dados in alunos.items():
    for dadopessoal, valores in dados.items():
        print(dadopessoal, valores)