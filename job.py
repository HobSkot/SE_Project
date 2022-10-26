import json, homepage 

def job (username, log_in):
  choice = 1
  while (choice > 0 and choice < 6):
    PrintListOfTitles()
    choice = int(input("[1]: Post a job\n[2]: Details of the job\n[3]: Delete a job\n[4]: Apply for a job\n[5]: Return to homepage\n"))
    if (choice == 1):
      PostJob(username, log_in)
    elif(choice == 2):
      JobDetails()
    elif (choice == 3):
      DeleteJob(username)
    elif (choice == 4):
      ApplyJob(username)
    elif (choice == 5):
      return
    else:
      print("Invalid Input! Try Again\n\n")
      
    
def PostJob(username, log_in):
  choice4 = 1

  while (choice4 > 0 and choice4 < 3):
    choice4 = int(input("1: Post a job\n2: Return to previous page\n"))
    if (choice4 == 1): 
      with open('jobs.json') as f:
        data = json.load(f)
        for item in data['jobPostings']:
          if len(data['jobPostings']) > 10:
            print("No more than 10 jobs may be posted, please come back later.")
            return 1
          else:
            Title = input("Create a Job title: ")
            Description = input("Create a Description: ")
            Employer = input("List the Employer: ")
            Location = input("List the job Location: ")
            Salary = input("List the Salary: ")
            print("\n")
            PostedBy = username
            
            tempDict = {"Title":Title, "Description":Description, "Employer":Employer, "Location":Location, "Salary":Salary,"PostedBy":PostedBy} 
            data['jobPostings'].append(tempDict)

            with open('jobs.json', "w") as f:
              json.dump(data, f)
            return 0
              
    #WIP Code for deletion functionality
    #if (choice4 == 2):
      #with open('jobs.json') as f:
        #data = json.load(f)
        #for item in data['jobPostings']:
          #if (data['Poster'] == username):
            #print("Here are your current job postings: \n")
            
       
    if (choice4 == 2):
        return
    # else:
    #   print("Please enter 1 or 2\n")




def PrintListOfTitles():
  with open('jobs.json') as f:
    data = json.load(f)
    if (len(data['jobPostings']) == 0):
      print("There are no job available currently\n\n")
    else :
      print("List of job titles available\n\n")
      i = 1
      for item in data['jobPostings']:
        print("{" + str(i) + "}\t" + item["Title"])
        i += 1
      print("\n")
      
def JobDetails():
  
  with open('jobs.json') as f:
    data = json.load(f)
    size = len(data['jobPostings'])
    if (size == 0):
      print("There are no job available currently\n\n")
    else :
      index = 1
      while (index > 0 and index < size+1):
        index = int(input("Which job are you interested? (1-" + str(size) + ")\n"))
        if (index < 1 or index > size):
          print("Invalid Input! Please only enter (1-" + str(size) + ")\n\n")
          index = 1
          continue
        else:
          print("Title: " + data['jobPostings'][index-1]['Title'] )
          print("Description: " + data['jobPostings'][index-1]['Description'] )
          print("Employer: " + data['jobPostings'][index-1]['Employer'] )
          print("Location: " + data['jobPostings'][index-1]['Location'] )
          print("Salary: " + data['jobPostings'][index-1]['Salary'] + "\n\n")
          return
        
def DeleteJob(username):
  print("Under Construction\n")


def ApplyJob(username):
  print("Under Construction\n")



        
      