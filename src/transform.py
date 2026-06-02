import pandas as pd
from datetime import datetime
from utils.logger import logger

def transform_movies_base(all_movies):

    try:
        df = pd.DataFrame(all_movies)

        logger.info(f"Initial movies DataFrame shape: {df.shape}")

        df = df[
            ["id", "title", "release_date", "popularity",
            "vote_average", "vote_count", "genre_ids"]
        ]

        initial_rows = len(df)

        df = df.dropna(subset=["id", "title"])
        df = df.drop_duplicates(subset=["id"])

        # Clean release_date
        df["release_date"] = (
            df["release_date"]
            .replace("", pd.NA)
        )

        df["release_date"] = pd.to_datetime(
            df["release_date"],
            errors="coerce"
        ).dt.date

        df["ingestion_date"] = datetime.now().date()
        df["ingestion_timestamp"] = datetime.now()

        df["release_date"] = df["release_date"].where(
        df["release_date"].notna(),
        None
)

        final_rows = len(df)

        logger.info(f"Dropped {initial_rows - final_rows} rows with null or duplicate IDs.")
        logger.info(f"Transformed movies DataFrame shape: {df.shape}")
        logger.info(f"Null values in movies DataFrame:\n{df.isnull().sum()}")

        return df

    except Exception:
        logger.exception("Error occurred while transforming movies data")
        return pd.DataFrame()

#genres table transform
def transform_genres(genres):
    try:
        df = pd.DataFrame(genres)

        logger.info(f"Initial genres DataFrame shape: {df.shape}")

        df = df.rename(columns={"id": "genre_id", "name": "genre_name"})

        logger.info(f"Transformed genres DataFrame shape: {df.shape}")
        logger.info(f"Null values in genres DataFrame:\n{df.isnull().sum()}")

        return df
    
    except Exception:
        logger.exception("Error occurred while transforming genres data")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
    

#movie_genres bridge table transform
def transform_movie_genres(movies_df):

    try:
        bridge = movies_df[["id", "genre_ids"]].explode("genre_ids")

        logger.info(f"Initial movie_genres DataFrame shape: {bridge.shape}")

        bridge = bridge.rename(columns={
            "id": "movie_id",
            "genre_ids": "genre_id"
        })

        initial_rows = len(bridge)

        bridge = bridge.dropna(subset=["genre_id"])
        bridge = bridge.drop_duplicates()

        final_rows = len(bridge)

        logger.info(f"Dropped {initial_rows - final_rows} rows with null or duplicate genre_ids.")
        logger.info(f"Transformed movie_genres DataFrame shape: {bridge.shape}")
        logger.info(f"Null values in movie_genres DataFrame:\n{bridge.isnull().sum()}")

        return bridge
    except Exception:
        logger.exception("Error occurred while transforming movie_genres data")
        return pd.DataFrame()  # Return an empty DataFrame in case of error