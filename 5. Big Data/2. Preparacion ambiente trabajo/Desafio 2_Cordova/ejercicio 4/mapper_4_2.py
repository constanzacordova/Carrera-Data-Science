import  sys

feed_document = sys.stdin
lista_answer = []
positive = 0
negative = 0
plan = ''

#leemos las lineas del archivo
for line_in_document in feed_document:
 
    # removemos los saltos de linea y separamos las palabras
    words_in_line = line_in_document.rstrip('\r\n').split(sep= ",")

    #recorremos las palabras de la linea para encontrar el plan del cliente
    for word in words_in_line:

        # si es una respuesta a la encuesta la almacenamos en una lista
        if word == '1' or word =='0':
            lista_answer.append(int(word))
        # de lo contrario corresponde al plan
        else:
            plan = word
    
    #recorremos la lista de respuestas por cliente
    #si la respuesta es 1 se contabiliza como positivo, en cambio se asume que es igual a 0 y se contabiliza en negativo
    for answer in lista_answer:
        if answer == 1:
            positive += 1

        else:
            negative += 1

    #imprimimos el plan del cliente y el total de repsuestas positivas y total de respuestas negativas
    #luego reseateamos los contadores
    print(plan + f'\t{positive}' + f'\t{negative}')
    lista_answer = []
    positive = 0
    negative = 0