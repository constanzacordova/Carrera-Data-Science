import  sys

feed_txt = sys.stdin

# para cada linea de cliente que corresponde a la linea del archivo txt
for line_in_txt in feed_txt:

    # separamos los datos de la linea generando una lista. Además se eliminan los saltos de liena 
    data_in_line = line_in_txt.rstrip('\r\n').split(sep= ",")

    # recorremos los datos que contiene la lista de datos de la linea
    # si el dato corresponde a 1 o 0 se ignora, de lo contrario se asume que el dato corresponde a un plan
    for data in data_in_line:
        if data == '1' or data =='0':
            None
        else:
            print(data + '\t1')
