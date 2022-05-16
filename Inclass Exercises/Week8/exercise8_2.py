# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:00:58 2021

@author: yuwen
"""

import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient() #connects on default host


#Creating
db = client.testDB
sailor1 = {"sid":"1","name":"Sue","age":"22","rating":"7"}
sailor2 = {"sid":"2","name":"Mary","age":"25","rating":"5"}
peeps = db.sailors # think of this as "create table", but no need to specifying fields!
peep_id = peeps.insert_one(sailor1).inserted_id
print("\nid returned from insert:" + str(peep_id))
peep_id = peeps.insert_one(sailor2).inserted_id
print("\nid returned from insert:" + str(peep_id))

print("\nOutput from peeps.find():")
for objs in peeps.find():
    pprint.pprint(objs)
