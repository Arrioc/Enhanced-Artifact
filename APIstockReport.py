import json
from bson import json_util
from pymongo import MongoClient, errors
from bson.json_util import dumps
from bottle import post, route, run, request

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method executes the query and reports on whether
# the files were found, otherwise it prints the requested 
# documents.

#read function
def read_document(document):
  try:
    myReadResult = collection.find(document)
    #if query count isnt 0
    if (myReadResult.count() != 0):
      #convert to json and print
      print(dumps(myReadResult, indent=4, default=json_util.default))
    #if result found 0 matching files  
    elif (myReadResult.count() == 0):
      #return error message
      print("No Files Found With That Criteria.")
    return
  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

# This method takes an array of ticker symbols from the CURL 
# and preformats them in order to be queried. It then sends 
# the query to the 'read_document' function.
  
#URI paths for REST service
@post('/stocks/api/v1.0/stockReport')
def main_stockRead_API():
  #take value for query
  array = request.json["array"]
  myQuery = {"Ticker" : {"$in" : array}}
  
  #send to read funtion
  myReadResult = read_document(myQuery)
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)   

