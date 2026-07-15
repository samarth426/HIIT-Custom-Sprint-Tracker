# Multi-Architecture HIIT Sprint Tracker & Analytics Engine

An independent, multi-phase software engineering project that tracks high-intensity interval training (HIIT) sprint parameters. This repository documents the evolution of an application from a local text-based data layer to a full-stack relational database infrastructure, preparing data pipelines for predictive machine learning models.

## Project Evolution

### Phase 1: Local State Serialization (`tracker_v1_json.py`)
- **Architecture**: Local client-side script utilizing flat-file data structures.
- **Data Layer**: High-performance JSON serialization for stateless persistence across runtimes.
- **Safety**: Robust, defensive runtime type-checking via nested `try-except` blocks to prevent numerical invalidation crashes.
- **Analytics**: Local data parsing engine calculating session volume aggregates, maximum execution thresholds, and rolling rest period averages.

### Phase 2: Full-Stack Relational Database Migration (`tracker_v2_mysql.py`)
- **Architecture**: Client-Server architecture separating the execution loop from the persistence tier.
- **Data Layer**: Local relational database management system using a XAMPP-hosted MariaDB/MySQL instance.
- **Database Driver**: Integrated native SQL command execution via the `mysql-connector-python` API wrapper.
- **Transactions**: Secure data routing protocols executing structured queries (`CREATE TABLE`, `INSERT INTO`, `SELECT`) with automatic transaction commits to ensure data integrity.

### Current Roadmap
- **Phase 3: Predictive ML Model**: Implementing `scikit-learn` and `pandas` to train a linear regression model on historical database parameters, automating personalized optimization of training structures based on historical exertion trends.

## Tech Stack
- **Languages**: Python, SQL
- **Libraries & Tools**: Matplotlib, MySQL (XAMPP Server Environment), JSON, Time, Datetime

## Database Schema Design
```sql
CREATE TABLE sprint_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    workout_date DATE NOT NULL,
    num_sprints INT NOT NULL,
    sprint_time_sec INT NOT NULL,
    rest_time_sec INT NOT NULL
);
