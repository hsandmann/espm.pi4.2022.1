
msg = ''
while msg != 'exit':
    msg = input('> ').strip().lower()
    if len(msg) == 0:
        pass
    elif msg == 'help':
        print('ESPM Terminal')
    elif msg == 'exit':
        pass
    elif msg == 'surian':
        print('Gente boa de dados!')
    else:
        print('Comando invalido')

print('bye bye')

