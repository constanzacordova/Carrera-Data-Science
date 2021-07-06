import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sn
import statsmodels.formula.api as snf
from sklearn.metrics import mean_squared_error, r2_score

def valores_perdidos(df):
    '''''
    valores_perdidos: Entrega los varoles perdidos por variable que contiene un DataFrame 
    
    Parametro:
    df = DataFrame
    '''''
    for i in list(df.columns):
        nulos = len(df[df[i].isnull() == True])
        print('Variable: ', i, '|| Valores perdidos: ',nulos,'\n')

def descriptive_var(data):
    '''''
    descriptive_var entrega las variables con el listado de valores únicos 
    que contiene el dataframe incluyendo el tipo de dato de cada variable
    
    Parametro:
    data = DataFrame 
    '''''
    for i in list(data.columns):
        print(i,'\n', data[i].value_counts().keys(),'\n')


def histograma(data, var_estudio, bins = 10):
    '''''
    Parametros:
    data: DataFrame 
    var_estudio: variable en estudio para el gráfico del histograma
    bins: parametrizar bins de histograma 
    '''''
    serie =  data[var_estudio]
    sns.distplot(serie, bins = bins, kde=True, hist_kws={"alpha": 0.6, "color": "grey"}, label = f'{var_estudio} gral').set_title(f'Histograma de {var_estudio}')
    plt.axvline(np.mean(serie), color='r', label = f'media: {round(np.mean(serie),2)}')
    plt.legend()

def evalua_95_confianza(modelo):
    '''''
    evalua_95_confianza: función que retorna tres objetos: var_significativas, var_no_significativas y p_values
        var_significativas: lista de las variables que tienen un 95% de significancia estadistica del modelo a evaluar
        var_no_significativas: lista de las variables que no son estadisticamente significativas con un 95% de confianza
        p_values: retorna una tupla con las variables del modelo y el p-valor
        
    Parametros:
    modelo: modelo de regresión
    '''''

    p_values = modelo.pvalues
    keys_tmp = list(p_values.keys())
    var_no_significativas = []
    var_significativas = []

    for i in keys_tmp:
        value_tmp = modelo.pvalues[i]
        if value_tmp > 0.05:
            var_no_significativas.append(i) 

        else:
            var_significativas.append(i)
        
    return var_significativas, var_no_significativas, p_values

def report_scores(vector_validar, vector_predicho):
    """
    report_scores: entrega las metricas que resumen la diferencia entre 
    los datos empiricos y los datos predichos por el modelo entrenado.
    Las mpetricas que evalúa son Error cuadrático promedio y R-Cuadrado 
                      
    parametros:
        vector_validar: vector que contiene los datos empíricos a validar
        vector_predicho: vector que contiene los datos precichos por el modelo en estudio 
    """
    mse = mean_squared_error(vector_validar, vector_predicho).round(1)
    r2 = r2_score(vector_validar, vector_predicho).round(2)
    print('MSE: ', mse)
    print('R2: ', r2)


def histograma_clases(data, var_estudio, var_obj, bins = 10):
    '''''
    histograma_clases: función que retorna tres histogramas para una variable en estudio. El primer histograma es general, 
    el segundo histograma es sobre la clase 1 del vector objetivo, el tercer histograma es sobre la clase 0 del vector objetivo
    
    Parametros:
    data= DataFrame
    var_estudio=  variable numérica que se quiere estudiar
    var_objetivo=  vector objetivo de clasificación
    bins= bins de histograma
    '''''

    plt.figure(figsize = (18,5))
    
    plt.subplot(1,3,1)
    serie =  data[var_estudio]
    sns.distplot(serie, bins = bins, kde=True, hist_kws={"alpha": 0.6, "color": "grey"}, label = f'{var_estudio} gral').set_title(f'Histograma de {var_estudio}')
    plt.axvline(np.mean(serie), color='r', label = f'media: {round(np.mean(serie),2)}')
    plt.legend()

    plt.subplot(1,3,2)
    serie_true = data[data[var_obj] == 1][var_estudio]
    sns.distplot(serie_true, bins = bins, kde=True, hist_kws={"alpha": 0.6, "color": "skyblue"}, label = f'{var_obj}: 1').set_title(f'Histograma de {var_estudio}, con clase de {var_obj}: 1')
    plt.axvline(np.mean(serie_true), color='r', label = f'media: {round(np.mean(serie_true),2)}')
    plt.legend()

    plt.subplot(1,3,3)
    serie_false = data[data[var_obj] == 0][var_estudio]
    sns.distplot(serie_false, bins = bins, kde=True, hist_kws={"alpha": 0.5, "color": "orange"}, label = f'{var_obj}: 0').set_title(f'Histograma de {var_estudio}, con clase de {var_obj}: 0')
    plt.axvline(np.mean(serie_false), color='r', label = f'media: {round(np.mean(serie_false),2)}')
    plt.legend()