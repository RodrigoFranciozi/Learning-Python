import sys
import random

ans = True

while ans:
    pergunta = input("Pergunte algo para Magic8Ball: (Pressione enter para sair) ")
    resposta = random.randint(1,8)

    if pergunta == '':
        sys.exit()

    elif resposta == 1:
        print ('Com Certeza')

    elif resposta == 2:
        print('Perspectiva Boa')
    
    elif resposta == 3:
        print('Você pode contar com ele')
    
    elif resposta == 4:
        print('Pergunte novamente mais tarde')
    
    elif resposta == 5:
        print('Concentre-se e pergunte novamente')
    
    elif resposta == 6:
        print('Resposta nebuloza, tente denovo')
    
    elif resposta == 7:
        print('Minha resposta é não')
    
    elif resposta == 8:
        print('Minhas fontes dizer que não')

    