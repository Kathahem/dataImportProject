import os
import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
#mycol = mydb["customers"]
#mydict = {"firstname":"Kevin","color":"purple"}
#x = mycol.insert_one(mydict)
#print(x.inserted_id)
directory ="./data/"
for fileName in os.listdir(directory ):
    if fileName.endswith(".json"):
        with open(directory + fileName,"r") as read_file:
            data = json.load(read_file)
            for collection in data:
                mycol = mydb[collection]
                print(collection)
                for document in data[collection]:
                    mycol.insert_one(document)


