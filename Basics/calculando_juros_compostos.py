#Juros Anual Estimado Para Investimento

print('Quantos anos você pretende salvar?')
anos = int(input('Digite o número de anos: '))

print('Quanto de dinheiro se encontra atualmente na sua conta?')
principal = float(input('Coloque a quantidade de dinheiro que se encontra na sua conta: '))

print('Qual o valor que você planeja investir mensalmente?')
investimento_mensal = float(input('Coloque a quantidade mensal: '))

print('Qual você estima que será o valor dos juros desse investimento por ano?')
juros = float(input('Coloque o valor do juros em decimal (10% = 0.1): '))

print(' ')

investimento_mensal = investimento_mensal * 12
quantidade_final = 0

for i in range(0, anos):
    if quantidade_final == 0:
        quantidade_final = principal
        
    quantidade_final = (quantidade_final + investimento_mensal) * (1 + juros)
    
print('Esta será a quantidade de dinheiro que estará na sua conta após {} anos: '.format(anos) + str(quantidade_final))
