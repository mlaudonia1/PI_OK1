

from fastapi import FastAPI, HTTPException
import pandas as pd
import uvicorn
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import numpy as np



# Cargar datos en el DataFrame (supongamos que ya lo tienes cargado)

data_types = {
    'budget': float,
    'id_pelicula': str,
    'original_language': str,
    'overview': str,
    'popularity': str,
    
    'revenue': float,
    'runtime': float,
    'status': str,
    'tagline': str,
    'title': str,
    'vote_average': float,
    'vote_count': 'Int32',  # Utiliza 'Int32' para un entero nullable
    'genres_ok': str,
    'spoken_languages_ok': str,
    'production_countries': str,
    'belong_to_collection': str,
    'production_companies_ok': str,
    'return': float,
    'release_year': 'Int64'  # Utiliza 'Int64' para un entero nullable
}



votadas_df = pd.read_csv('votadas_df.csv', dtype=data_types, low_memory=False)


# Crea una instancia de la aplicación
app = FastAPI()

# Función para obtener la cantidad de películas producidas en un idioma específico
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    '''Ingresas el idioma, retornando la cantidad de películas producidas en el mismo. 
    Ingresar las dos priemras letras del idioma'''
    cantidad_peliculas = votadas_df[votadas_df['original_language'] == idioma].shape[0]
    return {'idioma': idioma, 'cantidad': cantidad_peliculas}

# Función para obtener la duración y el año de una película específica
@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    '''Ingresas la película, retornando la duración y el año'''
    pelicula_data = votadas_df[votadas_df['title'] == pelicula]
    if pelicula_data.empty:
        return {'error': 'Película no encontrada'}
    else:
        
        duracion = pelicula_data['runtime'].iloc[0]
        anio = pelicula_data['release_year'].iloc[0]

     

        return {'pelicula': pelicula, 'duracion': duracion, 'anio': anio
    }


# Función para obtener información sobre una franquicia específica
# se decidió utilizar la columna 'revenue' en lugar de 'return', ya que la columna 'return' es difícil de construir porque la mayoría de los datos son igual a 0.
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    '''Se ingresa la franquicia, retornando la cantidad de películas, ganancia total y promedio'''
    try:
        franquicia_data = votadas_df[votadas_df['belong_to_collection'] == franquicia]
        if franquicia_data.empty:
            return {'error': 'Franquicia no encontrada'}
        cantidad_peliculas = franquicia_data.shape[0]
        ganancia_total = franquicia_data['revenue'].sum()
        ganancia_promedio = franquicia_data['revenue'].mean()
        return {
            'franquicia': franquicia,
            'cantidad': cantidad_peliculas,
            'ganancia_total': ganancia_total,
            'ganancia_promedio': ganancia_promedio
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Función para obtener la cantidad de películas producidas en un país específico

# Un ejemplo simple de mapeo de palabras clave a nombres de países
country_mapping = {
    'United States':'United States of America',
    'eeuu': 'United States of America',
    'usa': 'United States of America',
    'francia': 'France',
    'Francia': 'France',
    'alemania': 'Germany',
    'Alemania': 'Germany',
        'UK': 'United Kingdom',
    # Agrega más mapeos aquí según tus necesidades
}
# Función para obtener cantidad de películas por país
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    '''Se ingresa un país, retornando la cantidad de películas producidas en el mismo.'''
    try:
        # Busca en el mapeo de países y obtén el nombre completo del país
        full_country_name = country_mapping.get(pais.lower(), pais)
        
        cantidad_peliculas = votadas_df[votadas_df['production_countries'].str.contains(full_country_name, case=False)].shape[0]
        return {'pais': full_country_name, 'cantidad': cantidad_peliculas}
    except Exception as e:
        return {'error': 'Ocurrió un error al procesar la solicitud', 'detalle': str(e)}



# Función para obtener el revenue total y la cantidad de películas de una productora específica
@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora: str):
    '''Se ingresa una productora, entregando el revenue total y la cantidad de películas que realizó.'''
    try:
        productora_data = votadas_df[votadas_df['production_companies_ok'].str.contains(productora, case=False)]
        if productora_data.empty:
            return {'error': 'Productora no encontrada'}
        
        revenue_total = productora_data['revenue'].sum()
        cantidad_peliculas = productora_data.shape[0]
        
        return {
            'productora': productora,
            'revenue_total': revenue_total,
            'cantidad_peliculas': cantidad_peliculas
        }
    except Exception as e:
        return {'error': 'Ocurrió un error al procesar la solicitud', 'detalle': str(e)}
        

