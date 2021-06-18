import json
from bson import json_util
from bson.json_util import dumps, loads
from pymongo import MongoClient, errors

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method queries using the query parameter and executes deletion
# on the field using the field parameter, then returns results to main.

def delete_field(query, newFdel):
  try:
    myDeleteResult = collection.update_one(query, newFdel)
    return myDeleteResult
  except PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

# This method takes user ticker input, and checks if it exists.  
# If the ticker doesnt exist its reported and the program quits.
# If the ticker exists a field name is requested, stored and 
# formatted before being sent to the 'delete_field' funtion, 
# and then reports on the results sent back from the funtion.

def del_field_main():
  
  #request ticker data for query
  print('Please enter capitolized Ticker for the document to be modified.')
  
  #store variable for query
  newQuery = (raw_input()) 
  
  #format user input                                
  myQuery = loads("{\"Ticker\" : \""+newQuery+"\"}")
  
  #if query found no such ticker, report
  if (collection.find_one(myQuery) == None):
    print("Document not found.")
  
  #else continue...
  else:                                                              
    print('Please enter field to be removed with initial letter capitolized')

    #store field for deletion
    key = (raw_input())
    #format & load json for given field     
    deleteForm = "{\""+key+"\" : \"\"}"  
    removeField = loads(deleteForm)

    #store unset field to be removed 
    newFieldDel = {"$unset" : removeField}

    #send query & unset field to 'delete_field' function
    myDeleteResult = delete_field(myQuery, newFieldDel)

  
    #if modify count is 1
    if (myDeleteResult.modified_count == 1):
      #show confirmation results
      print(dumps(myDeleteResult.raw_result))
      print("Document field has been removed.")
    else:
      #show non-confirmation results
      print(dumps(myDeleteResult.raw_result))
      print("Document's field could not be found and may have already been removed.")
    
del_field_main()