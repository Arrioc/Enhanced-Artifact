import json
from bson import json_util
from pymongo import MongoClient, errors
from bson.json_util import dumps
from bottle import get, put, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method queries using the query parameter and executes deletion
# on the field using the field parameter, then returns results to main.

#delete field function
def APIdelete_field(query, newFdel):
  try:
    myDeleteResult = collection.update_one(query, newFdel)
    return myDeleteResult
  except PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return


# This method takes the ticker from the CURL, and checks its existance.  
# If the ticker doesnt exist its reported and the program quits.
# If the ticker exists the field name is requested & stored in an 
# "unset" statement before being sent to the 'delete_field' funtion. 
# The method then reports on the results sent back from the funtion.

#stocks_del_field:
@put('/stocks/api/v1.0/delField')
def main_del_field_API():
  
  #get ticker, store as json variable    
  ticker = request.params.get('ticker')
  myQuery = {"Ticker" : ticker}
  
  #if query found no such ticker, report
  if (collection.find_one(myQuery) == None):
    print("Document not found.")
  
  #else continue...
  else:                                                              
    #get key & store          
    key = request.json["Key"]

    #store unset field to be removed 
    newFieldDel = {"$unset" : key}

    #send query & unset field to 'delete_field' function
    myDeleteResult = APIdelete_field(myQuery, newFieldDel)
  
    #if modify count is 1
    if (myDeleteResult.modified_count == 1):
      #show confirmation results
      print(dumps(myDeleteResult.raw_result))
      print("Document field had been removed.")
    else:
      #show non-confirmation results
      print(dumps(myDeleteResult.raw_result))
      print("Document's field could not be found and may have already been removed.")


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True) 
