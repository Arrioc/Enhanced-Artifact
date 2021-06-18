import json
from bson import json_util
from pymongo import MongoClient, errors
from bson.json_util import dumps,loads 

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method takes the query and projection checking
# if any exist. If found it will print all tickers for 
# the inudstry. If not it will report none were found. 

#query funtion
def find_industry(filt, proj):
  try:
    myReadResult = collection.find(filt, proj)
    #if specific query exists
    if (myReadResult.count() >= 1):
      #convert to json and print in readable format
      print(dumps(myReadResult, indent=4, default=json_util.default)) 
    #if result found 0 files matching criteria 
    elif (myReadResult.count() == 0):
      #return error message
      print("No Files Found For:") 
      print(dumps(filt))
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

# This method will take a user defined industry string and
# preformat the string for use in a query. It then 
# sends the query and a projection for 'ticker' 
# and 0 id's shown to the 'find_industry' function.  
  
def read2_main(): 
  
  print('Enter industry with the initial letter capitolized')     
  #store user string
  industry = (raw_input())
  #format user input
  industryForm = "{\"Industry\" : \""+industry+"\"}"              
                                                                  
  #send to query & projection varaibles to the read funtion
  filterQ = loads(industryForm)                                   
  projectionQ = {"Ticker" : 1, "_id" : 0}
  myReadResult = find_industry(filterQ, projectionQ)

read2_main()