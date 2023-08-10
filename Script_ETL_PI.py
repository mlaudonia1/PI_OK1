# %%
import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('movies_dataset1.csv')

# Visualizar el contenido del DataFrame. 
df.head()


# %%
#El código arroja un warning, ya que se trata de una base de datos con estructuras complejas por dentro. Analizo más en detalle


# Leer solo las primeras n filas para identificar los tipos de datos
n = 100
df_preview = pd.read_csv('movies_dataset1.csv', nrows=n)

# Ver los tipos de datos de cada columna
print(df_preview.dtypes)


# %%


#Por el  archivo del diccionario del dataset, sabemos que podemos especificar los tipos de datos de las columnas con estructuras complejas
dtypes = {
    'belongs_to_collection': str,
    'production_companies': str,
    'production_countries': str,
    'genres': str
}

# Ahora volvemos a cargar el archivo CSV con los tipos de datos especificados
df = pd.read_csv('movies_dataset1.csv', dtype=dtypes, low_memory=False)


# %%
df.head()

# %%
df.info()

# %% [markdown]
# Observamos que columnas belongs_to_collection, homepage, tagline, tienen muchisima cantidad de nulos. Por ahora lo dejamos y nos concentramos en desanidar los campos con estructuras complejas. Probamos desanidar genres, pero nos encontramos con que de nuevo hay que volver a desanidar. Encontre problema para seguir desanidando, posiblemente porque Id es un campo que queda desanidado y que esta en un campo original

# %%
# Renombrar la columna "id" por "id_pelicula"
df.rename(columns={'id': 'id_pelicula'}, inplace=True)

# Mostrar el resultado
print(df)


# %%
df["genres"]

# %%
import pandas as pd
import ast

# Supongamos que df es el DataFrame que contiene la columna "genres" con listas de diccionarios
# df = ...

# Convertir las cadenas JSON en diccionarios
df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x))

# Desanidar la columna "genres" y obtener las columnas desanidadas en un nuevo DataFrame
df_genres_normalized = pd.json_normalize(df['genres'])

# Combinar las columnas desanidadas con el DataFrame original
df = pd.concat([df, df_genres_normalized], axis=1)

# Ahora df contiene las columnas desanidadas de los diccionarios en el campo "genres"


# %%
df.head()

# %%
df.info()

# %%
df[df.columns[24]]

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 25 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre1', 'name': 'name1'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 24 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre2', 'name': 'name2'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 24 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre3', 'name': 'name3'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 24 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre4', 'name': 'name4'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 24 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre5', 'name': 'name5'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 24 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre6', 'name': 'name6'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 24 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre7', 'name': 'name7'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Utilizar pd.json_normalize() para desanidar los diccionarios en la columna en el índice 24 en adelante igual codigo aplico
df_24 = pd.json_normalize(df[df.columns[24]], sep='_')

# Renombrar la clave 'id' a 'id_genres'
df_24.rename(columns={'id': 'id_genre8', 'name': 'name8'}, inplace=True)

# Eliminar la columna original en el índice 20
df.drop(columns=[df.columns[24]], inplace=True)

# Combinar los DataFrames resultantes con el DataFrame original
df = pd.concat([df, df_24], axis=1)

df.info()

# %%
# Seleccionar las columnas 20 a 35 del DataFrame original
columnas_name_genre = df.iloc[:, 25:40:2]


# %%
columnas_name_genre

# %%
# Suponiendo que ya tienes el DataFrame columnas_name_genre con las columnas de géneros "name1" hasta "name8"

# Concatenar las columnas de géneros en una sola columna
columnas_name_genre["genres"] = columnas_name_genre.apply(lambda x: ",".join(x.dropna()), axis=1)

# Obtener las variables dummies para la columna "genres"
dummies_genres = columnas_name_genre["genres"].str.get_dummies(sep=",")

# Concatenar las variables dummies al DataFrame original
columnas_name_genre = pd.concat([columnas_name_genre, dummies_genres], axis=1)

columnas_genre = columnas_name_genre

