import os
import sys
import json
import certifi
import pandas as pd
import pymongo
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()

if MONGO_DB_URL is None:
    raise Exception("MONGO_DB_URL is not set in .env file")


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path: str):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = json.loads(data.to_json(orient="records"))
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = self.mongo_client[database]
            col = db[collection]
            col.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = "Network_data\phisingData.csv"
    DATABASE = "KEV_AI"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()

    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)

    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(no_of_records)
