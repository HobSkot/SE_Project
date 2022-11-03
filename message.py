import json
# message function is the parent function to sendMessage function and friendList function
# purpose of this function: prompt the user for the action
def message(username): 
  choice = 1
  while (choice >= 0 and choice < 3):
    try: 
      choice = int(input("[1] Send a message\n[2] Generate a list of your friends\n[0]Return to previous page\n\n"))
    except ValueError:
      print("Input must be an integer. Try Again!\n")
      choice = 1
      continue

  
    if (choice == 1):
      receiver = input("Enter the username of the receiver: ")
      sendMessage(username, receiver)
    elif (choice == 2):
      friendsList(username)
    elif (choice == 0):
      return
    else:
      print("Invalid Input! Try Again.\n")
      choice = 1
      continue
# sendMessage is being called in message function
# purpose of this function: send message
def sendMessage(sender, receiver):
  
  with open('students.json') as f:
    students = json.load(f)
  with open('userFriends.json') as f:
    users = json.load(f)
  with open('inbox.json') as f:
    messages = json.load(f)
  if sender in users['studentFriends']:
    friends = users['studentFriends'][sender]
  # membership is a boolean variable (True for plus, False for standard)
  membership = checkMember(sender)
  # check if the receiver was a friend of sender
  check = False
  if (not membership):
    for friend in friends:
      if (friend['username'] == receiver):
        check = True
        break
    if (not check):
      print("You and ", receiver, " are not friend yet.\nDue to the limitation of your current membership, you are not allowed to send message to any InCollege users other than your InCollge friends.\n")
      return
  else:
    check = False
    for users in students['studentsLogin']:
      if (users['username'] == receiver):
        check = True
        break
    if (not check):
      print("The username of the person you are looking for does not exist.\n")
      return

  message = input("What do you want to tell them: ")
  tempDict = {"sender": sender, "receiver": receiver, "message": message, 'status': 'unread'}
  messages['messages'].append(tempDict)
  with open('inbox.json', "w") as f:
    json.dump(messages, f)

# friendsList function is being called in message function
# Purpose of the function: Generate a list of user's friends
def friendsList(username):
  with open('userFriends.json') as f:
        friends = json.load(f)
        friendArray = friends['studentFriends'][username]
  print("\n**********FRIENDS LIST**********")
  k = 1
  if len(friendArray) > 0:  # if friendArray is not empty
      for i in friendArray:  # print out friends of logged_in user.
          print("[" + str(k) + "]" + " " + i['name'])
          k += 1
      print("\n********** END OF THE LIST**********\n\n")
  else:
      print("\nUser has no friend on InCollege currently\n\n")
      return

# checkMember is being called in sendMessage function
# Purpose of this function: check if the user is plus member or standard member
def checkMember(sender):
    with open("students.json") as fp:
        checkMember = json.load(fp)

    for i in checkMember['studentsLogin']:
        if i['username'] == sender:
            if i['Membership'] == "plus":
              #return True if it's plus membership
              return True
            else:
              #return False if it's standard membership
              return False

# messageNotification function is being called at the very beginning of homepage.py
def messageNotification(username):
  with open('inbox.json') as f:
    messages = json.load(f)
  if len(messages['messages']) == 0:
    return
  num = -1
  for message in messages['messages']:
    num += 1
    if (message['receiver'] == username and message['status'] == 'unread'):
      print("\nYou have an unread message from ", message['sender'], "\nMessage: ", message['message'], "\n")
      choice = 'y'
      while (choice == 'y'):
        choice = input("Do you want to keep this message in your inbox? (y/n): ")
        message['status'] = "read"
        if (choice.lower() == 'n'):
          messages['messages'].pop(num)
        elif(choice.lower() != 'y' or choice.lower() != 'y'):
          print("Invalid Input! Try Again.\n\n")
          choice = 'y'
          continue
        with open('inbox.json', 'w') as f:
          json.dump(messages, f)
        break 
      choice = 'y'
      while (choice == 'y'):
        choice = input("Do you want to reply to this message? (y/n): ")
        if (choice.lower() == 'n'):
          break
        elif(choice.lower() == 'y'):
          sendMessage(username, message['sender'])
          break
        else:
          print("Invalid Input! Try Again.\n\n")
          choice = 'y'
          continue
    
          
        
        
      
      