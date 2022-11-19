import json, time

def studentAccountInputAPI():
  accounts = []
  with open('studentAccounts.txt') as f:
    while True:
      line1 = f.readline()
      if not line1:
          break
      strList = line1.split()
      line2 = f.readline().strip()
      f.readline()

      tempAcc = {"username": strList[0].lower(), "first": strList[1], "last": strList[2], "password": line2, "Membership": "standard", "university": "USF", "major": "cs", "lastApplyDate": int(time.time())}

      accounts.append(tempAcc)    
  if (len(accounts) == 0):
    return
  with open('students.json') as f:
    data = json.load(f)
      
    for account in accounts:
      check = True
      for item in data['studentsLogin']:
        if account['username'] == item['username']: 
          check = False
          break
      if (len(data['studentsLogin']) == 10):
        return
      if (not check):
        continue
      data['studentsLogin'].append(account)
      with open('students.json', "w") as f:
        json.dump(data, f)

  

      
      
        
        
  
  
  