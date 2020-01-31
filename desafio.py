import requests
import json
import hashlib

f = open('answer.json', 'w+')

req = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/'
                   'generate-data?token=96912ca70fb8769ed3e504a21425e3c382d53604')
r = req.json()

palavra = r['cifrado'].lower()
numero = r['numero_casas']

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decifrado = ''
len_list = len(alfabeto) - 1


for caracter in palavra:
    if caracter.isalpha():
        index = alfabeto.index(caracter)
        index_dec = index - numero
        if len_list >= index_dec >= 0:
            decifrado += alfabeto[index_dec]
        else:
            real_index = len_list + index_dec + 1
            decifrado += alfabeto[real_index]
    else:
        decifrado += caracter

r['decifrado'] = decifrado

resumo = hashlib.sha1(decifrado.encode(encoding='utf-8')).hexdigest()

r['resumo_criptografico'] = resumo

json.dump(r, f)
