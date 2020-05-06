import requests
import re

print('Tentaremos abrir esta URL para pegar o IP')

url = 'http://checkip.dyndns.org'

print(url)

requisição = requests.get(url)

limpar = requisição.text.split(': ', 1) [1]
seuIP = limpar.split('</body><html>' ,1) [0]

print('Seu endereço ip é:', seuIP)
