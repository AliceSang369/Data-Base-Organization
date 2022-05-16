# first need to make sure connector is installed:
#  python3 -m pip install mysql-connector-python

# this assumes you have created a user named "testuser2" with all privileges:
#     mysql> create user 'testuser2'@'localhost' identified by 'thepassword' ;
#     mysql> grant all privileges on *.* to 'testuser2'@'localhost' ;
# to read more about how to create users: 
#  https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql




import mysql.connector
import numpy as np

# note:  look at at end of this file - mydb.commit() and mydb.close() -> do not forget
# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )

print ("Hello - starting pythonConnector_ex2.py")

# Changed settings
mydb = mysql.connector.connect(
  user='root',    # could be root, or a user you created, I created 'testuser2'
  passwd='670510',  # the password for that use
  database='exercise7',   # the database to connect to
  host='127.0.0.1',   # localhost
  allow_local_infile=1  # needed so can load local files
)



print(mydb)
myc = mydb.cursor()   # myc name short for "my cursor"

# We need to reset the variable that allows loading of local files 
myc.execute('set global local_infile = 1') 
myc.execute ("use test9") 

print("\n\nPrinting out reserve info at start...")

print('\nHow many reservations now:')
theCommand = 'select count(*) from reserve;'
myc.execute(theCommand)
for x in myc:
	print(x)


# Or, instead, you can use fetchall to get all rows at once
print("\n\n\n\nNow use fetchall() ")
print("\n\nUse fetchall() to get all at once")

theCommand = 'select * from sailors'
myc.execute(theCommand)
sailor_info = myc.fetchall()
print('\nfind out the sailors that older than 20 and delete their reservations: ')
for sa in sailor_info:
	if  (sa[2] > 20):
		sid = sa[0]
		newCommand = "delete from reserve where sid = " + str(sa[0]) + " ;"
		print(newCommand)
		myc.execute(newCommand)


theCommand = 'select * from reserve'
myc.execute(theCommand)

print("\n\nPrinting out reserve info at end...")
row = myc.fetchone()  # gets first row from query set, returns "None" if empty 
while row is not None:
	print(row)
	row = myc.fetchone()  # get next row, returns "None" if at end


print('\nHow many reservations now:')
theCommand = 'select count(*) from reserve;'
myc.execute(theCommand)
for x in myc:
	print(x)


# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )
mydb.commit()
mydb.close() 


