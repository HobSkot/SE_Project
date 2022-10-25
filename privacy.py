


import json

def privacy(username) :
  email = "on"
  sms = "on"
  targetedAds = "on"

  
  choice  = int(input("[1]. Guest Controls\n[2]. Return\n"))
  while (choice < 1 or choice > 2) :
    choice = int(input("Invalid Input! Please Enter 1 for Guest Controls or 2 for Return to previous page"))
  if (choice == 2):
    return
  with open('userSetting.json') as f:
    data = json.load(f)
  while(True):
    choice = input("Do you want your Email feature turned on or off? (on/off): ")
    if (choice.lower() == "on"):
      email = "on"
      break
    elif (choice.lower() == "off"):
      email = "off"
      break
    else:
      print("Invalid Input! Please Try again.\n\n")
  while(True):
    choice = input("Do you want your SMS feature turned on or off? (on/off): ")
    if (choice.lower() == "on"):
      sms = "on"
      break
    elif (choice.lower() == "off"):
      sms = "off"
      break
    else:
      print("Invalid Input! Please Try again.\n\n")
  while(True):
    choice = input("Do you want your Targeted Advertising feature turned on or off? (on/off): ")
    if (choice.lower() == "on"):
      targetedAds = "on"
      break
    elif (choice.lower() == "off"):
      targetedAds = "off"
      break
    else:
      print("Invalid Input! Please Try again.\n\n")  
  for elem in data['userSetting']:
    if (elem['username'] == username):
      del elem['email']
      del elem['sms']
      del elem['targetedAds']
      elem['email'] = email
      elem['sms'] = sms
      elem['targetedAds'] = targetedAds
        
  with open('userSetting.json', 'w') as f:
    json.dump(data, f)
  
    
    

  
  
  
  