import requests

def getData():
    text = ''
    return text

def transform(text):
    d = {}
    index = 0
    while index >= 0:
        index = text.find('cate-name')
        if index >= 0:
            key = text[index:index+100]
            value = 'conteudo'
            d[key] = value
    return d