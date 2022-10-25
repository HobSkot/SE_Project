#    - User is able to view their own profile 
#    - When displayed:
#        - their name will be automatically be displayed at the top of the profile information
#        - number of their friends should not be displayed on the profile. 

import json

#A copy and paste from viewProfiles.py
def viewProfile(username):
  with open('profiles.json') as userProfilesJson:
            profiles2 = json.load(userProfilesJson)
            if username in profiles2['userProfiles']:
              friendProfile = profiles2['userProfiles'][username]
              print("=====Here is your profile=====\n")
              print("Name: " + username + "\n")
              print("Title: " + friendProfile['title'] + "\nMajor: " + friendProfile['major'] + "\nUniversity: " + friendProfile['uni'] + "\nAbout Me: " + friendProfile['inform'])
              if (friendProfile['experience']["job1"]['title']) != None:
                print("\nJob 1: " + friendProfile['experience']["job1"]['title'] + "\nEmployer: " + friendProfile['experience']["job1"]['employer'] + "\nStart Date: " + friendProfile['experience']["job1"]['startDate'] + "\nEnd Date: " + friendProfile['experience']["job1"]['endDate'] + "\nLocation: " + friendProfile['experience']["job1"]['location'] + "\nJob Description: " + friendProfile['experience']["job1"]['jobDescription'] + "\n")
              if (friendProfile['experience']["job2"]['title']) != None:
                print("\nJob 2: " + friendProfile['experience']["job2"]['title'] + "\nEmployer: " + friendProfile['experience']["job2"]['employer'] + "\nStart Date: " + friendProfile['experience']["job2"]['startDate'] + "\nEnd Date: " + friendProfile['experience']["job2"]['endDate'] + "\nLocation: " + friendProfile['experience']["job2"]['location'] + "\nJob Description: " + friendProfile['experience']["job2"]['jobDescription'] + "\n")
              if (friendProfile['experience']["job3"]['title']) != None:
                print("\nJob 3: " + friendProfile['experience']["job3"]['title'] + "\nEmployer: " + friendProfile['experience']["job3"]['employer'] + "\nStart Date: " + friendProfile['experience']["job3"]['startDate'] + "\nEnd Date: " + friendProfile['experience']["job3"]['endDate'] + "\nLocation: " + friendProfile['experience']["job3"]['location'] + "\nJob Description: " + friendProfile['experience']["job3"]['jobDescription'] + "\n")
                return 0