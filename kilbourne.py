import os

# This method provides an initial menu that 
# allows the user to chose between internal 
# and web based services.

def main_menu():
  reply = True
  print('Welcome to Kilbourne Financial\'s Stock Market Services. \nPlease select from the following:')
  #let user chooses from two types of services
  while reply:
    print("""
    1 Internal services
    2 Web services
    3 Exit """)
        
    reply = raw_input()

    if (reply == '1'):
      print("You chose internal services")
      internal()
    elif (reply == '2'):
      print("You chose web services")
      webService()
    elif (reply == '3'):
      print('Goodbye, have a great day!') 
      reply = False
    else:
      print('Does not compute! Try agian.')

# This method provides services through the internal service
# by taking a selection from the user and then executing 
# the chosen module. When finished we return to the main menu
      
def internal():
  select = True
  print('Welcome to internal services. \nPlease choose from the following:')
  #let user chose from different internal services
  while select:
    print("""
    1 Create a new stock document
    2 Update a document
    3 Delete a document
    4 Delete a document's field
    5 Find a document
    6 Report on 50-Day Simple Moving Average
    7 Get an industry's ticker symbol list
    8 Report on a sector's total oustanding shares
    9 Exit to main menu
    """)
    
    select = raw_input()

    if (select == '1'):
      print("You chose create a stock document")
      from stocks_create import create_main
    elif (select == '2'):
      print("You chose update document")
      from stocks_update import modify_main
    elif (select == '3'):
      print("You chose delete doument")
      from stocks_delete import delete_main
    elif (select == '4'):
      print("You chose delete document field")
      from stocks_deleteField import del_field_main
    elif (select == '5'):
      print("You chose find document")
      from stocks_read import read_main
    elif (select == '6'):
      print("You chose report 50-Day SMA")
      from stocks_read1 import read1_main
    elif (select == '7'):
      print("You chose Get industry ticker list")
      from stocks_read2 import read2_main
    elif (select == '8'):
      print("You chose report on a sector's total oustanding shares")
      from stocks_read3 import read3_main
    elif (select == '9'):
      print('Exiting') 
      select = False
    else:
      print('Does not compute! Try again')

# This method provides services through the web service
# by taking a selection from the user and then executing 
# the chosen module

def webService():
  
  select = True
  print('Welcome to internal services. \nPlease choose from the following:')
  #let user chose from different internal services
  while select:
    print("""
    1 Create a new stock document
    2 Update a document
    3 Delete a document
    4 Delete a document's field
    5 Find a document
    6 Find multiple documents
    7 Create industry report
    8 Exit to main menu
    """)
    
    select = raw_input()

    if (select == '1'):
      print("You chose create a stock document")
      os.system("python APIcreate.py")
    elif (select == '2'):
      print("You chose update document")
      os.system("python APIupdate.py")
    elif (select == '3'):
      print("You chose delete doument")
      os.system("python APIdelete.py")
    elif (select == '4'):
      print("You chose delete document field")
      os.system("python APIdeleteField.py")
    elif (select == '5'):
      print("You chose find document")
      os.system("python APIread.py")
    elif (select == '6'):
      print("You chose find multiple documents")
      os.system("python APIstockReport.py")
    elif (select == '7'):
      print("You chose create industry report")
      os.system("python APIindustryReport.py")
    elif (select == '8'):
      print('Exiting') 
      select = False
    else:
      print('Does not compute! Try agian.')
    

main_menu()