# Fazer uma função que calcula da distância
# euclidiana entre dois pontos. Para isso,
# recebe, nessa ordem: x1, y1, x2, y2.
import conversoes

km = float(input('km: '))
mi = conversoes.km2mi(km)
print('{:.2f} km -> {:.2f} mi'.format(km, mi))

