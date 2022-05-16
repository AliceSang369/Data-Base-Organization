import pymongo
import pprint
import numpy as np
import datetime

from pymongo import MongoClient

client = MongoClient()  # connects on default host
# client = MongoClient('localhost',27017))  # explicit connect command

db = client.db_people    


# remove entire collection, i.e. all docs in peopleDB.theEmps 
db.theEmps.remove()

# create UNIQUE INDEX
# db.theEmps.create_index( [('pid', pymongo.ASCENDING)], unique=True )

# the collection we will create
peeps = db.theEmps  


states = ["AL","AK","AZ","AZ","CA","CO","CT","DE","FL","GA", "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD", "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ", "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC", "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

numManagers = 100
numDocs = numManagers * 20
timeStartInsert = datetime.datetime.now()
print("\nStart inserting " + str(numDocs) + " documents at: " + str(timeStartInsert) )
for i in range(1,numDocs+1):
	aPid = i
	aName = 'Mary'+str(i)
	aAge = np.random.randint(49) + 18
	if i <= numManagers:
		aManager = 1   # managers report to person pid 1
	else:
		aManager = np.random.randint(numManagers - 1) + 2 # report to one of the "numMangers" except 1
	aBirth = 2019 - aAge
	aSalary = np.random.randint(100000) + 30  # lowests paid is 30K
	aState = states[ np.random.randint( len(states) ) ]
	newPerson = {"pid":aPid,"name":aName,"managerId":aManager,"state":aState,"age":aAge,
		"birth":aBirth, "salary":aSalary}
	peeps.insert_one(newPerson)

timeEndInsert = datetime.datetime.now()
timeElapsedInsert = timeEndInsert - timeStartInsert
timeStartQueries = datetime.datetime.now()

print("\nNumber of docs in db.theEmps = " + str(db.theEmps.count()))
# print("\nAt start, output from peeps.find():")
# for objs in peeps.find():
# 	print(objs)

numQueries = 20
print("\nStart " + str(numQueries) + " random queries at: ")
print(datetime.datetime.now())
for i in range(1,numQueries):
	randPID = np.random.randint(numDocs)
	anObject = db.theEmps.find_one( {"pid":randPID} )
	print(anObject)

timeEndQueries = datetime.datetime.now()
timeElapsedQueries = timeEndQueries - timeStartQueries
	
print("\nFinished random queries at: ")
print(datetime.datetime.now())


print("\nElapsed time for inserts = " + str(timeElapsedInsert) ) ;
print("\nElapsed time for queries = " + str(timeElapsedQueries) ) ;

