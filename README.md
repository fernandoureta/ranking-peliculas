# 🎬 Ranking de Películas por Rating Promedio

Un análisis simple pero funcional del dataset MovieLens para identificar las películas mejor valoradas por los usuarios.

> **Este es mi primer proyecto de data science.** No es un sistema de recomendación complejo con machine learning, sino un análisis exploratorio honesto que demuestra:
> - Limpieza y transformación básica de datos
> - Toma de decisiones con criterio estadístico
> - Comunicación clara de resultados

---

## 📌 ¿Qué hace este proyecto?

1. Carga el dataset MovieLens (ratings + metadatos de películas)
2. Calcula el **rating promedio** por película
3. Filtra películas con **mínimo 50 votos** (evita que una película con 1 voto de 5.0 aparezca como "la mejor")
4. Extrae el año de estreno del título (cuando está disponible)
5. Genera un CSV ordenado con las películas mejor valoradas

---

## ⚠️ ¿Qué NO hace este proyecto?

- ❌ No es un sistema de recomendación personalizado (no predice qué película te gustará)
- ❌ No usa machine learning ni modelos complejos
- ❌ No incluye visualizaciones interactivas ni dashboard web

---

## ⚙️ Tecnologías

- Python 3.11+
- Pandas para manipulación de datos
- Dataset: [MovieLens 25M](https://grouplens.org/datasets/movielens/25m/)

---

## 🚀 Cómo ejecutar

```bash
# Instalar dependencias
pip install pandas

# Ejecutar análisis
python main.py