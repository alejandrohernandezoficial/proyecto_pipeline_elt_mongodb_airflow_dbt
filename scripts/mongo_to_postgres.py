from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres():
    # Mongo
    mongo_client = MongoClient("mongodb://mongodb:27017/")
    db = mongo_client["ecommerce"]
    collection = db["events"]

    data = list(collection.find())
    df = pd.DataFrame(data)

    if df.empty:
        print("No data found")
        return

    # Limpieza mínima
    df = df[["user_id", "event_type", "amount"]]

    # Postgres
    engine = create_engine("postgresql://airflow:airflow@postgres:5432/warehouse")

    df.to_sql("raw_events", engine, if_exists="replace", index=False)

    print("Data loaded to Postgres")