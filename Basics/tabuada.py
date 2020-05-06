import time
num = int(input('Digite o número que deseja saber a tabuada:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num,c,num*c))

time.sleep(1500)
