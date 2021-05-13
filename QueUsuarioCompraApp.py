# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:13:07 2020

@author: Daniel Andres
"""

### IMPORTAR LIBRERÍAS ###
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### IMPORTAR LOS DATOS ###
data = pd.read_csv('appdata10.csv')
paginas = pd.read_csv('top_screens.csv').top_screens.values
print(paginas)

### UNIR LAS DOS BASES DE DATOS ###
#Aseguro que todos los datos sean una serie y esten separados por una coma
data['screen_list'] = data.screen_list.astype(str) + ','

#Creo nuevas columnas con las páginas más vistas e indico las páginas que fueron visitadas
#De igual forma reemplazo los datos de screen_list por los nombres de página visitados
for x in paginas:
    data[x] = data.screen_list.str.contains(x).astype(int)
    
data = data.drop(columns=['screen_list'])

#Sumar las columnas similares
#Pantallas de ahorros
pantalla_savings = ["Saving1",
                    "Saving2",
                    "Saving2Amount",
                    "Saving4",
                    "Saving5",
                    "Saving6",
                    "Saving7",
                    "Saving8",
                    "Saving9",
                    "Saving10"]
data["SavingCount"] = data[pantalla_savings].sum(axis=1)
data = data.drop(columns=pantalla_savings)

#Pantallas de créditos
pantalla_credits = ["Credit1",
                    "Credit2",
                    "Credit3",
                    "Credit3Container",
                    "Credit3Dashboard"]
data["CMCount"] = data[pantalla_credits].sum(axis=1)
data = data.drop(columns=pantalla_credits)

#Pantallas de CC
pantalla_cc = ["CC1",
                "CC1Category",
                "CC3"]
data["CCCount"] = data[pantalla_cc].sum(axis=1)
data = data.drop(columns=pantalla_cc)

#Pantallas de prestamo
pantalla_loan = ["Loan",
                  "Loan2",
                  "Loan3",
                  "Loan4"]
data["LoansCount"] = data[pantalla_loan].sum(axis=1)
data = data.drop(columns=pantalla_loan)

### ANALIZAR LOS DATOS ###
#Conocer el formato de los datos
tipos_datos = data.dtypes

#Conocer los datos nulos
datos_nulos = data.isnull().sum()

### PROCESAMIENTO DE LOS DATOS ###
#Convierto la columna de hora en datos enteros
data.hour.head()
data["hour"] = data.hour.str.slice(1,3).astype(int)
data.hour.head()

#NOTA: no se pueden hacer las siguientes dos visualizaciones al mismo tiempo, por ende se comenta 1 (averiguar como hacerlo en subplots) 

## VISUALIZACIÓN DE LOS DATOS ###
#Visualizar la distribución de edades de los usuarios
# data.age.hist(bins=200)
# plt.ylabel('Cantidad de visualizaciones')
# plt.xlabel('Edad')
# plt.title('Distribución de Edad de los Usuarios')

#Visualizar las horas de conexión
sns.distplot(data.hour)
plt.xlabel('Hora')
plt.title('Horas de Conexión')

#Visualizar el tiempo transcurrido en que se suscribió y se abrió la aplicación
#Convierto las columnas con horas en formato datetime
data['first_open'] = pd.to_datetime(data['first_open'])
data['enrolled_date'] = pd.to_datetime(data['enrolled_date'])

data['diferencia'] = (data.enrolled_date-data.first_open).astype('timedelta64[h]')
plt.hist(data['diferencia'].dropna(), range = [0, 100])
plt.title('Tiempo Transcurrido entre la Suscripción y Abrir la App')
plt.show()
tipos_datos = data.dtypes

data = data.drop(columns=['user','first_open','enrolled_date','diferencia'])

### ANÁLISIS DE MACHINE LEARNING ###
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score

#Definir las variables dependiente e independiente
y = data['enrolled']
X = data.drop('enrolled', axis = 1)

#Separar los datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)

# ######################################
# Analisis discriminante lineal para mejorar el modelo
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components = 1)
X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)
# ######################################


#Definir el algoritmo
algoritmo = LogisticRegression()

#Entrenar el algoritmo
algoritmo.fit(X_train, y_train)

#Realizar una predicción
y_test_pred = algoritmo.predict(X_test)

#Se calcula la exactitud y precision del modelo
print("Exactitud: ", accuracy_score(y_test, y_test_pred))
print("Precisión: ", precision_score(y_test, y_test_pred))

