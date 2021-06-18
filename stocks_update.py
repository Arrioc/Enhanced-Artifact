import json
from bson import json_util
from pymongo import MongoClient, errors
from bson.json_util import dumps, loads

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method returns 'false' and a message for when 
# document creation wasn't successful

def update_document(query, newMod):
  try:
    myUpdateResult = collection.update_one(query, newMod)
    return myUpdateResult
  except errors.DuplicateKeyError as e:
    print("Duplicated key error", e)               
    return False                                    
  except WriteError as we:
    print("MongoDB returned error message", we)
    return False
  except WriteConcernError as wce:
    print("MongoDB returned error message", wce)
    return False
  except PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

# This method accepts input for a ticker. If the ticker doesnt 
# exist it exits, else it takes input for a key and value, and
# preformats them. It then sends this data to the update 
# function.On return, it reports on whether the update worked.
  
def modify_main():
  
  #request ticker data for query
  print('Please enter capitolized Ticker name')
  
  #store variable for query
  newQuery = (raw_input())                          
  #format user input                                
  myQuery = loads("{\"Ticker\" : \""+newQuery+"\"}")
  #check for document existance, exit if none
  if (not collection.find_one(myQuery)):
    print("Document not found.")            
    
    
  #else continue...
  else:
    #store field input for modify_doc                  
    print('Please enter field name')                    
    key = (raw_input())
    print('Please enter field value')
    value = (raw_input())
    #check whether string or number, format accordingly
    if (value == int or float and not str):           
      modify = loads("{\""+key+"\" : "+value+"}")
    else:                                             
      modify = loads("{\""+key+"\" : \""+value+"\"}")

    newUpdate = {"$set" : modify}                         

    #update execution with query and modification
    myUpdateResult = update_document(myQuery, newUpdate)

    #if file was updated
    if (myUpdateResult.modified_count == 1):
      # print raw result & update results
      print(dumps(myUpdateResult.raw_result))
      print("Document updated!")
    #if file is not updated
    else:
      #print raw result & update result
      print(dumps(myUpdateResult.raw_result))
      print("File was not modified. The modification already exists.")


modify_main()