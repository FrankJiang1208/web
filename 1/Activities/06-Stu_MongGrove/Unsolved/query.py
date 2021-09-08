# Module used to connect Python with MongoDb
import pymongo
import datetime
# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
db = client.fruits_db
answer='yes'
while (answer=='yes'):
    vendor=input("What is the vendor's name? ")
    fruit=input("What is the type of fruit? ")
    amount=input("What is the amount? ")
    ripeness=input('What is the ripeness? ')

    db.fruits.insert_one(
        {
            'vendor_name': vendor,
            'fruit': fruit,
            'quantity': amount,
            'ripeness': ripeness,
            'date':datetime.datetime.today()
        }
    )
    answer=input("Do you want to add another item? ")

# query the classroom collection
fruit = db.fruits.find()

# see change in collection
for f in fruit:
    print(f)