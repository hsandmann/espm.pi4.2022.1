
# Vamos utilizar o pacote requests para fazer requisições HTTP:
# https://docs.python-requests.org/en/master/
#
# Para isso, ele precisa ser instalado via pip (de preferência com o VS Code fechado):
# python -m pip install requests
import requests

headers={

}
resultado = requests.get("https://finance.yahoo.com/quote/TASA4.SA/history?p=TASA4.SA")
# Imprime algumas informações simples da resposta
#print(resultado.status_code)
#print(resultado.headers['content-type'])
# Imprime a string pura da resposta
text = resultado.text
print(text)


