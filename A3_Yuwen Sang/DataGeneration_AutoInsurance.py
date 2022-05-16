# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:21:42 2021

@author: yuwen
"""
# NOTICE: Not real data, just for data management practice!
import numpy as np
import random
import string

states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
         'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho', 
         'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
         'Maine', 'Maryland','Massachusetts','Michigan','Minnesota',
         'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
         'NewHampshire','NewJersey','NewMexico','NewYork',
         'NorthCarolina','NorthDakota','Ohio',    
         'Oklahoma','Oregon','Pennsylvania','RhodeIsland',
         'SouthCarolina','South Dakota','Tennessee','Texas','Utah',
         'Vermont','Virginia','Washington','WestVirginia',
         'Wisconsin','Wyoming']
stateClimateDic = {}
stateDensityDic = {}

for i in range(0, len(states)):
    stateClimateDic[states[i]] = random.choice(['normal', 'bad'])
    stateDensityDic[states[i]] = random.choice(['high', 'medium', 'low'])
    
planDic = {'Premium' : 500, 'Silver' : 800, 'Gold' : 1500, 'Plantinum' : 2500}
planList = list(planDic.keys())
coverage = ['Full', 'Half', 'Quarter']
brands = ['Ford', 'Audi', 'Chevrolet', 'Cadillac','Buick', 'Honda', 'Nissan', 'BMW', 'KIA', 'Jeep', 'GMC', 'Subaru']
colors = ['white', 'black', 'silver', 'red', 'blue', 'others']
carTypes = ['SUV', 'Sport', 'Truck']
coverageAmount = ['high', 'medium', 'low']
np.random.seed(1)


#1. Customers (customerID, cname, age, gender, SSN, dlNum, planName, cityName)
customerPlanDic = {}
customerStateDic = {}
customerNum = 10 #10000 
outfile = open("customersOAT.sql","w") 
for i in range(1,customerNum+1):
    outString = 'insert into Customers values('
    outString += str(i)   # customerID
    outString += ','
    outString += '"Alice"' # name
    outString += ','
    age = str( np.random.randint(80) + 18)   
    outString += age  # age
    outString += ','
    genderNum = np.random.randint(0,2)
    if genderNum == 0:
        outString += '"Male",'
    else:
        outString += '"Female",' # gender
    ssn = '{:09}'.format(np.random.randint(999999999))
    dlNum = '{:09}'.format(np.random.randint(999999999))
    outString += str(ssn); #ssn
    outString += ','
    outString += str(dlNum) # driving license number
    outString += ',"'
    planName = planList[np.random.randint(0,3)]
    outString += planName # planName
    outString += '","'
    state = states[np.random.randint(0, len(states)-1)]
    outString += state # cityName (use state name here)
    outString += '");\n'
    customerPlanDic[str(i)] = planName
    customerStateDic[str(i)] = state
    outfile.write(outString)
outfile.close()


#2. Cars (VINcode, brand, color, ctype, customerID)
numCars = customerNum 
outfile = open("carsOAT.sql", "w")
for i in range (1, numCars+1):
    outString = 'insert into Cars values("'
    outString += str(''.join(random.choices(string.ascii_uppercase + string.digits, k=20))) #VIN code
    outString += '","'
    outString += random.choice(brands) # brand
    outString +='","'
    outString += random.choice(colors) # color
    outString +='","'
    outString += carTypes[np.random.randint(0, len(carTypes))-1] # car types
    outString += '",'
    outString += str(i) # customerID
    outString += ");\n"
    outfile.write(outString)
outfile.close()


#3. City (cityName, climate, pDensity)
# NOTICE: too many cities, use states instead
outfile = open("statesOAT.sql", "w")
for i in range(0,len(states)):
    outString = 'insert into States values("'
    outString += states[i-1] # cityName (stateName)
    outString += '","'
    outString +=  stateClimateDic[states[i]] # climate
    outString += '","'
    outString +=  stateDensityDic[states[i]] # pDensity
    outString += '");\n'
    outfile.write(outString)
outfile.close()

#4. Driving Records (recordID, DRdate, DRtype, customerID, premiumID)
customerPremDic = {}
drivingRecordDic = {}
customerDRdic = {}
premIDlist = []
drNum = 2 # 2000
outfile = open('drivingRecordOAT.sql', 'w')
for i in range (1, drNum + 1):
    outString = 'insert into DrivingRecords values('
    outString += str(i) # recordID
    outString += ',"'
    date = '2020-'
    date += str( np.random.randint(12) + 1)  
    date += '-'
    date += str( np.random.randint(28) + 1)  
    outString += date # date
    outString += '","'
    rType = random.choice(['serious', 'medium', 'slight'])
    outString +=  rType # DRtype
    outString += '",'
    
    customerID = np.random.randint(customerNum) + 1
    while customerID in customerPremDic: # suppose no driver have two accident records
       customerID = np.random.randint(customerNum) + 1
    
    outString += str(customerID) # customerID
    outString += ','
    
    premiumID = np.random.randint(999999999)
    while premiumID in premIDlist:
        premiumID = np.random.randint(999999999)
    premIDlist.append(premiumID)
    outString += str(premiumID) # premium ID
    
    customerPremDic[customerID] = premiumID
    outString += ');\n'
    
    drivingRecordDic[i] = rType
    customerDRdic[i] = customerID
    
    outfile.write(outString)
outfile.close()

#5. Coverage (cAmount, planName, price)
count = 1
outfile=open('coverageOAT.sql', 'w')
for i in range(0, len(planList)):
    base = planDic[planList[i]]
    for j in range(0, len(coverageAmount)):
        outString = 'insert into Coverage values('
        outString += str(count)
        count += 1
        outString += ',"'
        outString += coverageAmount[j] # amount
        outString += '","'
        outString += planList[i] # plan name
        outString += '",'
        outString += str(int(((j+10)/10) * base)) # price
        outString += ');\n'
        outfile.write(outString)
outfile.close()


#6. Premium (premiumID, paymentPeriod, cAmount, recordID, customerID)
pNum = customerNum - drNum
outfile=open('premiumOAT.sql', 'w')
for i in range(1, drNum+1): # customers have accident record
    outString = 'insert into Premium values('
    outString += str(customerPremDic[customerDRdic[i]]) # premiumID
    outString += ',"'
    outString += random.choice(['week', 'month', 'year']) # payment period
    outString += '","'
    outString += random.choice(coverageAmount) #cAmount
    outString += '",'
    outString += str(i) # recordID
    outString += ','
    outString += str(customerDRdic[i]) # customerID
    outString +=');\n'
    outfile.write(outString)

cid = 1;
for i in range(0, pNum):
    outString = 'insert into Premium values('
    premiumID = np.random.randint(999999999)
    while premiumID in premIDlist:
        premiumID = np.random.randint(999999999)
    outString += str(premiumID) # premiumID
    outString += ',"'
    outString += random.choice(['week', 'month', 'year']) # payment period
    outString += '","'
    outString += random.choice(coverageAmount) #cAmount
    outString += '",'
    outString += 'NULL,' # recordID
    while cid in customerPremDic:
        cid += 1
    outString += str(cid) #customerID
    cid +=1
    outString += ');\n'
    outfile.write(outString)
    
outfile.close()








