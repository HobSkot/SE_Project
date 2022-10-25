# - Users are able to view friend's profile (only friend's profile is viewable by the user)
#        => Displaying a list of friends
#        => User get to select the "profile"option that is by a friend's name.
#        => If the friend does not have their profile created,  the profile option will not be displayed by that friend's name.
#    - User is able to view their own profile 
#    - When displayed:
#        - their name will be automatically be displayed at the top of the profile information
#        - number of their friends should not be displayed on the profile. 

import json

def viewFriendProfile(username):

  option = 1
  
  with open('userFriends.json') as profileJson:
    profiles = json.load(profileJson)
    if username in profiles['studentFriends']:
      selectedProfile = profiles['studentFriends'][username]
    else:
      print("user not found, redirecting to homepage...")
      return

    print("Your current friends: ")
    k = 1
    if len(selectedProfile) > 0:
      for i in selectedProfile:
        print("[" + str(k) + "]" + " Name: " + i['name'] + " Username: " + i['username'])
        k += 1
    else:
      print("You currently have no friends.\n")
      print("Redirecting to Homepage...\n")
      return
    option == input("Which friend's profile would you like to view?(Type 0 to return to the Homepage): ")
    if option >= 0:
      if option == 0:
        print("Returning to Homepage...\n")
        return
      else:
        friendName = selectedProfile[int(option)]['username']
        try:
          with open('profiles.json') as userProfilesJson:
            profiles2 = json.load(userProfilesJson)
            if friendName in profiles2['userProfiles']:
              friendProfile = profiles2['userProfiles'][friendName]
              #if friendProfile != None: #I'm trying to fix the bug but im tired.
              #  print("This user has no profile.\n")
              #  return
              print("Title: " + friendProfile['title'] + "\nMajor: " + friendProfile['major'] + "\nUniversity: " + friendProfile['uni'] + "\nAbout Me: " + friendProfile['inform'])
              if friendProfile['experience']["job1"]['title'] != None:
                print("\nJob 1: " + friendProfile['experience']["job1"]['title'] + "\nEmployer: " + friendProfile['experience']["job1"]['employer'] + "\nStart Date: " + friendProfile['experience']["job1"]['startDate'] + "\nEnd Date: " + friendProfile['experience']["job1"]['endDate'] + "\nLocation: " + friendProfile['experience']["job1"]['location'] + "\nJob Description: " + friendProfile['experience']["job1"]['jobDescription'] + "\n")
              if friendProfile['experience']["job2"]['title'] != None:
                print("\nJob 2: " + friendProfile['experience']["job2"]['title'] + "\nEmployer: " + friendProfile['experience']["job2"]['employer'] + "\nStart Date: " + friendProfile['experience']["job2"]['startDate'] + "\nEnd Date: " + friendProfile['experience']["job2"]['endDate'] + "\nLocation: " + friendProfile['experience']["job2"]['location'] + "\nJob Description: " + friendProfile['experience']["job2"]['jobDescription'] + "\n")
              if friendProfile['experience']["job3"]['title'] != None:
                print("\nJob 3: " + friendProfile['experience']["job3"]['title'] + "\nEmployer: " + friendProfile['experience']["job3"]['employer'] + "\nStart Date: " + friendProfile['experience']["job3"]['startDate'] + "\nEnd Date: " + friendProfile['experience']["job3"]['endDate'] + "\nLocation: " + friendProfile['experience']["job3"]['location'] + "\nJob Description: " + friendProfile['experience']["job3"]['jobDescription'] + "\n")
        except:
          print("Incorrect Input, or your friend does not have a profile yet. Please try again.")
          
          

    
      