import json, homepage 


def PostJob(username, log_in):
  choice4 = 1

  while (choice4 > 0 and choice4 < 3):
    choice4 = int(input("1: Post a job\n2: Return to homepage\n"))
    if (choice4 == 1): 
      with open('jobs.json') as f:
        data = json.load(f)
        for item in data['jobPostings']:
          if len(data['jobPostings']) > 5:
            print("No more than 5 jobs may be posted, please come back later.")
            return 1
          else:
            Title = input("Create a Job title: ")
            Description = input("Create a Description: ")
            Employer = input("List the Employer: ")
            Location = input("List the job Location: ")
            Salary = input("List the Salary: ")
            Poster = username
            
            tempDict = {"Title":Title, "Description":Description, "Employer":Employer, "Location":Location, "Salary":Salary,"Poster":Poster} 
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
        homepage.homepage(username, log_in)
    # else:
    #   print("Please enter 1 or 2\n")

