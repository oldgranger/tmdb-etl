# TMDB ETL PIPELINE

This project is an ETL (Extract, Transform, Load) pipeline that extracts movie data from the TMDB API, transforms and cleans it using Python (Pandas), and loads it into a PostgreSQL database for analysis.

It also maintains historical tracking of movie data for trend analysis.

---

## BUSINESS OBJECTIVE

The goal of this pipeline is to:

- Ingest movie data from an external API (TMDB)
- Clean and structure raw data into analytics-ready tables
- Track historical changes in movie popularity over time
- Enable SQL-based analysis for trends and insights

## DATA PIPELINE FLOW:

### 1. Extract
- Pulls **popular movies (paginated)** from TMDB API
- Fetches **movie genres reference data**
- Handles API errors with logging

**SAMPLE LOG:**

<img width="432" height="363" alt="image" src="https://github.com/user-attachments/assets/50303718-b755-4e86-b81d-ca23a95dd91e" />

---

### 2. Transform
- Cleans missing values and duplicates
- Converts release dates into proper datetime format
- Adds ingestion timestamps
- Normalizes:
  - `movies_dim`
  - `genres`
  - `movie_genres` bridge table

---

### 3. Load
- Loads data into PostgreSQL using SQLAlchemy
- Supports:
  - `UPSERT` for `movies_dim`
  - `APPEND` for `movies_history`
  - `INSERT ON CONFLICT DO NOTHING` for bridge table
  - `REPLACE` for genres table

---

## ERD:

<img width="755" height="535" alt="image" src="https://github.com/user-attachments/assets/3fe9a2a8-be5a-4a0e-ae81-af559eed86ea" />

---

## PIPELINE EXECUTION SCHEDULE

This ETL pipeline was executed daily from **May 20 – May 31** using Windows Task Scheduler (WTS) to simulate a production-like scheduled data ingestion system.

<img width="432" height="363" alt="image" src="https://github.com/user-attachments/assets/53194cfc-7096-41ff-b5a9-7a53f788332f" />

<img width="432" height="363" alt="image" src="https://github.com/user-attachments/assets/825d8f9e-b7df-4a6d-a612-78f45f1da126" />

Each run:
- Extracted fresh movie data from TMDB API
- Transformed and cleaned the dataset
- Loaded updates into PostgreSQL tables
- Appended historical snapshots into `movies_history`

---

## POSTGRESQL TABLES (pgAdmin 4)

### movies_dim

<img width="432" height="363" alt="image" src="https://github.com/user-attachments/assets/45017b93-089f-4cc9-a6dd-166bce5ebc50" />

---

### movie_genres

<img width="432" height="363" alt="image" src="https://github.com/user-attachments/assets/b5b26242-cd8f-4e17-88f2-204455a25e07" />

---

### genres

<img width="432" height="363" alt="image" src="https://github.com/user-attachments/assets/9d277517-007a-4069-bc19-33de017dc60b" />

---

### movies_history

<img width="432" height="363" alt="image" src="https://github.com/user-attachments/assets/1787dee1-885a-4b93-bade-ccfe371ae925" />

---

## SAMPLE QUERIES

### Genre Frequency Analysis

<img width="597" height="500" alt="image" src="https://github.com/user-attachments/assets/117c51f7-545a-4214-b14f-71b1b42d10bc" />

---

### Popularity Trend of the movie "Obsession" Overtime (using history table)

<img width="557" height="600" alt="image" src="https://github.com/user-attachments/assets/dbe900eb-5af3-4926-88b8-5764d9e0d772" />

---

## KEY HIGHLIGHTS 
- End-to-end ETL pipeline design
- API integration (TMDB)
- Data cleaning and transformation using Pandas
- Relational database modeling (PostgreSQL)
- Many-to-many relationship handling
- Time-series / historical data tracking
- Automated scheduled execution (WTS)
- Analytical SQL querying

## FUTURE IMPROVEMENTS
- Airflow / Prefect orchestration
- Docker containerization
- Data validation layer
- Incremental loading instead of full refresh
- Cloud deployment (AWS RDS / GCP Cloud SQL)

## 📜 NOTE: THIS PROJECT IS FOR EDUCATIONAL AND PORTFOLIO PURPOSES .
