
hora  = int(input('Digite uma hora: '))

if hora < 0 or hora > 24:
    print('Hora invalida')
elif hora < 12:
    print('Bom dia!')
elif hora < 18:
    print('Boa tarde!')
else:
    print('Boa noite!')
    
print('Fim')
