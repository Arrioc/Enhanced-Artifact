import json
from bson import json_util
from bson.json_util import dumps, loads
from pymongo import MongoClient, errors

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method returns an error and a message for when 
# document creation wasn't successful or returns a 
# deletion results if it was successful. 

def delete_document(document):
  try:
    myDeleteResult = collection.delete_one(document)
    return myDeleteResult
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm) 
    abort(400, str(pm))
  return

# This method takes input for a ticker, formats it 
# then checks it for errors. It then sends it to
# the deletion function. The deletion function sends 
# back the results which are checked on whether the 
# document was successfully deleted or whether the 
# doc queried couldnt be found.

def delete_main():
                                                      
  #request document ticker for deletion                
  print('Please enter capitolized ticker name for document to be removed.')
  
  #store variable for query                           
  try:
    newQuery = (raw_input())                          
    #format user input                                
    queryForm = "{\"Ticker\" : \""+newQuery+"\"}"     
    myQuery = loads(queryForm)                   
  #return error if badly formatted data  
  except ValueError:
    print("ValueError: wrongly formatted doc!")       
    return "Error occured"                            
  except TypeError:
    print("ValueError: wrongly formatted doc!")
    return "Error occured"  
  
  #Deletion execution with query
  myDeleteResult = delete_document(myQuery)
  
  #if delete count isnt 1
  if (myDeleteResult.deleted_count != 1):
    #print error message
    print(dumps(myDeleteResult.raw_result))
    print("Document not found.")
  else:
    #return confirmation results
    print(dumps(myDeleteResult.raw_result))
    print("Document removed!")
    
delete_main()