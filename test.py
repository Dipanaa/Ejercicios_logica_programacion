def numeros(a,b):
    resultado = 0
    multiplos = a
    i = a
    while(i<b):
        print(resultado)
        multiplos = i
        resultado = multiplos + resultado
        i = i + a
    return resultado    


a = numeros(2,9)
print(a,"<---")        