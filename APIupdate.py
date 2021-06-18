import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient, errors
from bottle import get, put, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method executes the update and returns results to 
# the main program. If they ticker was modified, and the
# new ticker already exists, duplicate key error is reported.

#update funtion
def update_document(query, newMod):
  try:
    myUpdateResult = collection.update_one(query, newMod)
    return myUpdateResult
  except errors.DuplicateKeyError as e:
    print("Duplicated key error", e)               
    return False  
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

# This method takes a ticker and key from the users CURL.
# It uses the ticker as the query parameter, and sets the 
# key's value (which is a key and value) as the update parameter
# and calls 'update_function'. Upon return, the result is checked 
# and reports whether the document was updated, has already been 
# modified, or is not found.
  
#URI paths for REST service
@put('/stocks/api/v1.0/updateStock')
def main_update_API():
  #get ticker    
  ticker = request.params.get('ticker')
  myQuery = {"Ticker" : ticker}  
  #check for document existance, exit if none 
  if (not collection.find_one(myQuery)):
    print("Document not found.")
  
  #else continue...
  else:  
    #get key & value in json       
    modify = request.json["key-value"]  
    #set key and value to update
    newUpdate = {"$set" : modify}

    #pass query and update to update function
    myUpdateResult = update_document(myQuery, newUpdate)

    #if file was modified
    if (myUpdateResult.modified_count == 1):
      #print raw result & update result
      print(dumps(myUpdateResult.raw_result))
      print("Document updated!")
    #if file was not modified  
    else:
      #print raw result & update result
      print(dumps(myUpdateResult.raw_result))
      print("File was not modified. The modification already exists.")


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)  

