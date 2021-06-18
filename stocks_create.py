import json
from bson import json_util, errors
from bson.json_util import dumps, loads
from pymongo import MongoClient, errors

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# This method returns 'true' and a message for when 
# document creation was successful or will return an 
# error if it was not successful

def insert_doc(document):
  try:
    myInsertResult = collection.insert_one(document)
    print("Document created!")
    return True
  except errors.DuplicateKeyError as e:
    print("Duplicated key error")
    return False
  except errors.WriteError as we:
    print("MongoDB returned error message")
    return False
  except errors.WriteConcernError as wce:
    print("MongoDB returned error message")
    return False
  
#This method accepts user input, first it checks
# a given ticker for duplicate key errors, then
# it sends the document to the insert function
  
def create_main():

  print('Please enter capitolized Ticker name')
  dict = {}
  #take ticker value & create new doc
  try:
    ticker = (raw_input())
    #format data
    newTicker = "{\"Ticker\" : \""+ticker+"\"}"
    newDoc = loads(newTicker)
  #check for duplicate
  except errors.DuplicateKeyError as e:
    print("Duplicated key error")
    return False  
  dict.update(newDoc)
  
  print('Please enter Profit Margin')
  profit = (raw_input())
  newProfit = "{\"Profit Margin\" : \""+profit+"\"}" 
  newDoc2 = loads(newProfit)
  dict.update(newDoc2)
  
  print('Please enter Institutional Ownership')
  ownership = (raw_input())
  newOwnership = "{\"Institutional Ownership\" : \""+ownership+"\"}" 
  newDoc3 = loads(newOwnership)
  dict.update(newDoc3)

  print('Please enter EPS growth past 5 years')
  epsGro5yr = (raw_input())
  newEpsGro5yr = "{\"EPS growth past 5 years\" : \""+epsGro5yr+"\"}" 
  newDoc4 = loads(newEpsGro5yr)
  dict.update(newDoc4)
  
  print('Please enter Total Debt/Equity')
  totDebtEq = (raw_input())
  newtotDebtEq = "{\"Total Debt/Equity\" : \""+totDebtEq+"\"}" 
  newDoc5 = loads(newtotDebtEq)
  dict.update(newDoc5)
  
  print('Please enter Current Ratio')
  curRatio = (raw_input())
  newCurRatio = "{\"Current Ratio\" : \""+curRatio+"\"}" 
  newDoc6 = loads(newCurRatio)
  dict.update(newDoc6)

  print('Please enter Return on Assets')
  rOnA = (raw_input())
  newRonA = "{\"Return on Assets\" : \""+rOnA+"\"}" 
  newDoc7 = loads(newRonA)
  dict.update(newDoc7)  
  
  print('Please enter Sector')
  sector = (raw_input())
  newSector = "{\"Sector\" : \""+sector+"\"}" 
  newDoc8 = loads(newSector)
  dict.update(newDoc8)
  
  print('Please enter P/S')
  ps = (raw_input())
  newPs = "{\"P/S\" : \""+ps+"\"}"
  newDoc9 = loads(newPs)
  dict.update(newDoc9)
  
  print('Please enter Change from Open')
  changeFrOpen = (raw_input())
  newChangeFrOpen = "{\"Change from Open\" : \""+changeFrOpen+"\"}" 
  newDoc10 = loads(newChangeFrOpen)
  dict.update(newDoc10)
  
  print('Please enter Performance (YTD)')
  perfYTD = (raw_input())
  newPerfYTD = "{\"Performance (YTD)\" : \""+perfYTD+"\"}" 
  newDoc11 = loads(newPerfYTD)
  dict.update(newDoc11)
  
  print('Please enter Performance (Week)')
  perfW = (raw_input())
  newPerfW = "{\"Performance (Week)\" : \""+perfW+"\"}" 
  newDoc12 = loads(newPerfW)
  dict.update(newDoc12)
  
  print('Please enter Quick Ratio')
  qRatio = (raw_input())
  newQRatio = "{\"Quick Ratio\" : \""+qRatio+"\"}" 
  newDoc13 = loads(newQRatio)
  dict.update(newDoc13)
  
  print('Please enter P/B')
  pb = (raw_input())
  newPB = "{\"P/B\" : \""+pb+"\"}"
  newDoc14 = loads(newPB)
  dict.update(newDoc14)
  
  print('Please enter EPS growth quarter over quarter')
  epsGroQ = (raw_input())
  newEpsGroQ = "{\"EPS growth quarter over quarter\" : \""+epsGroQ+"\"}" 
  newDoc15 = loads(newEpsGroQ)
  dict.update(newDoc15)
  
  print('Please enter Performance (Quarter)')
  perfQ = (raw_input())
  newPerfQ = "{\"Performance (Quarter)\" : \""+perfQ+"\"}" 
  newDoc16 = loads(newPerfQ)
  dict.update(newDoc16)
  
  print('Please enter 200-Day Simple Moving Average')
  d200SMA = (raw_input())
  newD200SMA = "{\"200-Day Simple Moving Average\" : \""+d200SMA+"\"}" 
  newDoc17 = loads(newD200SMA)
  dict.update(newDoc17)
  
  print('Please enter Shares Outstanding')
  sharesOut = (raw_input())
  newSharesOut = "{\"Shares Outstanding\" : \""+sharesOut+"\"}" 
  newDoc18 = loads(newSharesOut)
  dict.update(newDoc18)
  
  print('Please enter 52-Week High')
  w52h = (raw_input())
  newW52h = "{\"52-Week High\" : \""+w52h+"\"}" 
  newDoc19 = loads(newW52h)
  dict.update(newDoc19)
  
  print('Please enter P/Cash')
  pCash = (raw_input())
  newPCash = "{\"P/Cash\" : \""+pCash+"\"}" 
  newDoc20 = loads(newPCash)
  dict.update(newDoc20)
  
  print('Please enter Change')
  change = (raw_input())
  newChange = "{\"Change\" : \""+change+"\"}" 
  newDoc21 = loads(newChange)
  dict.update(newDoc21)
  
  print('Please enter Analyst Recom')
  anaRec = (raw_input())
  newAnaRec = "{\"Analyst Recom\" : \""+anaRec+"\"}" 
  newDoc22 = loads(newAnaRec)
  dict.update(newDoc22)
  
  print('Please enter Volatility (Week)')
  volW = (raw_input())
  newVolW = "{\"Volatility (Week)\" : \""+volW+"\"}" 
  newDoc23 = loads(newVolW)
  dict.update(newDoc23)
  
  print('Please enter Country')
  country = (raw_input())
  newCountry = "{\"Country\" : \""+country+"\"}" 
  newDoc24 = loads(newCountry)
  dict.update(newDoc24)
  
  print('Please enter Return on Equity')
  returnEq = (raw_input())
  newReturnEq = "{\"Return on Equity\" : \""+returnEq+"\"}" 
  newDoc25 = loads(newReturnEq)
  dict.update(newDoc25)
  
  print('Please enter 50-Day Low')
  d50l = (raw_input())
  newD50l = "{\"50-Day Low\" : \""+d50l+"\"}" 
  newDoc26 = loads(newD50l)
  dict.update(newDoc26)
  
  print('Please enter Price')
  price = (raw_input())
  newPrice = "{\"Price\" : \""+price+"\"}" 
  newDoc27 = loads(newPrice)
  dict.update(newDoc27)
  
  print('Please enter 50-Day High')
  d50h = (raw_input())
  newD50h = "{\"50-Day High\" : \""+d50h+"\"}" 
  newDoc28 = loads(newD50h)
  dict.update(newDoc28)
  
  print('Please enter Return on Investment')
  returnOnInv = (raw_input())
  newReturnOnInv = "{\"Return on Investment\" : \""+returnOnInv+"\"}" 
  newDoc29 = loads(newReturnOnInv)
  dict.update(newDoc29)
  
  print('Please enter Shares Float')
  shareFloat = (raw_input())
  newShareFloat = "{\"Shares Float\" : \""+shareFloat+"\"}" 
  newDoc30 = loads(newShareFloat)
  dict.update(newDoc30)
  
  print('Please enter Industry')
  industry = (raw_input())
  newIndustry = "{\"Industry\" : \""+industry+"\"}" 
  newDoc31 = loads(newIndustry)
  dict.update(newDoc31)
  
  print('Please enter Beta')
  beta = (raw_input())
  newBeta = "{\"Beta\" : \""+beta+"\"}"
  newDoc32 = loads(newBeta)
  dict.update(newDoc32)    
  
  print('Please enter Sales growth quarter over quarter')
  salesGroQ = (raw_input())
  newSalesGroQ = "{\"Sales growth quarter over quarter\" : \""+salesGroQ+"\"}"
  newDoc33 = loads(newSalesGroQ)
  dict.update(newDoc33)
  
  print('Please enter Operating Margin')
  opMarg = (raw_input())
  newOpMarg = "{\"Operating Margin\" : \""+opMarg+"\"}"
  newDoc34 = loads(newOpMarg)
  dict.update(newDoc34)
  
  print('Please enter EPS (ttm)')
  epsTtm = (raw_input())
  newEpsTtm = "{\"EPS (ttm)\" : \""+epsTtm+"\"}"
  newDoc35 = loads(newEpsTtm)
  dict.update(newDoc35)
  
  print('Please enter 52-Week Low')
  w52l = (raw_input())
  newW52l = "{\"52-Week Low\" : \""+w52l+"\"}"
  newDoc36 = loads(newW52l)
  dict.update(newDoc36)
  
  print('Please enter Average True Range')
  avTruRange = (raw_input())
  newAvTruRange = "{\"Average True Range\" : \""+avTruRange+"\"}"
  newDoc37 = loads(newAvTruRange)
  dict.update(newDoc37)
  
  print('Please enter Company')
  company = (raw_input())
  newCompany = "{\"Company\" : \""+company+"\"}"
  newDoc38 = loads(newCompany)
  dict.update(newDoc38)
  
  print('Please enter Gap')
  gap = (raw_input())
  newGap = "{\"Gap\" : \""+gap+"\"}"
  newDoc39 = loads(newGap)
  dict.update(newDoc39)
  
  print('Please enter Relative Volume')
  relVol = (raw_input())
  newRelVol = "{\"Relative Volume\" : \""+relVol+"\"}"
  newDoc40 = loads(newRelVol)
  dict.update(newDoc40)
  
  print('Please enter Volatility (Month)')
  volM = (raw_input())
  newVolM = "{\"Volatility (Month)\" : \""+volM+"\"}"
  newDoc41 = loads(newVolM)
  dict.update(newDoc41)
  
  print('Please enter Market Cap')
  markCap = (raw_input())
  newMarkCap = "{\"Market Cap\" : \""+markCap+"\"}"
  newDoc42 = loads(newMarkCap)
  dict.update(newDoc42)
  
  print('Please enter Volume')
  volume = (raw_input())
  newVolume = "{\"Volume\" : \""+volume+"\"}"
  newDoc43 = loads(newVolume)
  dict.update(newDoc43)
  
  print('Please enter Gross Margin')
  grossMarg = (raw_input())
  newGrossMarg = "{\"Gross Margin\" : \""+grossMarg+"\"}"
  newDoc44 = loads(newGrossMarg)
  dict.update(newDoc44)
  
  print('Please enter Performance (Half Year)')
  perfHY = (raw_input())
  newPerfHY = "{\"Performance (Half Year)\" : \""+perfHY+"\"}"
  newDoc45 = loads(newPerfHY)
  dict.update(newDoc45)
  
  print('Please enter Relative Strength Index (14)')
  relStrIndx = (raw_input())
  newRelStrIndx = "{\"Relative Strength Index (14)\" : \""+relStrIndx+"\"}"
  newDoc46 = loads(newRelStrIndx)
  dict.update(newDoc46)
  
  print('Please enter Insider Ownership')
  insideOwnersh = (raw_input())
  newInsideOwnersh = "{\"Insider Ownership\" : \""+insideOwnersh+"\"}"
  newDoc47 = loads(newInsideOwnersh)
  dict.update(newDoc47)
  
  print('Please enter 20-Day Simple Moving Average')
  d20SMA = (raw_input())
  newD20SMA = "{\"20-Day Simple Moving Average\" : \""+d20SMA+"\"}"
  newDoc48 = loads(newD20SMA)
  dict.update(newDoc48)
  
  print('Please enter Performance (Month)')
  perfM = (raw_input())
  newPerfM = "{\"Performance (Month)\" : \""+perfM+"\"}"
  newDoc49 = loads(newPerfM)
  dict.update(newDoc49)
  
  print('Please enter LT Debt/Equity')
  ltDebtEq = (raw_input())
  newLtDebtEq = "{\"LT Debt/Equity\" : \""+ltDebtEq+"\"}"
  newDoc50 = loads(newLtDebtEq)
  dict.update(newDoc50)
  
  print('Please enter Average Volume')
  avVol = (raw_input())
  newAvVol = "{\"Average Volume\" : \""+avVol+"\"}"
  newDoc51 = loads(newAvVol)
  dict.update(newDoc51)
  
  print('Please enter EPS growth this year')
  epsGroTY = (raw_input())
  newEpsGroTY = "{\"EPS growth this year\" : \""+epsGroTY+"\"}"
  newDoc52 = loads(newEpsGroTY)
  dict.update(newDoc52)
  
  print('Please enter 50-Day Simple Moving Average')
  d50SMA = (raw_input())
  newD50SMA = "{\"50-Day Simple Moving Average\" : \""+d50SMA+"\"}"
  newDoc53 = loads(newD50SMA)
  dict.update(newDoc53)

  
  #send data to 'insert' function
  insertResult = insert_doc(dict)
  #write true if inserted, false if not
  print(insertResult)  

create_main()
