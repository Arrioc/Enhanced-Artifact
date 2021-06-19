Here are the curls used in the API:

CREATE: (test documents for tickers JK & KM)
curl -H "Content-Type: application/json" -X POST -d '{"Ticker" : "JK","Profit Margin" : -0.075,"Institutional Ownership" : 0.003,"EPS growth past 5 years" : 0.242,"Total Debt/Equity" : 7.46,"Current Ratio" : 0.7,"Return on Assets" : -0.074,"Sector" : "Services","P/S" : 0.06,"Change from Open" : 0.0205,"Performance (YTD)" : -0.9353,"Performance (Week)" : -0.137,"Quick Ratio" : 0.7,"P/B" : 0.82,"EPS growth quarter over quarter" : 0.119,"Performance (Quarter)" : -0.767,"200-Day Simple Moving Average" : -0.7382,"Shares Outstanding" : 0.99,"52-Week High" : -0.9308,"P/Cash" : 1,"Change" : 0.0687,"Analyst Recom" : 3,"Volatility (Week)" : 0.0996,"Country" : "USA","Return on Equity" : 6.889,"50-Day Low" : 0.1318,"Price" : 2.49,"50-Day High" : -0.7658,"Return on Investment" : -0.011,"Shares Float" : 3.09,"Industry" : "Management Services","Beta" : -2.5,"Sales growth quarter over quarter" : 9.286,"Operating Margin" : -0.017,"EPS (ttm)" : -5.97,"52-Week Low" : 0.1318,"Average True Range" : 0.37,"Company" : "Jessicus Kilbourneous Inc.","Gap" : 0.0472,"Relative Volume" : 3.24,"Volatility (Month)" : 0.0714,"Market Cap" : 2.3,"Volume" : 46666,"Gross Margin" : 0.292,"Performance (Half Year)" : -0.7376,"Relative Strength Index (14)" : 22.46,"Insider Ownership" : 0.071,"20-Day Simple Moving Average" : -0.4444,"Performance (Month)" : -0.6331,"LT Debt/Equity" : 4.11,"Average Volume" : 15.83,"EPS growth this year" : 0.791,"50-Day Simple Moving Average" : -0.589}' http://localhost:8080/stocks/api/v1.0/createStock/ 
curl -H "Content-Type: application/json" -X POST -d '{"Ticker" : "KM","Profit Margin" : -0.077,"Institutional Ownership" : 0.007,"EPS growth past 5 years" : 0.777,"Total Debt/Equity" : 7.70,"Current Ratio" : 0.7,"Return on Assets" : -0.077,"Sector" : "Services","P/S" : 0.07,"Change from Open" : 0.0707,"Performance (YTD)" : -0.7777,"Performance (Week)" : -0.177,"Quick Ratio" : 0.7,"P/B" : 0.77,"EPS growth quarter over quarter" : 0.177,"Performance (Quarter)" : -0.777,"200-Day Simple Moving Average" : -0.7777,"Shares Outstanding" : 0.97,"52-Week High" : -0.7777,"P/Cash" : 1,"Change" : 0.0777,"Analyst Recom" : 3,"Volatility (Week)" : 0.0977,"Country" : "USA","Return on Equity" : 7.777,"50-Day Low" : 0.1777,"Price" : 2.77,"50-Day High" : -0.7777,"Return on Investment" : -0.017,"Shares Float" : 3.07,"Industry" : "Management Services","Beta" : -2.7,"Sales growth quarter over quarter" : 9.277,"Operating Margin" : -0.017,"EPS (ttm)" : -5.77,"52-Week Low" : 0.1277,"Average True Range" : 0.37,"Company" : "Kitty Mittens Group","Gap" : 0.0477,"Relative Volume" : 3.77,"Volatility (Month)" : 0.0777,"Market Cap" : 2.3,"Volume" : 77777,"Gross Margin" : 0.377,"Performance (Half Year)" : -0.7777,"Relative Strength Index (14)" : 27.77,"Insider Ownership" : 0.077,"20-Day Simple Moving Average" : -0.4777,"Performance (Month)" : -0.6777,"LT Debt/Equity" : 4.77,"Average Volume" : 15.77,"EPS growth this year" : 0.777,"50-Day Simple Moving Average" : -0.777}' http://localhost:8080/stocks/api/v1.0/createStock/

    
READ:
curl -H "Content-Type: application/json" -X GET -d '{"Ticker" : "JK"}' http://localhost:8080/stocks/api/v1.0/getStock    
curl -H "Content-Type: application/json" -X GET -d '{"Ticker" : "KM"}' http://localhost:8080/stocks/api/v1.0/getStock  

    
UPDATE: change numerical value on JK
curl -H "Content-Type: application/json" -X PUT -d '{"key-value" : {"Volume" : 77777}}' http://localhost:8080/stocks/api/v1.0/updateStock?ticker="JK"
#UPDATE: change string value on KM
curl -H "Content-Type: application/json" -X PUT -d '{"key-value" : {"Company" : "Kitteny Mittenies"}}' http://localhost:8080/stocks/api/v1.0/updateStock?ticker="KM"  
    
UPDATE: Add new key (value = string)
curl -H "Content-Type: application/json" -X PUT -d '{"key-value" : {"New Key" : "New Value"}}' http://localhost:8080/stocks/api/v1.0/updateStock?ticker="JK"
UPDATE: Add new key (value = number)
curl -H "Content-Type: application/json" -X PUT -d '{"key-value" : {"Mittens" : 7}}' http://localhost:8080/stocks/api/v1.0/updateStock?ticker="KM"

    
DELETE: Ticker docs JK and KM
curl -H "Content-Type: application/json" -X DELETE -d '{"Ticker" : "JK"}' http://localhost:8080/stocks/api/v1.0/deleteStock
curl -H "Content-Type: application/json" -X DELETE -d '{"Ticker" : "KM"}' http://localhost:8080/stocks/api/v1.0/deleteStock    
    

DELETEFEILD: Ticker docs JK and KM
curl -H "Content-Type: application/json" -X PUT -d '{"key" : {"New Key" : ""}}' http://localhost:8080/stocks/api/v1.0/delField?ticker="JK"
curl -H "Content-Type: application/json" -X PUT -d '{"Key" : {"Mittens" : ""}}' http://localhost:8080/stocks/api/v1.0/delField?ticker="KM"    
    
    
STOCKREPORT:
curl -H "Content-Type: application/json" -X POST -d '{"array" : ["AA", "BA", "T"]}' http://localhost:8080/stocks/api/v1.0/stockReport
    

INDUSTRYREPORT:
curl -H "Content-Type: application/json" -X GET -d '{"Industry" : "Telecom"}' http://localhost:8080/stocks/api/v1.0/industryReport
    
    
INDUSTRYREPORT for file 'not' found: 
curl -H "Content-Type: application/json" -X GET -d '{"Industry" : "tetecom"}' http://localhost:8080/stocks/api/v1.0/industryReport


