from sqlalchemy import create_engine
from sqlalchemy import text
from utils.logger import logger
from configs.config import DB_PASSWORD  

engine = create_engine(
    f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/tmdb_db"
)

#current/clean movies table/no duplicates
def load_movies_dim(df): 
    if df.empty:
        logger.warning("Movies DataFrame is empty, skipped loading movies_dim")
        return
    try:
        logger.info("LOADING MOVIES_DIM DATA...")

        records = df.to_dict(orient="records")

        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO movies_dim (
                        id, title, release_date, popularity,
                        vote_average, vote_count
                    )
                    VALUES (
                        :id, :title, :release_date, :popularity,
                        :vote_average, :vote_count
                    )
                    ON CONFLICT (id)
                    DO UPDATE SET
                        title = EXCLUDED.title,
                        release_date = EXCLUDED.release_date,
                        popularity = EXCLUDED.popularity,
                        vote_average = EXCLUDED.vote_average,
                        vote_count = EXCLUDED.vote_count;
                """),
                records
            )

        logger.info(f"Inserted/updated {len(records)} rows into movies_dim")

    except Exception:
        logger.exception("Error loading movies_dim")


def load_genres(df):
    if df.empty:
        logger.warning("Genres DataFrame is empty, skipped loading genres")
        return
    logger.info("LOADING GENRES DATA...")
    df.to_sql("genres", engine, if_exists="replace", index=False)
    logger.info(f"Recreated genres table with {len(df)} rows")


def load_movie_genres(df):
    if df.empty:
        logger.warning("Movie Genres DataFrame is empty, skipped loading movie_genres")
        return
    try:
        logger.info("LOADING MOVIE_GENRES DATA...")

        records = df.to_dict(orient="records")

        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO movie_genres (
                        movie_id,
                        genre_id
                    )
                    VALUES (
                        :movie_id,
                        :genre_id
                    )
                    ON CONFLICT (movie_id, genre_id)
                    DO NOTHING;
                """),
                records
            )

        logger.info(f"Loaded {len(records)} rows into movie_genres")

    except Exception:
        logger.exception("Error loading movie_genres")

#full history of movies with duplicates
def load_movies_history(df):
    if df.empty:
        logger.warning("Movies History DataFrame is empty, skipped loading movies_history")
        return
    logger.info("LOADING MOVIES_HISTORY DATA...")
    df.to_sql(
        "movies_history",
        engine,
        if_exists="append",
        index=False
    )
    logger.info(f"Appended {len(df)} rows to movies_history")