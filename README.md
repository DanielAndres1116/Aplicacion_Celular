# Aplicacion_Celular
## Predicción de los clientes que comprarán una aplicación celular 

### Descripción del Dataset y cómo se obtuvo
Se hace uso de los datos de una empresa que cuenta con una aplicación celular, de donde se pueden obtener sus servicios. 
La base de datos cuenta con dos archivos, en el primero se encuentra la información de los usuarios que han accedido a la aplicación, se tiene información del día y la hora de la instalación de la App, así como el comportamiento que han tenido dentro de la aplicación, qué páginas han visitado. Los datos recolectados son solamente de las primeras 24 horas, una vez que se haya instalado la aplicación, esto se debe a que la empresa proporciona un acceso completo a todas sus opciones, aún las que son pagas en las primeras 24 horas una vez se instala la aplicación, pasado este tiempo se bloquea este acceso, a menos que el cliente se suscriba a la versión paga.
El segundo archivo cuenta con los nombres de las páginas más visitadas y sobre todo las que nos interesa para nuestro análisis. 

### Objetivos
Muchas empresas ofrecen sus servicios a través de aplicaciones móviles. En ocasiones algunos servicios son gratuitos, con la intención de que los usuarios puedan ver lo que ofrece la empresa para posteriormente comprar la membresía paga de la misma, por lo tanto, con este proyecto, se quiso predecir cuál usuario es capaz de comprar una suscripción paga de acuerdo con el comportamiento de visitas que tiene en la aplicación móvil.
En medio del proceso se unieron los datos importantes de ambas tablas para así tener un conjunto con datos más valiosos. Se unificaron algunas variables para hacerlo menos extenso y más claro. También se emplearon diversas gráficas para entender mejor el comportamiento y tendencias de los usuarios, por ejemplo, algunos de los análisis interesantes que aquí se emplearon fueron los de mirar las horas en las que más personas se conectaban, observar las edades predominantes de los usuarios y también observar el tiempo transcurrido entre la suscripción del usuario y cuando se abrió la aplicación. 
Para llevar a cabo todos estos procesos se emplearon las librerías de numpy, pandas, Matplotlib, seaborn y sklearn.

Algunos de los gráficos de importancia que tenemos aquí son los histogramas de distribución de edades por cantidad de visualizaciones para saber las edades predominantes de los usuarios así como el de las horas a las que las personas más suelen ingresar a la página

![image](https://user-images.githubusercontent.com/43154438/118187587-c4d38f00-b404-11eb-837c-1cbfe0f1d5d5.png)

![image](https://user-images.githubusercontent.com/43154438/118187597-c7ce7f80-b404-11eb-91ed-0f785950c256.png)

![image](https://user-images.githubusercontent.com/43154438/118187610-cbfa9d00-b404-11eb-823b-98c9bbc39941.png)


### Conclusiones y resultados obtenidos
##### Al final se aplicó un modelo de regresión logística para realizar la predicción y el resultado obtenido fue el siguiente:

![image](https://user-images.githubusercontent.com/43154438/118187655-d74dc880-b404-11eb-8b48-95bf197c1677.png)

Con ello, la empresa ya tendría una gran idea de cuáles son aquellos usuarios en los que podrían enfocarse más para atraer su atención de una u otra manera y analizar nuevas maneras de llamar la atención de aquellos que es más probable que no compren la app. Un modelo de Machine Learning alimentado con los datos correctos resulta útil para mejorar los procesos de una empresa como esta. 

