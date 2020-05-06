#Colocar o nome do usuário
usuário = input('Login:>>')

#Usuários autorizados
usuário1 = 'Janaina'
usuário2 = 'Lérisson'
usuário3 = 'Elaine'
usuário4 = 'Erika'

#Vê se o usuário digitado se encontra ou não na lista
if usuário == (usuário1 or usuário2 or usuário3 or usuário4):
    print ("Acesso garantido")

else:
    print('Acesso Negado')

