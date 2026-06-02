# TMDB ETL PIPELINE

This project is an ETL (Extract, Transform, Load) pipeline that extracts movie data from the TMDB API, transforms and cleans it using Python (Pandas), and loads it into a PostgreSQL database for analysis.

It also maintains historical tracking of movie data for trend analysis.

## DATA PIPELINE FLOW:

### 1. Extract
- Pulls **popular movies (paginated)** from TMDB API
- Fetches **movie genres reference data**
- Handles API errors with logging: SAMPLE LOG
  <img width="1075" height="902" alt="image" src="https://github.com/user-attachments/assets/50303718-b755-4e86-b81d-ca23a95dd91e" />


### 2. Transform
- Cleans missing values and duplicates
- Converts release dates into proper datetime format
- Adds ingestion timestamps
- Normalizes:
  - `movies_dim`
  - `genres`
  - `movie_genres` bridge table

### 3. Load
- Loads data into PostgreSQL using SQLAlchemy
- Supports:
  - `UPSERT` for `movies_dim`
  - `APPEND` for `movies_history`
  - `INSERT ON CONFLICT DO NOTHING` for bridge table
  - `REPLACE` for genres table
--

## ERD:
<img width="755" height="535" alt="image" src="https://github.com/user-attachments/assets/3fe9a2a8-be5a-4a0e-ae81-af559eed86ea" />

## Future Improvements
- Add Airflow / Prefect orchestration
- Containerize with Docker
- Add data validation layer
- Incremental loading
- Deploy to cloud (AWS RDS / GCP Cloud SQL)

### This project is for educational and portfolio purposes.

