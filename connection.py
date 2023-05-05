from pymongo import MongoClient

MONGO_URI = "mongodb+srv://myAtlasDBUser:trinhanthanh@myatlasclusteredu.3bvuqhl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
