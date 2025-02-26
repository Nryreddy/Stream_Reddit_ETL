# Stream_Reddit_ETL
## Overview

StreamRedditETL is a data engineering pipeline designed to extract, transform, and load (ETL) Reddit data into an Amazon Redshift data warehouse. This pipeline leverages Apache Airflow for orchestration and integrates multiple AWS services such as S3, Glue, Athena, and Redshift to ensure efficient data processing.

## Architecture

The project consists of the following components:

- **Apache Airflow**: Used for workflow orchestration and scheduling tasks.
- **PostgreSQL**: Backend components for managing Airflow workers.
- **Amazon S3**: Storage layer for raw and processed data.
- **AWS Glue**: Performs data transformations and schema management.
- **Amazon Athena**: Query engine for analyzing transformed data.
- **Amazon Redshift**: Data warehouse for storing and querying structured data.
- **Docker**: Containerization for running Airflow and associated services.
![reddit_PL](https://github.com/user-attachments/assets/84471150-e806-4659-85f5-12279b2d312b)

## Features

- **Reddit API Integration**: Extracts Reddit posts and comments from specified subreddits.
- **Data Transformation**: Cleans, processes, and enriches data using AWS Glue.
- **S3 Storage**: Organizes raw and transformed data in separate S3 buckets.
- **Athena Queries**: Allows SQL-based queries on transformed datasets.
- **Redshift Loading**: Moves structured data into Redshift for further analytics.
- **Airflow DAGs**: Automates the ETL pipeline execution.
![image](https://github.com/user-attachments/assets/8bf4cac0-d281-4b6f-8d4f-d7090b8e0836)

![image](https://github.com/user-attachments/assets/d02306b5-5288-4501-905c-7924d593e8e3)

![image](https://github.com/user-attachments/assets/5a2e4b90-ce1c-47e0-b4cd-bf36766cd54a)
![image](https://github.com/user-attachments/assets/49ffcdae-8f09-4211-a194-b19366c5f1f8)

## Prerequisites

Ensure you have the following installed:

- Python 3.12
- Docker & Docker Compose
- AWS CLI (configured with valid credentials)
- Apache Airflow
- PostgreSQL (for Airflow metadata storage)
- AWS Services: S3, Glue, Athena, Redshift

## Setup and Installation

### 1. Clone the Repository

```sh
git clone https://github.com/Nryreddy/Stream_Reddit_ETL.git
cd Stream_Reddit_ETL
```

### 2. Create a Conda Environment

```sh
conda create -n streamreddit_etl python=3.12 -y
conda activate streamreddit_etl
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file and add the following variables:

```sh
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_SESSION_TOKEN=your_session_token
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_SECRET_KEY=your_reddit_secret_key
```

### 5. Start Docker Services

```sh
docker-compose up -d --build
```

### 6. Initialize Airflow

```sh
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin
```

### 7. Trigger the DAG

Start the Airflow scheduler and webserver:

```sh
airflow scheduler & airflow webserver
```

Then, trigger the `reddit_etl_dag` in the Airflow UI.


