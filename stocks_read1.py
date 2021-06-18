import json
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps, loads

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This funtion returnts the query results
# requested by the user. Note: if there were none, 
#it prints a '0'.

#read query and print results
def moving_average(document):
  try:
    myReadResult = collection.find(document)
    #if specific query exists
    if (myReadResult != None):
      #convert to json and print count
      print("There are:")
      print((dumps(myReadResult.count())))
      print("reports.")
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

# This program takes a high and low number from 
# the user, checking for errors, and then preformatting
# them for a query which is sent to the 'moving_average' funtion.
  
def read1_main():
  
  print('Enter high integer or decimal for 50-Day Simple Moving Average') 
  #store high value from user
  try:
    high = loads(raw_input())
  #return error if badly formatted data 
  except ValueError:
    print("ValueError: wrongly formatted entry")
    return "Error occured"

  print('Enter low integer for 50-Day Simple Moving Average')
  #store low value from user  
  try:
    low = loads(raw_input())
  #return error if badly formatted data 
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"
  
  #take document & format key/values for query
  myQuery = {"50-Day Simple Moving Average" : {"$lt" : high, "$gt" : low}}

  #send query to read function
  myReadResult = moving_average(myQuery)

read1_main()