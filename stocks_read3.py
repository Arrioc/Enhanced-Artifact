import json
from bson import json_util
from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps, loads

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method performs the aggregation and outputs
# the aggregation results.

def aggregate(filt, proj):
  try:
    myReadResult = collection.aggregate([filt, proj])
    #if specific query exists
    if (myReadResult != None):
      #convert to json and print
      print("Total oustanding shares grouped by industry:")
      print(dumps(myReadResult, indent=4, default=json_util.default))
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)  
    abort(400, str(pm))
    return
  
# This method sets up an aggregation pipeline for 
# a given sector which is sent to the 'aggregate' funtion. 
# The aggregation is stored as a projection and matches 
# the sector given as a query. It groups the 
# results by industry, and performs summation of the 
# industries 'outstanding shares'. It also checks for 
# if no matches were found.
  
def read3_main():
  
  print('Please enter sector with first letter capitolized')
  
  #store user sector
  sector = (raw_input())
  #format user input
  sectorForm = "{\"Sector\" : \""+sector+"\"}"   
  
  #store aggregation query
  filterQ = {"$match" : loads(sectorForm)}    
  projectionQ = {"$group" : {"_id" : "$Industry", "Total Outstanding Shares" : {
                    "$sum" : "$Shares Outstanding"}}}
  
  #if sector query doesnt exist, print error
  match = ({"Sector" : sector})
  if (collection.find_one(match) == None):
    print("No Matches Found For:")
    print(dumps(match))
  #else send query aggregation to aggregation function
  else:
    myReadResult = aggregate(filterQ, projectionQ)

read3_main()