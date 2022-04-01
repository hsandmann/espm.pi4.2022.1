import requests

resultado = requests.get("https://pt.aliexpress.com/")
# Imprime algumas informações simples da resposta
#print(resultado.status_code)
#print(resultado.headers['content-type'])
# Imprime a string pura da resposta
text = resultado.text

print(text.find('Moda Feminina'))

