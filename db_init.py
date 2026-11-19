from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["bdd_python"]
collection = db["personnages"]
collection = db["monstres"]