import pandas as pd
import numpy as np
import pickle

#nombre de columnas
colnames = ['deliverer_id', 'delivery_zone', 'monthly_app_usage', 'suscription_type', 'paid_price', 'customer_size', 'menu', 'delay_time']

#leemos dataframe y asignamos nombre a las columnas
df_test_delivery = pd.read_csv('test_delivery_data.csv', header=None, names=colnames)

#Copiamos dataframe original
df_copy = df_test_delivery.copy()

#recodificación vector obetivo
# 1 para demora > promedio
# 0 para demora =< promedio
df_test_delivery.delay_time = np.where(df_test_delivery.delay_time > df_test_delivery.delay_time.mean(), 1, 0)

#buscamos las variables que sean de tipo string 
dict_data_type = dict(df_test_delivery.dtypes)
str_var = []

for colname in dict_data_type:
    if dict_data_type[colname] == 'O':
        str_var.append(colname)

#Recodificamos los atributos de tipo string en K-1 columnas 
df_test_delivery = pd.get_dummies(df_test_delivery, columns= str_var, drop_first=True)

#Definimos vector Objetivo
vector_objetivo = 'delay_time'

#Enlistamos y removemos vector objetivo de la matriz de entrenamiento
colname_x = list(df_test_delivery.columns)
colname_x.remove(vector_objetivo)

#definimos matriz de entrenamiento y vector objetivo
x_matriz = df_test_delivery[colname_x]
y_vector = df_test_delivery[vector_objetivo]

#Cargamos el mejor modelo entrenado
model = pickle.load(open('Bernoulli.pkl', 'rb'))

#Realizamos la predicción
y_hat = model.predict(x_matriz)

#Cargamos el modelo
model = pickle.load(open('Bernoulli.pkl', 'rb'))

#Realizamos la predicción de que el pedido se tarde por sobre la media
y_hat = model.predict(x_matriz)

#agregamos la predicción al dataframe original
df_copy['y_hat'] = y_hat

#se define funcion para determinar la probabilidad 
def proba_retraso_alto(categoria):

    print(f'Tabla de probabilidad que un pedido se retrase para cada {categoria}\n')

    values = df_copy[categoria].unique()
    values.sort()
    
    for value in values:
        y_hat_value = df_copy[df_copy[categoria]== value]['y_hat']
        proba =  round(sum(y_hat_value)/len(y_hat_value),2)
        print(value,'\t\t',proba)
        
    print('\n')
    
#Determinamos la probabilidad por categoria
proba_retraso_alto('delivery_zone')
proba_retraso_alto('deliverer_id')
proba_retraso_alto('menu')
proba_retraso_alto('suscription_type')