import pymysql
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://65.108.148.94:27017/ezeia_db")
db = client["ezeia_db"]
collection = db["products"]

# Function to return the collection
def get_collection():
    return collection

# MySQL Connection
def get_mysql_connection():
    connection = pymysql.connect(host="127.0.0.1",user="root",password="admin@1234",database="learning",port=3306,autocommit=True,)
    return connection