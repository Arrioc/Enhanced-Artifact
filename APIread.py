import json
from bson import json_util
from pymongo import MongoClient, errors
from bson.json_util import dumps
from bottle import get, route, run, request

connection = MongoClient('localhost', 27017)
db = connection['market']                             
collection = db['stocks']                     


# This method executes the query and returns results.

#read function
def read_document(document):
  try:
    myReadResult = collection.find(document)
    return myReadResult

  except errors.PyMongoError as pm:
    print("MongoDB returned error message", pm)
    abort(400, str(pm))
    return

  
# This method takes from the user's CURL a ticker variable 
# and preformats it. It then checks and reports on the file's 
# existance. If the file was found, the query data is sent to 
# the query function. On return, it outputs the queried document.
  
#URI paths for REST service
@get('/stocks/api/v1.0/getStock')                       
def main_read_API():
  #take value for query
  ticker = request.json["Ticker"]
  myQuery = {"Ticker" : ticker}
  
  #check for document existance, exit if none
  if (not collection.find_one(myQuery)):
    print("Document not found.")            
    
    
  #else continue...
  else:  
    #send to read function
    myReadResult = read_document(myQuery)    
    
    #convert returned doc to json and print
    print(dumps(myReadResult, indent=4, default=json_util.default))     
    
    
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)   

