def dominator(arr):
    if len(arr) == 1:
        return arr[0]
    for a in arr:
        if a == 0:
            return
    diccionario = {}
    diferente = 0
    for a in arr:
        if a != diferente:
            diccionario[a] = 0
            diferente = a
    for a in diccionario:
        diccionario[a] = arr.count(a)
    dominador = 0    
    for a in diccionario:
        if diccionario[a] > dominador:
            dominador = diccionario[a]
            index = a
    repeticion = False        
    for a in diccionario:
        if index == a:
            repeticion = True
        elif diccionario[index] == diccionario[a]:
            return -1
    not1 = 1    
    if len(arr) > 2:
        for a in diccionario:
            if diccionario[a]>not1:
                not1 = diccionario[a]
        if not1 == 1:
            return -1
        elif diccionario[index] > (len(arr)/2):
            return index
        else:
            return -1            




      
contador = [1,2,2,4,5,2,3,4,4,4,4,5,6,7,4,2,12,1,1,1]
print(contador.count(2))        
valor = dominator([1,2,2,4,5,2,3,4,4,4,4,5,6,7,4,2,12,1,1,1])
print(valor)














