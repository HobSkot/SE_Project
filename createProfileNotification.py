import json

def remindProfileNotification(username):
  with open('profiles.json') as f:
    datadump = json.load(f)
  if username not in datadump['userProfiles']:
    print("Don't forget to create a profile")
  return
  
  
    