# Función para obtener información sobre un director específico y sus películas
@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    '''Se ingresa el nombre de un director que se encuentre dentro de un dataset, debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista.'''
    director_data = votadas_df[votadas_df['director'] == nombre_director]
    if director_data.empty:
        return {'error': 'Director no encontrado'}
    retorno_total_director = director_data['return'].sum()
    peliculas_info = []
    for index, row in director_data.iterrows():
        pelicula_info = {
            'nombre_pelicula': row['title'],
            'fecha_lanzamiento': row['release_date'],
            'retorno_individual': row['return'],
            'costo': row['budget'],
            'ganancia': row['revenue']
        }
        peliculas_info.append(pelicula_info)
    return {
        'director': nombre_director,
        'retorno_total_director': retorno_total_director,
        'peliculas': peliculas_info
    }
#Modelo de Recomendación de peliculas
@app.get('/recommend_movies/{title}')
def recommend_movies(title: str):
    try:
        # Preprocesamiento de datos
        votadas_df["overview"].fillna(" ", inplace=True)
        stopwords = ['united', 'states', 'nan', "English", "Film", "man", "boy", "girl", "woman", "United Kingdom"]
        
        vectorizer_overview = TfidfVectorizer(stop_words='english')
        vectorizer_overview.stop_words_ = vectorizer_overview.get_stop_words().union(stopwords)
        overview_vectors = vectorizer_overview.fit_transform(votadas_df['overview'])
        vector_overview_preprocessed = overview_vectors.toarray()

        vectorizer_title = TfidfVectorizer(stop_words='english')
        vectorizer_title.stop_words_ = vectorizer_title.get_stop_words().union(stopwords)
        title_vectors = vectorizer_title.fit_transform(votadas_df['title'])
        vector_titles_titles_preprocessed = title_vectors.toarray()

        # Codificación one-hot del belong to collection
        encoder = OneHotEncoder()
        btc_encoded = encoder.fit_transform(votadas_df["belong_to_collection"].values.reshape(-1, 1)).toarray()

        # Codificación one-hot a genres_ok
        genre_encoded = encoder.fit_transform(votadas_df["genres_ok"].values.reshape(-1, 1)).toarray()

        # Combina los vectores de títulos preprocesados con columnas 'vote_count' y género
        features_combined = np.concatenate((vector_overview_preprocessed, vector_titles_titles_preprocessed, votadas_df['vote_count'].values.reshape(-1, 1), genre_encoded, btc_encoded), axis=1)

        # Normalización de características si es necesario
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features_combined)

        # Calcula la matriz de similitud del coseno entre las películas
        similarity_matrix = cosine_similarity(features_scaled)

        # Obtener el índice de la película basado en el título
        index = votadas_df[votadas_df["title"] == title].index[0]

        # Filtrar las películas similares por género apropiado para niños
        filtered_similar_movies = [movie_index for movie_index in range(len(similarity_matrix[index])) if any(keyword in genre for keyword in ['Animation', 'Family'] for genre in votadas_df['genres_ok'].iloc[movie_index].split(','))]

        # Calcular la similitud solo para las películas filtradas
        filtered_similarity_scores = similarity_matrix[index][filtered_similar_movies]

        # Obtener las películas más recomendadas (excluyendo la película de referencia)
        similar_movies = np.argsort(filtered_similarity_scores)[::-1][1:6]
        top_movies = votadas_df.iloc[filtered_similar_movies[similar_movies]]['title'].tolist()

        return top_movies
    except Exception as e:
        return {'error': 'Ocurrió un error al procesar la solicitud', 'detalle': str(e)}@app.get('/recommend_movies/{title}')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

