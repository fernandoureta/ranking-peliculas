import pandas as pd

# Cargar datos
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

# Calcular rating promedio y total de votos por película
ratings_avg = ratings.groupby('movieId').agg(
    rating_promedio=('rating', 'mean'),
    total_votos=('rating', 'count')
).reset_index()

# Unir con información de películas
peliculas_con_rating = movies.merge(ratings_avg, on='movieId', how='inner')

# Filtrar películas con al menos 50 votos (evitar ruido estadístico) y ordenar
peliculas_top = peliculas_con_rating[peliculas_con_rating['total_votos'] >= 50].sort_values(
    by='rating_promedio', 
    ascending=False
)

# Extraer año de forma segura (admite valores faltantes)
peliculas_top['year'] = peliculas_top['title'].str.extract(r'\((\d{4})\)')[0]
peliculas_top['year'] = peliculas_top['year'].astype('Int64')  # 'I' mayúscula permite NaN

# Redondear rating para mejor presentación
peliculas_top['rating_promedio'] = peliculas_top['rating_promedio'].round(2)

# Guardar resultado
peliculas_top[['movieId', 'title', 'year', 'rating_promedio', 'total_votos']].to_csv(
    'peliculas_mejor_valoradas.csv', 
    index=False
)

# Mostrar top 10
print("🏆 Top 10 películas mejor valoradas (mínimo 50 votos):\n")
print(peliculas_top[['title', 'year', 'rating_promedio', 'total_votos']].head(10).to_string(index=False))
print("\n✅ Resultado guardado en: peliculas_mejor_valoradas.csv")