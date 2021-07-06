def letra_x(n):

    linea = ""
    if n%2 == 0:
        n += 1

    for i in range(n):
        limite_sup = int((n-1)/2)
        centro = int((n-1)/2)
        limite_inf = int(centro + 1)
        
        if i in range(limite_sup):
            extremos = i
            espacios_usados = 2*extremos + 2
            centro = n - espacios_usados
            linea += " "*extremos + "*" + " "*centro + "*" + "\n"

        elif i == centro:
            extremos = i
            linea += " "*extremos + "*"+"\n"

        elif i in range(limite_inf, n):
            extremos = n-i-1
            espacios_usados = 2*extremos + 2
            centro = n - espacios_usados
            linea += " "*extremos + "*" + " "*centro + "*" + "\n"
    return linea



print(letra_x(9))