# Ahora puedes definir el género de la película usando las variables dummies
# Por ejemplo, si deseas saber si una película es de género "Comedy", "Drama" y "Romance":
columnas_genre["is_comedy"] = columnas_genre["Comedy"] == 1
columnas_genre["is_drama"] = columnas_genre["Romance"] == 1
columnas_genre["is_adventure"] = columnas_genre["Adventure"] == 1
columnas_genre["is_fantasy"] = columnas_genre["Family"] == 1
columnas_genre["is_animation"] = columnas_genre["Animation"] == 1
columnas_genre["is_thriller"] = columnas_genre["Thriller"] == 1
columnas_genre["is_action"] = columnas_genre["Action"] == 1
columnas_genre["is_tv_movie"] = columnas_genre["TV Movie"] == 1
columnas_genre["is_documentary"] = columnas_genre["Documentary"] == 1
columnas_genre["is_crime"] = columnas_genre["Crime"] == 1
columnas_genre["is_war"] = columnas_genre["War"] == 1
columnas_genre["is_western"] = columnas_genre["Western"] == 1

# Agrega más columnas de género según tus necesidades

# Puedes eliminar la columna "genres" si ya no la necesitas
# columnas_name_genre.drop(columns=["genres"], inplace=True)


# %%
columnas_genre

# %%
# Lista de columnas a eliminar
columnas_a_eliminar = ["name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8"]

# Eliminar las columnas del DataFrame
columnas_genre.drop(columns=columnas_a_eliminar, inplace=True)


# %%
columnas_genre

# %%
columnas_genre["Crime"].isnull

# %%
# Renombrar la columna "genres" como "genres_ok" en el DataFrame columnas_genre
columnas_genre.rename(columns={"genres": "genres_ok"}, inplace=True)

# Concatenar la columna "genres_ok" al DataFrame df
df = pd.concat([df, columnas_genre["genres_ok"]], axis=1)


# %%
df.head()

# %%
# limpiamos df de columnas de genero innecesarias y eliminamos las columnas que no serán utilizadas  en el proyecto

columnas_a_eliminar = ["name1", "name2", "name3", "name4", "name5", "name6", "name7", "name8", "video","imdb_id","adult","original_title","poster_path", "homepage"]

df.drop(columns=columnas_a_eliminar, inplace=True)

# %%
Columnas_a_eliminar1 = ["id_genre1","id_genre2","id_genre3","id_genre4","id_genre5","id_genre6","id_genre7","id_genre8","genres" ]


# Eliminar las columnas del DataFrame
df.drop(columns=Columnas_a_eliminar1, inplace=True)

# %%
df.head()

# %%

# Cargar el archivo CSV en un dataFrame, desde donde desanide spoken languajes. El desaniadado de spoken_languages se hizo en otro notebook 
# y la nueva dataram fue guardada en Idiomas.cvs
df1_idiomas = pd.read_csv('Idiomas.csv')

# Visualizar el contenido del DataFrame. 
df1_idiomas.head()


# %%
# Renombrar la columna "spoken_languages" como "spoken_languajes_ok" en el DataFrame 
df1_idiomas.rename(columns={"spoken_languages": "spoken_languages_ok"}, inplace=True)

# Concatenar la columna "spoken_languages_ok" al DataFrame df
df = pd.concat([df, df1_idiomas["spoken_languages_ok"]], axis=1)

# %%
df.info()

# %%
Columna_a_eliminar = ["spoken_languages"]


# Eliminar las columnas del DataFrame
df.drop(columns=Columna_a_eliminar, inplace=True)

# %%
df.info()

# %%
# Exportar como backup la data obtenida hasta ahora del DataFrame,  a un archivo CSV
df.to_csv('df_genero_spoken_languages_ok.csv', index=False)

# %%
# Eliminar la columna número 8 (índice 7)
df.drop(df.columns[7], axis=1, inplace=True)

# %%
#importar archivo df_new.csv que contiene dataframe en donde se desanidó previamente "production_countries"
df_countries = pd.read_csv('df_new.csv')

# Visualizar el contenido del DataFrame. 
df_countries.head()


# %%

# Concatenar la columna "production_countries" al DataFrame df
df = pd.concat([df, df_countries], axis=1)

# %%
df

# %%
df.info()

# %%
df["belongs_to_collection"]

# %%
df.head()

# %%
resultados = df[df.apply(lambda row: row.astype(str).str.contains('director', case=False).any(), axis=1) ]
print(resultados)

# %%
import pandas as pd
import json
import ast


