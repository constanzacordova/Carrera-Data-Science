import sys

#Leer clave-valor pero ordenado por clave
feed_mapper_output = sys.stdin

previous_plan = None
total_positive_count = 0
total_total_count = 0


for line_answer in feed_mapper_output:
    plan, positive, total, mean = line_answer.split('\t')
    

    if float(mean)>= 0.6:

        # Revisar si cambio de palabra
        if plan != previous_plan:
            
            # Condicion inicial
            if previous_plan is not None:
                # Imprimo resultado
                print(f"{previous_plan}\t{str(total_positive_count/total_total_count)}")

            previous_plan = plan
            total_positive_count = 0
            total_total_count = 0
            
        
        total_positive_count += int(positive)
        total_total_count += int(total)
print(f"{previous_plan}\t{str(total_positive_count/total_total_count)}")