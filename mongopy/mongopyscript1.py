import json,pymongo

connection=pymongo.MongoClient("mongodb://localhost")
db=connection.book
record1 = db.book_collection
page=open("test.json")
parsed = json.loads(page.read())

for item in parsed["Records"]:
	record1.insert(item)