# Rellenar los valores NaN con una lista vacía
df["belongs_to_collection"] = df["belongs_to_collection"].fillna('[]')

# Corregir el formato de los datos en la columna "belongs_to_collection"
def fix_json_format(json_str):
    try:
        return ast.literal_eval(json_str)
    except (SyntaxError, ValueError):
        return []

df["belongs_to_collection"] = df["belongs_to_collection"].apply(fix_json_format)

# Desanidar los diccionarios en la columna "belongs_to_collection" y crear un nuevo DataFrame con las columnas desanidadas
btc_info_df = df["belongs_to_collection"].apply(pd.Series).add_prefix('btc_info_')

# Concatenar el nuevo DataFrame con el DataFrame original
df = pd.concat([df, btc_info_df], axis=1)

# Ver la información del DataFrame resultante
print(df.info())


# %%
df.head()

# %%
# Lista de columnas a eliminar
columnas_a_eliminar = ["belongs_to_collection","btc_info_poster_path","btc_info_backdrop_path","btc_info_0", "btc_info_id"]
df=df.drop(columns=columnas_a_eliminar)


# %%
df.rename(columns={'btc_info_name': 'belong_to_collection'}, inplace=True)

# %%
df.info()

# %%
df["production_companies"]

# %%
import pandas as pd
import json
import ast


# Rellenar los valores NaN con una lista vacía
df["production_companies"] = df["production_companies"].fillna('[]')

# Corregir el formato de los datos en la columna "belongs_to_collection"
def fix_json_format(json_str):
    try:
        return ast.literal_eval(json_str)
    except (SyntaxError, ValueError):
        return []

df["production_companies"] = df["production_companies"].apply(fix_json_format)

# Desanidar los diccionarios en la columna "belongs_to_collection" y crear un nuevo DataFrame con las columnas desanidadas
dfb_info = df["production_companies"].apply(pd.Series).add_prefix('dfb_')

# Concatenar el nuevo DataFrame con el DataFrame original
df = pd.concat([df, dfb_info], axis=1)

# Ver la información del DataFrame resultante
print(df.info())

# %%
df.head()

# %%
df.info()

# %%
from ast import literal_eval
from pandas import json_normalize
import json

# Lee el archivo CSV y carga los datos en un DataFrame



# Utiliza el método explode para desanidar la columna "production_companies"
dfb = df.explode("production_companies")


# Convierte el contenido de la columna "production_companies" en un DataFrame
dfb = json_normalize(df["production_companies"], record_path=None)

# Convierte el contenido de la columna "production_companies" en un DataFrame


# %%


# %%
dfb

# %%
import pandas as pd
from pandas import json_normalize

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_0 = dfb.iloc[:, 0].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_0 = json_normalize(dfb_0.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_0.head())


# %%
dfb_0

# %%
import pandas as pd
from pandas import json_normalize

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_1 = dfb.iloc[:, 1].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_1 = json_normalize(dfb_1.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_0.head())


# %%
dfb_1

# %%
import pandas as pd
from pandas import json_normalize

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_2 = dfb.iloc[:, 2].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_2 = json_normalize(dfb_2.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_2.head())


# %%
import pandas as pd
from pandas import json_normalize

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_3 = dfb.iloc[:, 3].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_3 = json_normalize(dfb_3.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_3.head())


# %%
import pandas as pd
from pandas import json_normalize

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_4 = dfb.iloc[:, 4].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_4 = json_normalize(dfb_4.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_4.head())


# %%




# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_5 = dfb.iloc[:, 5].apply(pd.Series)
# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_5 = json_normalize(dfb_5.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_5.head())


# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_6 = dfb.iloc[:, 6].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_6 = json_normalize(dfb_6.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_6.head())


