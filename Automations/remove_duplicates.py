def remover_duplicatas(lista):
    lista2 = []
    if lista:
        for item in lista:
            if item not in lista2:
                lista2.append(item)
    else:
        return lista
    return lista2
print (remover_duplicatas([1,2,3,3,]))

#insere uma lista e remove todos os arquivos duplicados. 