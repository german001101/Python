#!/usr/bin/env python3
from decouple import config
from datetime import datetime, timedelta, date
import pymongo
import logging


logging.basicConfig(level=logging.DEBUG)
MONGO_URI = config("MONGO_URI")
MONGO_USER = config("MONGO_USER")
MONGO_PASSWORD = config("MONGO_PASSWORD")
column_insert = "measurement,organizationCode,serviceName,serviceStatus,serviceCount"
clientDb = pymongo.MongoClient("mongodb+srv://{}:{}@{}".format(MONGO_USER, MONGO_PASSWORD, MONGO_URI))
def getTotalOrder(db, collection):
    print(column_insert)
    mydb = clientDb[db]
    mycollection = mydb[collection]
    find =  [
        {"$match": {'organizationCode':{'$in':['IZZIMX','IZZIMXHFC','AXTELLEGO']},'status':'FAILED'}},
        {"$group":{'_id':{'organizationCode': "$organizationCode",'errorMessage':"$errorMessage",'resourceType':"$resourceType"},'total': {"$sum": 1}}},
        {"$sort":{'_id.organizationCode':1}},
        {"$project":{'organizationCode':'$_id.organizationCode', 'errorMessage':'$_id.errorMessage','resourceType':'$_id.resourceType', 'total':'$total', '_id':0}}
        ]
    total = mycollection.aggregate(find)
    for i in total:
        print("{organizationCode},{errorMessage},{resourceType},{total}".format(organizationCode=i["organizationCode"],errorMessage=i["errorMessage"],resourceType=i["resourceType"],total=i["total"]))

getTotalOrder('sym-resource-order-manager','resourceOrders')