# %%
import pandas as pd
from pandas import json_normalize


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_7 = dfb.iloc[:, 7].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_7 = json_normalize(dfb_7.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna
print(dfb_7.head())


# %%
import pandas as pd
from pandas import json_normalize

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_8 = dfb.iloc[:, 8].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_8 = json_normalize(dfb_8.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_9 = dfb.iloc[:, 9].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_9 = json_normalize(dfb_9.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_10 = dfb.iloc[:, 10].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_10 = json_normalize(dfb_10.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_11 = dfb.iloc[:, 11].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_11 = json_normalize(dfb_11.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna


# %%
import pandas as pd
from pandas import json_normalize

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_12 = dfb.iloc[:, 12].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_12 = json_normalize(dfb_12.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_13 = dfb.iloc[:, 13].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_13 = json_normalize(dfb_13.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%

# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_14 = dfb.iloc[:, 14].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_14 = json_normalize(dfb_14.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_15 = dfb.iloc[:, 15].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_15 = json_normalize(dfb_15.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_16 = dfb.iloc[:, 16].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_16 = json_normalize(dfb_16.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna

# %%


# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_17 = dfb.iloc[:, 17].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_17 = json_normalize(dfb_17.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna


# %%


# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_18 = dfb.iloc[:, 18].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_18 = json_normalize(dfb_18.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_19 = dfb.iloc[:, 19].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_19 = json_normalize(dfb_19.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Supongamos que tienes un DataFrame llamado dfb y deseas trabajar con la primera columna

# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_20 = dfb.iloc[:, 20].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_20 = json_normalize(dfb_20.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna



# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_21 = dfb.iloc[:, 21].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_21 = json_normalize(dfb_21.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna


# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_22 = dfb.iloc[:, 22].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_22 = json_normalize(dfb_22.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna


# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_23 = dfb.iloc[:, 23].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_23 = json_normalize(dfb_23.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna


# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_24 = dfb.iloc[:, 24].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_24 = json_normalize(dfb_24.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna

# %%


# Paso 1: Desanidar la primera columna (diccionarios) usando apply(pd.Series)
dfb_25 = dfb.iloc[:, 25].apply(pd.Series)

# Paso 2: Usar json_normalize para desanidar los diccionarios en la columna
dfb_25 = json_normalize(dfb_25.to_dict(orient='records'))

# Ahora dfb_0 contiene los datos desanidados de la primera columna

# %%
dfb.info()

# %%
#codigo para unir columnas # Primero, crea una nueva columna con datos vacíos.
#dbf['production_companies_ok'] = ""

# Luego, utiliza apply para cada fila y la función ','.join para unir los valores en una sola cadena separada por comas.
#dbf['production_companies_ok'] = dbf.apply(lambda row: ','.join(str(val) for val in row), axis=1)


# %%

import pandas as pd

# Lista para almacenar los DataFrames
dataframes_list = []

# Iterar sobre los nombres de los DataFrames
for i in range(0, 26):
    # Obtener el nombre del DataFrame actual
    df_name = f"dfb_{i}"
    
    # Agregar el DataFrame actual a la lista
    dataframes_list.append(locals()[df_name])

# Concatenar todos los DataFrames en un nuevo DataFrame llamado dbf
dfb = pd.concat(dataframes_list, ignore_index=True)

# Ahora dbf contendrá la concatenación de todos los DataFrames dfb_0, dfb_2, ..., dfb_26.


# %%
dfb

# %%
dfb

# %%
dfb_1

# %%


# %%
import pandas as pd

# Lista para almacenar los DataFrames
dataframes_list = []

# Iterar sobre los nombres de los DataFrames
for i in range(26):
    # Obtener el nombre del DataFrame actual
    df_name = f"dfb_{i}"
    
    # Supongamos que ya tienes los DataFrames con los nombres adecuados, si no, debes cargarlos aquí.
    # Ejemplo: dbf_0 = pd.read_csv("ruta_del_archivo.csv")
    
    # Asegurarse de que el DataFrame actual tenga la columna "name"
    if "name" in locals()[df_name].columns:
        # Obtener solo la columna "name" del DataFrame actual y agregarla a la lista
        dataframes_list.append(locals()[df_name]["name"])

# Concatenar las columnas "name" en un solo DataFrame
result_df = pd.concat(dataframes_list, axis=1)

# Concatenar los registros de cada columna separados por comas en una sola columna
result_df["merged_names"] = result_df.apply(lambda row: ','.join(row.dropna().astype(str)), axis=1)

# Ahora tienes todas las filas con los registros de las columnas "name" de los DataFrames unidos en una sola columna llamada "merged_names".


# %%
result_df["merged_names"]

# %%

# Supongamos que ya tienes definido el DataFrame df y el DataFrame result_df con la columna "merged_names".

# Añadir la columna "merged_names" de result_df a df
df["merged_names"] = result_df["merged_names"]


# %%
df.head()

# %%



# Utiliza el método drop para eliminar las columnas del DataFrame df
df.drop(columns=["production_companies", "dfb_0","dfb_1","dfb_2","dfb_3","dfb_4","dfb_5","dfb_6","dfb_7","dfb_8","dfb_9","dfb_10","dfb_11","dfb_12","dfb_13","dfb_14","dfb_15","dfb_16","dfb_17","dfb_18","dfb_19","dfb_20","dfb_21","dfb_22","dfb_23","dfb_24","dfb_25"], inplace=True)

# El argumento inplace=True asegura que los cambios se apliquen directamente al DataFrame df y no se devuelva un DataFrame nuevo.


# %%


# Utiliza el método rename para renombrar la columna "merged_names" a "production_companies"
df.rename(columns={"merged_names": "production_companies_ok"}, inplace=True)



# %%
df.info()

# %%
df.head()

# %%
# Exportar el DataFrame a un archivo CSV
df.to_csv('movies_desanidado.csv', index=False)

# %%
import pandas as pd


# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('movies_desanidado.csv')

# Visualizar el contenido del DataFrame. 
df.head()


# %%



# Rellena los valores nulos de 'revenue' y 'budget' con 0
df['revenue'].fillna(0, inplace=True)
df['budget'].fillna(0, inplace=True)


# %%


# Elimina las filas con valores nulos en 'release date'
df.dropna(subset=['release_date'], inplace=True)


# %%
import pandas as pd

# Supongamos que ya tienes el dataframe df con los datos cargados

# Asegura que el campo 'release_date' tenga el formato AAAA-MM-DD
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce', format='%Y-%m-%d')

# Crea la columna 'release_year' para extraer el año de la fecha de estreno
df['release_year'] = df['release_date'].dt.year


# %%
type(df["release_date"])

# %%
df['release_year']

# %%
import pandas as pd


# Convierte los valores de la columna 'release_year' a enteros
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Extrae solo los años de los valores convertidos y crea una nueva columna 'year'
df['year'] = df['release_year'].astype('Int64')

# Ahora, 'year' contendrá solo los años de los valores originales en 'release_year'


# %%
df["year"]

# %%
df.drop(columns=["release_year"], inplace=True)

# Renombra la columna "year" como "release_year"
df.rename(columns={"year": "release_year"}, inplace=True)

# %%
df["release_year"]

# %%
df.info()

# %%
#Filtra el dataframe para obtener el registro con el dato "/ff9qCepilowshEtG2GYWwzt2bs4.jpg" en la columna 'budget'
registro_con_dato = df.loc[df['budget'] == "/ff9qCepilowshEtG2GYWwzt2bs4.jpg"]
print(registro_con_dato)

# %%
# Encuentra y elimina el registro con el dato no válido en la columna 'budget'
df.loc[df['budget'] == "/ff9qCepilowshEtG2GYWwzt2bs4.jpg", 'budget'] = 0

# %%
# Encuentra y elimina los registros con el patrón ".jpg" en la columna 'budget'
df.loc[df['budget'].astype(str).str.contains('.jpg'), 'budget'] = 0

# Convierte la columna 'budget' de str a float
df['budget'] = df['budget'].astype(float)

# Rellena los valores nulos de 'revenue' y 'budget' con 0
df['revenue'].fillna(0, inplace=True)
df['budget'].fillna(0, inplace=True)



# Crea la columna 'return' y calcula el retorno de inversión
df['return'] = df['revenue'] / df['budget']
df['return'].fillna(0, inplace=True)


# %%


# %%
df["return"].head(10)

# %%
# Cuenta cuántos registros en la columna 'budget' tienen valor de cero
registros_con_budget_cero = (df['budget'] == 0).sum()
print(registros_con_budget_cero)

# %%
df.shape

# %%


# Reemplaza los valores cero en 'budget' por 1 para evitar divisiones por cero
#sería recomendable usar solo revenue y no return, en calculos posteriores , al detectar que hay más de 36000 registros cuyo budget es 0
df['budget'].replace(0, 1, inplace=True)

# Crea la columna 'return' y calcula el retorno de inversión
df['return'] = df['revenue'] / df['budget']
df.loc[df['budget'] == 0, 'return'] = df['revenue']




# %%
df['return'].head(10)

# %%
# Redondea las columnas 'return', 'budget' y 'revenue' a dos decimales
df['return'] = df['return'].round(2)
df['budget'] = df['budget'].round(2)
df['revenue'] = df['revenue'].round(2)

# %%

# Elimina los valores infinitos ("inf") en la columna 'vote_count'
df.replace([float('inf')], 0, inplace=True)

# Convierte la columna 'vote_count' a tipo de dato entero (int), ignorando los valores no numéricos
df['vote_count'] = pd.to_numeric(df['vote_count'], errors='coerce').fillna(0).astype(int)

df['vote_count'] = df['vote_count'].astype(int)

# %%
df["vote_count"]

# %%
df["popularity"]

# %%
df.head()

# %%
df.info() # damos una descripcion final del dataset, antes de exprotarlo, para tener claro el tipo de variables que exportamos

# %% [markdown]
# 

# %%
# Exportar el DataFrame a un archivo CSV
df.to_csv('movies_etl.csv', index=False)

# %% [markdown]
# 

# %%
#Para continuar, buscamos duplicados
print(f"Numero de filas duplicadas = {df.duplicated().sum()}")
print("-"*50)

print(f"filas/columnas del dataset de carros antes de eliminar los duplicados = {df.shape}")
print("-"*50)

df.drop_duplicates(inplace = True)
print(f"filas/columnas del dataset de carros despues de eliminar los duplicados = {df.shape}")

# %%
#Manejo de valores faltantes
#Cuantos NaN tenemos?

df.isna().sum()

# %% [markdown]
# Aquí vemos que belong_to_collection tiene varios valores faltantes, pero como nos piden hacer un analisis de esa columna con los datos que tenemos, la dejamos en el modelo para su analisis.
# También production_countries y production_companies tienen gran cantidad de datos faltantes, pero los dejamos para su análisis.
# Evaluamos la conveniencia de dejar tagline o no. En principio, no nos piden algo especial para esta columna, podemos optar por eliminarla.
# También eliminamos Id pelicula para preparar datos para el modelamiento.

# %%
# MANIPULACION DE LA DATA
#import numpy as np
#import pandas as pd
pd.set_option("display.max_columns", None) # MUESTRA TODAS LAS COLUNAS DE UN PANDAS DATAFRAME

# VISUALIZACION DE DATOS
import matplotlib.pyplot as plt
import seaborn as sns

# QUITAMOS LOS WARNINGS DE LAS SALIDAS DEL NOTEBOOK
#import warnings
#warnings.filterwarnings("ignore")

# ESTADISTICAS
from statsmodels.graphics.gofplots import qqplot
# Esta funcion compara la distribucion de la muestra con una distribucion normal, 
# para comprobar si tu muestra se distribuye normalmente o no

# %%
df.head()

# %%
#Correlacion entre variables
#Miramos ahora la correlación entre variables, es buena idea verificar cuáles son las que más correlación tienen, si tienen demasiada correlación, pueden incluir sesgo, y si tienen muy poca, se pueden eliminar sin afectar el rendimiento. Es buena idea revisar cuáles tienen mucha correlación con nuestro objetivo, el precio ´price´, porque serán muy importantes para el modelo.

# Generamos la matriz de correlación

corr = df.corr()
# Ahora, la graficaremos, primero, indicamos el tamaño que tendra el plot.
plt.figure(figsize=(16,8))

# heatmap
sns.heatmap(corr, cmap="YlGnBu", annot=True)
plt.show()

# %% [markdown]
# Vemos que hay una fuerte correlación positiva entre los ingresos (revenue) y el vote_count de la pelicula.
# También vemos que de las peliculas que presentan datos de budget, se relacionan positivamente con las que tienen altos ingresos.

# %% [markdown]
# 

# %% [markdown]
# 

# %%
!pip install --upgrade pip



# %%
!pip install wordcloud

# %%
# Suponiendo que 'df' es el DataFrame que contiene tus datos.
tipo_dato_overview = df['overview'].dtypes
print(tipo_dato_overview)


# %%
# Suponiendo que 'df' es el DataFrame que contiene tus datos.
df['overview'] = df['overview'].astype(str)

# Verificar el tipo de dato después de la conversión
tipo_dato_overview = df['overview'].dtype
df["overview"].head()


# %%
df['title'] = df["title"].astype(str)

# Verificar el tipo de dato después de la conversión
tipo_dato_title = df['title'].dtype
df["title"].head()


# %%
df['tagline'] = df['tagline'].astype(str)

# Verificar el tipo de dato después de la conversión
tipo_dato_overview = df['tagline'].dtype



# %%
df['genres_ok'] = df['genres_ok'].astype(str)

# Verificar el tipo de dato después de la conversión
tipo_dato_genres_ok = df['genres_ok'].dtype


# %%
df['spoken_languages_ok'] = df['spoken_languages_ok'].astype(str)

# Verificar el tipo de dato después de la conversión
tipo_dato_spoken_languages_ok = df['spoken_languages_ok'].dtype



# %%
df['belong_to_collection'] = df['belong_to_collection'].astype(str)

# Verificar el tipo de dato después de la conversión
tipo_dato_btc = df['belong_to_collection'].dtype



# %%
df['production_companies_ok'] = df['production_companies_ok'].astype(str)

# Verificar el tipo de dato después de la conversión
tipo_dato_production_companies_ok= df['production_companies_ok'].dtype


# %%
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Selecciona las columnas relevantes para la nube de palabras.
selected_columns = ['overview', 'tagline', 'title', 'genres_ok', 'spoken_languages_ok', 'production_countries', 'belong_to_collection', 'production_companies_ok']

# Crea una lista de textos de las columnas seleccionadas.
text_list = [df[col].dropna().astype(str).str.strip().tolist() for col in selected_columns if col in df]

# Combina los textos en un solo string.
combined_text = ' '.join([text for sublist in text_list for text in sublist])

# Crea el objeto de la nube de palabras.
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

# Muestra la nube de palabras.
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# %%
#quitamos algunas columnas
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Selecciona las columnas relevantes para la nube de palabras.
selected_columns2 = ['overview', 'tagline', 'title', 'genres_ok', 'belong_to_collection']

# Crea una lista de textos de las columnas seleccionadas.
text_list2 = [df[col].dropna().astype(str).str.strip().tolist() for col in selected_columns2 if col in df]

# Combina los textos en un solo string.
combined_text = ' '.join([text for sublist2 in text_list for text in sublist2])

# Crea el objeto de la nube de palabras.
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

# Muestra la nube de palabras.
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# %%
#En un breve analisis exploratorio para armar una nube de palabras, vemos que podems armar stopwords para poder ajustar mejor el modelo que vayamos a utilizar.  

# %%
#quitamos algunas columnas
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Selecciona las columnas relevantes para la nube de palabras.
selected_columns3 = ['overview', 'title']

# Crea una lista de textos de las columnas seleccionadas.
text_list3 = [df[col].dropna().astype(str).str.strip().tolist() for col in selected_columns3 if col in df]

# Combina los textos en un solo string.
combined_text = ' '.join([text for sublist3 in text_list for text in sublist3])

# Crea el objeto de la nube de palabras.
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

# Muestra la nube de palabras.
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# %%
#no buscamos otuliers, porque nos focalizamos para el modelamiento en variables categoricas
#hay muchos NAN, hay que ver donde estan y quitarlos si es posible
#observams las columnas overview y titulos engobal a genero, tagline, languages, en cuanto a las palaras más utilizadas


# %%
from wordcloud import WordCloud, STOPWORDS
# Crea una lista de stopwords adicionales
additional_stopwords = ['united', 'states', 'nan', "English","Film", "man", "boy", "girl", "woman", "United Kingdom"]

# Combina las stopwords predeterminadas con las adicionales
stopwords = set(list(STOPWORDS) + additional_stopwords)

# Crea el objeto de la nube de palabras con las stopwords
wordcloud = WordCloud(stopwords=stopwords, width=800, height=400, background_color='white').generate(combined_text)

# Muestra la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Guarda la nube de palabras en un archivo de imagen
wordcloud.to_file('nube_de_palabras.png')

# %%
import os
import zipfile


# %%
#comprimimos archivo para poder subirlo a githhub
with zipfile.ZipFile("ETL.zip", "w") as fzip:
    fzip.write("PI4.ipynb")


