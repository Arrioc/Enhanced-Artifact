import json
from bson import json_util
from pymongo import MongoClient, errors
from bson.json_util import dumps, loads

connection = MongoClient('localhost', 27017)
db = connection['market']                             
collection = db['stocks']                     

# This method executes the query and reports on 
# whether no file was found, otherwise it outputs 
# the document requested or reports any error.

#read function
def read_document(document):
  try:
    myReadResult = collection.find(document)
    #if specific query exists
    if (myReadResult.count() != 0):
      #convert to json and print
      print(dumps(myReadResult, indent=4, default=json_util.default)) 
    #if result found 0 matching files  
    elif (myReadResult.count() == 0):
      #return error message
      print("No File Found With That Criteria.")
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

# This method takes from the user a ticker 
# string, preformats it, and then sends it to
# the 'read_document' query function.

def read_main():
  print('Please enter capitolized ticker name')
  #store variable for query                           
  try:
    newQuery = (raw_input())                          
    #format user input                                
    myQuery = loads("{\"Ticker\" : \""+newQuery+"\"}")
                  
  #return error if badly formatted data  
  except ValueError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"      
  except TypeError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"

  #send to read funtion
  myReadResult = read_document(myQuery)

read_main()
