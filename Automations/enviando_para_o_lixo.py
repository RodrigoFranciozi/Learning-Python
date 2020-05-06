import send2trash

baconFile = open('bacon.txt', 'a') # cria o arquivo
baconFile.write('Bacon is not a vegetable.')

#fecha o arquivo, caso o mesmo esteja aberto
baconFile.close()

#envia para a lixeira
send2trash.send2trash('bacon.txt')