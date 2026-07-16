# HIIT Sprint Tracker & Analytics Engine

A Python-based project that tracks high-intensity interval training (HIIT) sprint sessions. This repository documents the evolution of the application from JSON file storage to a MySQL database backend while adding analytics and data visualization.

## Project Evolution

### Version 1 – JSON Storage
**File:** `tracker_v1_json.py`

- Stores workout sessions in a JSON file.
- Calculates workout statistics such as:
  - Total sprint volume
  - Maximum sprint time
  - Average rest time
- Uses exception handling for input validation.
- Saves data between program runs.

### Version 2 – MySQL Database
**File:** `tracker_v2_mysql.py`

- Migrates workout data from JSON to a MySQL database.
- Uses `mysql-connector-python` to communicate with MariaDB/MySQL.
- Creates database tables and inserts workout sessions.
- Retrieves stored workouts using SQL queries.
- Improves data organization and scalability compared to JSON storage.

### Planned Version 3 – Machine Learning
**File:** `tracker_v3_ml.py` (planned)

- Analyze historical workout data using pandas.
- Train a regression model with scikit-learn.
- Predict personalized sprint and rest recommendations.

## Tech Stack

- Python
- SQL (MySQL / MariaDB)
- Matplotlib
- JSON
- mysql-connector-python
- pandas (planned)
- scikit-learn (planned)
