import sys

#Leer clave-valor pero ordenado por clave
feed_mapper_output = sys.stdin

previous_word = None
total_word_count = 0

for line_ocurrence in feed_mapper_output:
    word, ocurrence = line_ocurrence.split('\t')
    
    
    # Revisar si cambio de palabra
    if word != previous_word:
        
        # Condicion inicial
        if previous_word is not None:
            # Imprimo resultado
            print(f"{previous_word}\t{str(total_word_count)}")

        previous_word = word
        total_word_count = 0
        
    
    total_word_count += int(ocurrence)
   

