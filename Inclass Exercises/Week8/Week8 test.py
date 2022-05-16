# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:30:44 2021

@author: yuwen
"""

import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient() #connects on default host


#Creating
db = client.testDB
aPerson1 = {"name":"Sojourner Truth", "birth":"1797","death":"1883-11-26",
            "knownFor":["abolitionist", "public speaking", "writing", "activism"]}
aPerson2 = {"name":"Susan B. Anthony", "birth":"1820-02-05","death":"1906-03-13",
            "knownFor":["women's suffrage", "public speaking", "writing", "activism"]}
peeps = db.somePeople # think of this as "create table", but no need to specifying fields!
peep_id = peeps.insert_one(aPerson1).inserted_id
print("\nid returned from insert:" + str(peep_id))
peep_id = peeps.insert_one(aPerson2).inserted_id
print("\nid returned from insert:" + str(peep_id))

print("\nOutput from peeps.find():")
for objs in peeps.find():
    pprint.pprint(objs)

# Delet_One()
peeps.delete_one({'name':{'$regex':'So'}}) #if multiple satisfied, only delete the first one
#peeps.delete_one({'name':{'$regex':'Su'}})

#Delete_Many
peeps.delete_many({'name':{'$regex':'S'}}) #clear
# =============================================================================
# print('\n\nAfter delete')
# for objs in peeps.find():
#     pprint.pprint(objs)
# =============================================================================

#Update_One() & Update_Many()
peeps.insert_many([aPerson1,aPerson2])
aQuery = {'name':{'$regex':'Susan'}}
aChange = {'$set':{'name':'Alice'}}
peeps.update_one(aQuery, aChange)
print('\n\nAfter update one:')
for objs in peeps.find():
    pprint.pprint(objs)
print('\n\n update many:')
peeps.update_many(aQuery, aChange)
for objs in peeps.find():
    pprint.pprint(objs)


# =============================================================================
# for cursor in client.list_databases():
#     print(cursor)
# =============================================================================
