# THIS IS USED TO DEAL WITH HANDLING OF PROFILES

# Profile must be viewable - so print JSON of info.

# a title, a major, a university name, a paragraph with information about the 
# student, zero or more lines about their experience, and 1 or more lines about their education.
import json
from api_profiles_output import profilesOutputAPI
experienceIndex = {"1":"title", "2":"employer","3":"startDate","4":"endDate","5":"location","6":"jobDescription"} # used for selecting what part of job person wishes to edit. ... i just loveee hardcoding c:


# Returns 1 if yes, 0 if no.
def wishToEdit():
  answer = 3
  while answer != "1" or "2":
    answer = input("\nWould you like to edit this info?\n[1] Yes\n[2] No\n\n")
    # 2 false , 1 true
    if answer == "1":
      return 1
    elif answer =="2":
      return 0
    else:
      print("Invalid choice. Please type a valid answer.")

    
  

def edit_profile_menu(username):
  # When creating profile, 
  # create list of options to adjust
  
  options = 1
  with open('profiles.json') as profileJson:
    profiles = json.load(profileJson)
    if username in profiles['userProfiles']: # checking if user had bio information yet in profiles.json
      #print("key found")
      selectedProfile = profiles['userProfiles'][username] # Dictionary of selected user's profile information.
    else: #else create profile 
      #print("key created")
      profiles['userProfiles'][username] =  {"title": "", "major": "", "uni": "", "inform": "", "experience": {"job1": {"title": "", "employer": "", "startDate": "", "endDate": "", "location": "", "jobDescription": ""}, "job2": {"title": "", "employer": "", "startDate": "", "endDate": "", "location": "", "jobDescription": ""}, "job3": {"title": "", "employer": "", "startDate": "", "endDate": "", "location": "", "jobDescription": ""}}, "education": {"schoolName": "", "degree": "", "years": ""}}
      selectedProfile = profiles['userProfiles'][username]
      #print(profiles)
  print("*****************PROFILE MENU*****************")  
  while options != "0":
    # Title
    options = input("[1] Title\n[2] Major\n[3] University Name\n[4] Information\n[5] Experience\n[6] Education\n[0] Back to previous page\n\n")
    if options == "1":
      # Access JSON of their profile -- TITLE
      print("Current Title: " + selectedProfile['title'])
      if(wishToEdit() == 1): # if returns true, (1 == yes, i wish to edit)
        selectedProfile['title'] = input("Please enter new Title: ")

    elif options == "2": # major
      print("Current Major: " + selectedProfile['major'])
      if(wishToEdit() == 1): # if returns true, (1 == yes, i wish to edit)
        selectedProfile['major'] = input("Please enter new major.\n").title()
    
    elif options == "3": # uni
      print("Current University: " + selectedProfile['uni'])
      if(wishToEdit() == 1): # if returns true, (1 == yes, i wish to edit)
        selectedProfile['uni'] = input("Please enter new University.\n").title()
      
    elif options == "4": # inform
      print("Current About Section: " + selectedProfile['inform'])
      if(wishToEdit() == 1): # if returns true, (1 == yes, i wish to edit)
        selectedProfile['inform'] = input("Please enter new about description.\n")

    elif options == "5": # experience -- THE ERROR HANDLING IS VERY POOR but it works... for now.
        jobOption = input("Which job profile would you like to look at? [1] [2] [3], or type [0] to exit.\nChoice: ")
        if jobOption == "0":
          continue;
        elif jobOption == "1" or "2" or "3": # bad code practice, ikik
          chosenJob = selectedProfile['experience']["job"+jobOption] # selected job array 
          print("Job " + jobOption)
          j = 1
          for i in chosenJob:
            print("[" + str(j) + "] " + i.capitalize() + ": " + chosenJob[i])
            j += 1
          if(wishToEdit() == 1): # if returns true, (1 == yes, i wish to edit)
            
            selectedExperience = input("Select what you wish to edit via its number or [0] to return: ")
            while selectedExperience not in ["1","2","3","4","5","6","0"]: # ANOTHER BAD CODE PRACTICE BUT idk what the cleanest, best solution is -- feel free to edit.
              selectedExperience = input("Select what you wish to edit via its number or [0] to return: ")
              
            while selectedExperience != "0": # continually select SELECTED job's subData to edit.
              chosenJob[experienceIndex[selectedExperience]] = input("New description: ")
              selectedExperience = "temp"
              while selectedExperience not in ["1","2","3","4","5","6","0"]:
                selectedExperience = input("Select what you wish to edit via its number or [0] to return: ")
        else:
          print("Invalid option..\n")
       
    elif options == "6": # education
      chosenEducation = selectedProfile['education']
      j = 1
      for i in chosenEducation:
        print("[" + str(j) + "] " + i.capitalize() + ": " + chosenEducation[i])
        j+= 1
      selectChoice = input("\nSelect what you wish edit: ")
      while selectChoice != "0":
        if(selectChoice == "1"):
          chosenEducation['schoolName'] = input("Enter new school name: ")
        elif(selectChoice == "2"):
          chosenEducation['degree'] = input("Enter new degree: ")
        elif(selectChoice == "3"): 
          chosenEducation['years'] = input("Enter years worked: ")
        else:
          print("Invalid Choice.\n")
        selectChoice = input("\nSelect what you wish edit or type [0] to return: ")
      # print("Current Title: " + selectedProfile['title'])
      # if(wishToEdit() == 1): # if returns true, (1 == yes, i wish to edit)
      #   selectedProfile['title'] = input("Please enter new Title.")
      
    #Developers option
    elif options == "0":
     break;

    #Invalid option
    else:
      print("Invalid option\n")
  with open('profiles.json', "w") as f:
      json.dump(profiles, f)
  profilesOutputAPI()
  