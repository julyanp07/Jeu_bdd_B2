from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["bdd_python"]
collection_personnages = db["personnages"]
collection_monstres = db["monstres"]