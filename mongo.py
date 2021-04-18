import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://localhost:3306/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())