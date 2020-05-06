import random

min = 1
max = 6

jogar_denovo = 'Sim'

while jogar_denovo == 'Sim' or jogar_denovo == 's':
    print('Jogando os dados...')
    print('Os valores são')
    print(random.randint(min,max))
    print(random.randint(min,max))

    jogar_denovo = input("Jogar os dados novamente?")
