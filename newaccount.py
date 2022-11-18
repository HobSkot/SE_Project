# This file is to create a new InCollege account

import verifi, json, time
from notifys import newUser


def newaccount(username, newPassword, first, last, university, major, member):

    with open('students.json') as f:
        data = json.load(f)
        for item in data['studentsLogin']: #going over each username
            if username == item['username']: #if username in system already
                print("Username already exists...")
                return 1
                #exit()
            if len(data['studentsLogin']) >= 11:
                print(
                    "All permitted accounts have been created, please come back later"
                )
                return 1
                #exit()
              

    boolNum = verifi.verifiPass(newPassword) 
  
  
  ###
    ### !!!! INSERT DEFAULT PRIVACY SETTINGS HERE. MAYBE VIA FUNCTION? DEFINITELY GRAB INPUT !!!! ###
  ###

  
    while (boolNum != 0): # if invalid password, try again.
      print("Try again.\n")
      newPassword = input("Please create a strong password: ")
      boolNum = verifi.verifiPass(newPassword)
      
    tempDict = {"username":username.lower(),"password":newPassword,"first":first.lower(), "last":last.lower(), "university":university.lower(), "major":major.lower(), "Membership":member.lower(), "lastApplyDate": int(time.time())}
    data['studentsLogin'].append(tempDict) # add new Info to database 
    
    with open('userSetting.json') as f:
      setting = json.load(f)
    
    tempDict = {"username": username.lower(), "email": "on", "sms": "on", "targetedAds": "on", "language": "eng"}
    setting['userSetting'].append(tempDict)
    print("bakak")
    with open('userFriends.json') as fp:    
      friend = json.load(fp)
      
    #tempfriend = {"username": username.lower(), "Friends":[]}
    #tempfriend = {"username":username.lower(), "Friends":[]}
    friend['studentFriends'][username.lower()] = []
    
    # Next 3 lines of code add empty Notification box to studentNotification.json
    with open('studentNotification.json') as fpw:
      notificationData = json.load(fpw)
    notificationData['studentNotifications'][username.lower()] = []
    tempinfo = {"username": username.lower(), "newJob":" ", "newUser": " "}
    notificationData['newNotify'].append(tempinfo)

    with open('students.json', "w") as f:
        json.dump(data, f)

    with open('userSetting.json', "w") as f:
        json.dump(setting, f)

    with open('userFriends.json', "w") as fp:
        json.dump(friend, fp)
    with open('studentNotification.json', "w") as fpw:
        json.dump(notificationData, fpw)

    newUser(first, last)

    return 0


