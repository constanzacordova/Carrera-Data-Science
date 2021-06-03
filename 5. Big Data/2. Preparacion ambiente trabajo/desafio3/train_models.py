import pandas as pd
import numpy as np
import pickle
import warnings

warnings.filterwarnings('ignore')


from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB


#nombre de columnas
colnames = ['deliverer_id', 'delivery_zone', 'monthly_app_usage', 'suscription_type', 'paid_price', 'customer_size', 'menu', 'delay_time']

#leemos dataframe y asignamos nombre a las columnas
df_train_delivery = pd.read_csv('train_delivery_data.csv', header=None, names=colnames)

#recodificación vector obetivo
# 1 para demora > promedio
# 0 para demora =< promedio
df_train_delivery.delay_time = np.where(df_train_delivery.delay_time > df_train_delivery.delay_time.mean(), 1, 0)

#buscamos las variables que sean de tipo string 
dict_data_type = dict(df_train_delivery.dtypes)
str_var = []

for colname in dict_data_type:
    if dict_data_type[colname] == 'O':
        str_var.append(colname)

#Recodificamos los atributos de tipo string en K-1 columnas 
df_train_delivery = pd.get_dummies(df_train_delivery, columns= str_var, drop_first=True)

#Definimos vector Objetivo
vector_objetivo = 'delay_time'

#Enlistamos y removemos vector objetivo de la matriz de entrenamiento
colname_x = list(df_train_delivery.columns)
colname_x.remove(vector_objetivo)

#definimos matriz de entrenamiento y vector objetivo
x_matriz = df_train_delivery[colname_x]
y_vector = df_train_delivery[vector_objetivo]

#Generamos conjunto de entrenamiento y validación 
x_train, x_test, y_train, y_test = train_test_split(x_matriz, y_vector, test_size=0.33, random_state=11238)

#Entrenamiento de modelos
model_logit = LogisticRegression().fit(x_train, y_train)
model_decisiontree = DecisionTreeClassifier().fit(x_train, y_train)
model_randomforest = RandomForestClassifier().fit(x_train, y_train)
model_gradientboost = GradientBoostingClassifier().fit(x_train, y_train)
model_bernoulli = BernoulliNB().fit(x_train, y_train)

models = [model_logit, model_decisiontree, model_randomforest, model_gradientboost, model_bernoulli]

for model in models:
    print(f'Classification report: {type(model).__name__}\r\n\n{classification_report(y_test, model.predict(x_test))}\n\n\n')

#Guardamos el mejor modelo 
pickle.dump(model_bernoulli, open("Bernoulli.pkl" , 'wb'))
