##python -m src.main

from src.extract import get_movies, get_genres
from src.transform import (
    transform_movies_base,
    transform_genres,
    transform_movie_genres
)
from src.load import load_movies_dim, load_genres, load_movie_genres, load_movies_history
from utils.logger import logger

def main():
    try:
        all_movies = []
        logger.info("===========EXTRACTING DATA FROM API===========")
        logger.info("EXTRACTING MOVIES DATA...")
        for page in range(1, 6):
            all_movies.extend(get_movies(page))
        logger.info("EXTRACTING GENRES DATA...")
        genres_raw = get_genres()

        logger.info("===========TRANSFORMING DATA===========")
        base_df = transform_movies_base(all_movies)
        movies_dim_df = base_df.drop(columns=["genre_ids"])
        movies_history_df = base_df.drop(columns=["genre_ids"])

        genres_df = transform_genres(genres_raw)
        movie_genres_df = transform_movie_genres(base_df)

        logger.info("===========LOADING DATA INTO DATABASE===========")
        load_genres(genres_df)
        load_movies_dim(movies_dim_df)
        load_movie_genres(movie_genres_df)
        load_movies_history(movies_history_df)

        logger.info("===========ETL PIPELINE COMPLETED SUCCESSFULLY===========")

    except Exception:
        logger.exception("PIPELINE FAILED")

if __name__ == "__main__":
    main()