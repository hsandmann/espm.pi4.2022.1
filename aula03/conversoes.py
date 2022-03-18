import math

def km2mi(km):
    return 0.621371 * km

def mi2km(mi):
    return mi / 0.621371

# Faça uma função que retorna quantas raízes tem uma
# equação de 2o grau
# delta > 0 -> 2 raízes
# delta == 0 -> 1 raiz
# delta < 0 -> 0 raiz
def qtd_raizes(a, b, c):
    delta = b**2 -4*a*c
    return (2 if delta > 0 else (1 if delta == 0 else 0))


# Faça uma funcão que entra ano, mes e dia, retorna se a data é válida,
# considerar ano bissexto, segundo:
# https://docs.microsoft.com/pt-br/office/troubleshoot/excel/determine-a-leap-year