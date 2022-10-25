import json, homepage

#send request funtion
def send_request(reciver, username):
    #open the students info file
    with open ('students.json') as fp:
        request = json.load(fp)

    request_name = request["studentsLogin"]
    #if find user name, then save their first name and last name for friend request message
    for i in request_name:
        if i['username'] == username:
            sender_first = i['first']
            sender_last = i['last']

    #store the info into request file
    with open ('friendsRequest.json') as f:
      data = json.load(f)
      tempInfo = {'reciver':reciver ,'senderFirst': sender_first, 'senderLast': sender_last, 'sender': username}
    data['request'].append(tempInfo)

    
    with open('friendsRequest.json', "w") as f:
        json.dump(data, f)



    return

#show the friend request on homepage
def show_request(reciver):
    boolNum = False
    with open('friendsRequest.json') as fp:
        request = json.load(fp)
#find if the user has any friend request
    for i in request['request']:
      #if yes, then ask user if they want to add friend
        if i['reciver'] == reciver:
            print("======You have a friend request=====")
            print("The user " + i['senderFirst'] + ' ' + i['senderLast'] + ' ' +'want to add you as friend')
            reciver_choice = input("Would you like to add user as friend? Y/N")
            sender_user = i['sender']
#calling add friend function to add friend
            if reciver_choice.lower() == 'y':
                boolNum = add_friend(reciver, sender_user)
                if boolNum == True:
                    print("=====Friend added=====")
                with open ('friendsRequest.json') as ff:
                  fedRequest = json.load(ff)

                delRequest = fedRequest['request']
                j = 0
                while (delRequest[j].get('reciver') != reciver):
                    j += 1
                temReqst = delRequest[j]
                delRequest.pop(j)
                with open('friendsRequest.json', 'w') as pp:
                    json.dump(fedRequest, pp)
#if no, then delete the request message, so it doesn't show next time
            elif reciver_choice.lower() == 'n':
                print("=====Friend request ignored=====")
                with open ('friendsRequest.json') as ff:
                  fedRequest = json.load(ff)

                delRequest = fedRequest['request']
                j = 0
                while (delRequest[j].get('reciver') != reciver):
                    j += 1
                temReqst = delRequest[j]
                delRequest.pop(j)
                with open('friendsRequest.json', 'w') as pp:
                    json.dump(fedRequest, pp)

#add friend function
def add_friend(reciver, sender):
  i=0
  # Search for both username's info.
  with open('students.json') as tempFile:
    userBase = json.load(tempFile)
      
  # Find part of array where username exists and grab info to add to userFriends.json (FirstName) 
  while reciver != userBase['studentsLogin'][i]['username']:
     i += 1 
  tempFName1 = userBase['studentsLogin'][i]['first']
  
  i = 0
  # Now do same for sender.
  
  while sender != userBase['studentsLogin'][i]['username']:
    i += 1
  tempFName2 = userBase['studentsLogin'][i]['first']
  
  # Add to friendslist.
  
  with open('userFriends.json') as friend_json:
    friends_json = json.load(friend_json)
      # Dictionary containing keys that are usernames and values that are Arrays of friends.

  userAddFriend = friends_json['studentFriends'][reciver]  # Array of Reciever's friends
  friendAddUser = friends_json['studentFriends'][sender]  # Array of Sender's friends

    # FIN
  userAddFriend.append({'username':sender,'name':tempFName2})
  friendAddUser.append({'username':reciver,'name':tempFName1})

  with open('userFriends.json', 'w') as f:
        json.dump(friends_json, f)

  return True

















