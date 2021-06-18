import json
from bson import json_util
from pymongo import MongoClient, errors
from bson.json_util import dumps
from bottle import get, route, run, request, abort

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method executes the aggregation pipeline, then reports
# a portfolio on the top five shares with the given aggregation 
# criteria.

#aggregate Function
def aggregate(aggreg): 
  try:
    myReadResult = collection.aggregate(aggreg)
    print(myReadResult)
    #if aggregation does not equal 'None'
    if (myReadResult != None):
      #convert to json and print                 
      print("Top five shares grouped by company, strength, 200-Day SMA.")
      print(dumps(myReadResult, indent=4, default=json_util.default)) 
    return
  except Exception as pm:
    print(dumps("MongoDB returned error message", pm))

# This method extracts the CURLS's industry and sets up an
# aggregation pipeline with it. The aggregation matches the industry 
# and groups the top companies by thier relative strength index and 
# the highest 200-Day SMA. It then sorts them by their highest strength
# index. The method first reports an error if the industry doesnt exist, 
# it then sends the aggregation to the 'aggregation' function.
    
#URI for REST service
@get('/stocks/api/v1.0/industryReport')
def main_aggregate_API():

  #take value for query
  industry = request.json["Industry"]

  #aggregation filtering & projection criteria
  aggregationQ = [{"$match" : {"Industry" : {"$regex" : ".*"+industry+".*"}}}, {"$sort" : {"HighestStrength" : -1}},
                  {"$group" :  {"_id" : "$Company", "HighestStrength" : 
                   {"$max" : "$Relative Strength Index (14)"},"Highest200-DaySMA" : 
                   {"$max" : "$200-Day Simple Moving Average"}}},
                   {"$limit" : 5}]

  #if industry query doesnt exist, print error
  match = {"Industry" : {"$regex" : ".*"+industry+".*"}}
  if (collection.find(match).count() == 0):
    print("No Matches Found For:")
    print(dumps(match))
  #else send variables to aggregation function
  else: 
    myReadResult = aggregate(aggregationQ)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)       
