#Proyecto Individual de la Carrera de Data Science en Soy Henry

##Sistema de Recomendación de películas con algoritmo de filtrado colaborativo

**Autor@s**

- Mara Laudonia (@mlaudonia1)

### Descripción de proyecto

El objetivo del proyecto es crear un modelo de ML para solucionar un problema de negocio de una startup que provee servicios de agregación de plataformas de streaming. Se crea y se implementa un sistema de recomendación de películas, 
###Desarrollo del proyecto
El primer paso fue la realización de un trabajo de Data Engenieer para dejar los datos limpios y listos para su análisis y posterior creación del modelo. Luego, se realizó un EDA de los datos, y se concluyó que la elección del modelo de machine learning debe ser de algoritmo de filtrado colaborativo basado en similitud?, en base a los datos provistos. Se entrenó el modelo y se creó una API deployable en Render para disponibilizar los datos y que el cliente pueda comprobar la eficacia del modelo de recomendación. El trabajo fue realizado utilizando PYTHON y sus librerías y para el deploy se eligió Render
En cuanto a los recursos, se dispone de dos datasets, movies.cvs y credits.cvs, y un diccionario de datos,  xls. para analizar los datos y elaborar el modelo. Se trata de dos bases de datos muy sucias, que requieren una limpieza extrema para poder extraer los datos que luego serán analizados

### Paquetes necesarios

-El trabajo fue íntegramente realizado utilizando PYTHON y sus librerías y para el deploy se eligió Render
- pandas
- numpy
- random
- matplotlib


### Instrucciones para correr el programa

1.- Instalar paqueterías de python que se encuentran en el requirements.txt

`pip install -r requirements.txt`

2.- Colocar al mismo nivel de ejecución del notebook y de los .py, los .csv a analizar:

- links_small.csv
- ratings_small.csv
- movies_metadata.csv

Para correr con **jupyter notebook**

1.- Abrir el notebook **PI4.ipynb** y ejecutar cada celda 💪 . 

En el notebook se encontrarán las siguientes acciones :

-Carga de los datasets provistos, inspección general de datos y transformaciones básicas solicitadas por el cliente
-Se detectan datos sucios y campos anidados, y se procede a su limpieza, extracción de datos de las columnas anidadas, quita de duplicados, tratamiento de nulos, verificación y cambios de formatos de los campos, entre otros, en base a los objetivos para desarrollar el modelo.
-Se procede a eliminar columnas que no serán utilizadas
-Se procede a efectuar transformaciones mínimas solicitadas por el cliente, que incluyen la creación de dos variables return (con campos revenue y budget), y año de lanzamiento (release_year)
-Se detecta en base los datos que el modelo de recomendación de películas más apropiado es de filtro colaborativo en dase a similitud de contenido.
-Se procede a hacer mayores transformaciones en base a lo que se prevé que necesitará el modelo de recomendación, se crea una nube de palabras para detectar palabras clave entre las películas y que luego se utilizarán en el modelo de machine learning.
-Se exportan los datos a un nuevo dataset movies_etl.csv
-Se decide elaborar una nueva base de datos de películas, en base a las más votadas, para optimizar problemas de memoria y garantizar la ejecución del modelo de recomendación. El nuevo dataset votadas_df pasa desde los 4500 registros a 5000 registros.
-Se crean nuevas funciones para atender las necesidades del cliente, que quiere saber, además de la recomendación, la cantidad de películas por idioma original,  la duración y el año de la película, qué franquicia pertenece la película, cuánto ganó esa franquicia en total, y en promedio por película, el idioma original de las películas, la cantidad de películas producidas por país, las productoras exitosas, en base al revenue total y la cantidad de películas que realizó, y los directores de las películas, con datos de las películas que realizaron y su retorno.

2 -Desarrollo de la API

Se propuso disponibilizar los datos con el framework de FastApi y crear 6 funciones para atender los requerimientos del cliente. Para este ejercicio específico de las funciones , se proporcionó una guía de las funciones que se solicitaron :

+ def **peliculas_idioma( *`Idioma`: str* )**:
    Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de 
    películas producidas en ese idioma.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` cantidad de películas fueron estrenadas en `idioma`*
         

+ def **peliculas_duracion( *`Pelicula`: str* )**:
    Se ingresa una pelicula. Debe devolver la duracion y el año.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` . Duración: `x`. Año: `xx`*

+ def **franquicia( *`Franquicia`: str* )**:
    Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La franquicia `X` posee `X` peliculas, una ganancia total de `x` y una ganancia promedio de `xx`*

+ def **peliculas_pais( *`Pais`: str* )**:
    Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *Se produjeron `X` películas en el país `X`*

+ def **productoras_exitosas( *`Productora`: str* )**:
    Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. 
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La productora `X` ha tenido un revenue de `x`*

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

3- .Abrir el notebook **sistema_recomendacion.ipynb** y ejecutar cada celda.  

-Se carga votadas_df y se realiza un EDA de los datos.
-Se decide implementar el método de similitud de coseno
-Para los inputs del modelo, se realizan nube de palabras a  los campos overview y titulos, 
 -Se crea inicialmente un modelo que contempla las variables overview, title, genres_ok. y belong_to_collecion, de las 500 películas más votadas
-

4- Link de render para visualizar la recomendación de las 5 películas más similares, sobre la base de un título de una película  😏                                                   

5- Link al video explicativo del proyecto individual

😊 :blush:
🖕 :fu:

## Recursos y estructura del proyecto

| Nombre archivo | Contenido|
|----------------|----------|
| **Diccionario de Datos - Movies.xlsx** | Recurso-Diccionario de datos, con los nombres de los campos y la descripción de los mismos |
| **movies.csv** | Recurso -archivo para limpieza de datos |
| **credits.csvx** | Recurso-archivo para limpieza de datos  |
|**movie_etl.csvx** | Recurso-archivo con datos limpios para el realizar el  EDA  
| **votadas_df.csv** | base de datos para crear el modelo de ML con una reducción a 5000 registros |
|  |   |
| **requirements.txt** | Paquetes utilizados |
| **main.py** |  Ejecución de de API |
 **sistema_recomendacion.ipynb** | Jupyter notebook de ejecución para entrenar, predecir, y realizar la recomendación |

# PI_Henry_MLOps
# PI_Henry_MLOps
