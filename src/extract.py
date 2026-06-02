import requests
from utils.logger import logger
from configs.config import API_KEY

BASE_URL = "https://api.themoviedb.org/3"

def get_movies(page=1):
    try:
        url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
        
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        movies = data.get("results", [])
        logger.info(f"Extracted {len(movies)} movies from page {page}.")
        return movies

    except Exception:
        logger.exception("Error occurred while extracting movies data")
        return []

def get_genres():
    try:
        url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        genres = data.get("genres", [])
        logger.info(f"Extracted {len(genres)} genres.")
        return genres
    
    except Exception:
        logger.exception("Error occurred while extracting genres data")
        return []