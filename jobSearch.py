import datetime
import json



def job(username, log_in):
    JobRemovedNotification(username)
    choice = 1
    while (choice > 0 and choice < 11):
        PrintListOfTitles(username)
        choice = int(
            input(
                "[1]: Post a job\n[2]: Details of the job you interested in\n[3]: Delete a job\n[4]: Apply for a job\n[5]: List of applied job\n[6]: List of unapplied job\n[7]: Saving job posting for later\n[8]: List of saved jobs\n[9]: Remove a job from your job save list\n[10]: Return to homepage\n"
            ))
        if (choice == 1):
            PostJob(username, log_in)
        elif (choice == 2):
            JobDetails()
        elif (choice == 3):
            DeleteJob(username)
        elif (choice == 4):
            ApplyJob(username)
        elif (choice == 5):
            listOfAppliedJob(username)
        elif (choice == 6):
            listOfUnappliedJob(username)
        elif (choice == 7):
            JobSaving(username)
        elif (choice == 8):
            listOfSavedJobs(username)
        elif (choice == 9):
            RemovingSavedJob(username)
        elif (choice == 10):
          return  
        else:
            print("Invalid Input! Try Again\n\n")
            choice = 1


def PostJob(username, log_in):
  data ={}
  with open('jobs.json') as f:
        data = json.load(f)
  choice4 = 1
  while (choice4 > 0 and choice4 < 3):
    try:
      choice4 = int(input("1: Post a job\n2: Return to previous page\n"))
    except ValueError:
      print("Input must be an integer! Try Again.\n")
      choice4 = 1
      continue
      
    if (choice4 < 1 or choice4 > 2):
      print("Invalid Input! Try Again")
      choice4 = 1
      continue

      
    if (choice4 == 1): 
      if (len(data['jobPostings']) == 10):
        print("No more than 10 jobs may be posted, please come back later.\n\n")
        return
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
        return
  
    if (choice4 == 2):
        return

def PrintListOfTitles(username):
    data = {}
    application = {}
    with open('jobApplications.json') as f:
        application = json.load(f)
    with open('jobs.json') as f:
        data = json.load(f)
    if (len(data['jobPostings']) == 0):
        print("There are no job available currently\n\n")
    else:
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n" +
        "List of available job titles\n" +  "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n\n")
        i = 1
        printed = False
        for item in data['jobPostings']:
            for elem in application['jobApplications']:
                if (item['Title'] == elem['title']
                        and item['Employer'] == elem['employer']
                        and item['PostedBy'] == elem['postedBy']
                        and username == elem['applicant']):
                    print("{" + str(i) + "}\t" + item["Title"] + " (Applied)")
                    i += 1
                    printed = True
                    break
            if (not printed):
                print("{" + str(i) + "}\t" + item["Title"])
                i += 1
            else:
                printed = False

        print("\n")


def JobDetails():

    with open('jobs.json') as f:
        data = json.load(f)
        size = len(data['jobPostings'])
        if (size == 0):
            print("There are no job available currently\n\n")
        else:
            index = 1
            while (index > 0 and index < size + 1):
                try:
                    index = int(
                        input("Which job are you interested? (1-" + str(size) +
                              ")\n"))
                except ValueError:
                    print("Input must be an integer! Try Again.\n")
                    index = 1
                    continue
                if (index < 1 or index > size):
                    print("Invalid Input! Please only enter (1-" + str(size) +
                          ")\n\n")
                    index = 1
                    continue
                else:
                    print("Title: " + data['jobPostings'][index - 1]['Title'])
                    print("Description: " +
                          data['jobPostings'][index - 1]['Description'])
                    print("Employer: " +
                          data['jobPostings'][index - 1]['Employer'])
                    print("Location: " +
                          data['jobPostings'][index - 1]['Location'])
                    print("Salary: " +
                          data['jobPostings'][index - 1]['Salary'] + "\n\n")
                    return


def DeleteJob(username):
  data = {}
  application ={}
  savedJobs = {}
  with open('jobs.json') as f:
    data = json.load(f)
  with open('jobApplications.json') as f:
    application = json.load(f)
  with open('savedJobs.json') as f:
    savedJobs = json.load(f)

  arrayOfSavedJobs = savedJobs['savedJobs']
  arrayOfJobs = data['jobPostings']
  arrayOfApplications = application['jobApplications']
  
  size = len(arrayOfJobs)
  if (size == 0):
    print("No job posting currently. Come back later!\n\n")
    return 

  #Find the index of the job to be deleted  
  choice = 1
  while (choice>= 0 and choice < size+1):
    try:
      choice = int(input("Which job posting do you want to remove?(1-" + str(size) +") Enter 0 to return to previous page: "))
    except ValueError:
      print("\nInput must be an integer! Try Again\n")
      choice = 1
      continue
    if (choice < 0 or choice > size):
      print("\nInvalid input! Try Again\n")
      choice = 1
      continue
    if (choice == 0):
      return
    if (username != arrayOfJobs[choice-1]['PostedBy']):
      print("\nYou are not allowed to delete job postings posted by other users. Try again.\n")
      choice = 1
      continue
    break

  deletedJob = arrayOfJobs[choice-1]
  #remove the job from the jobs.json  
  arrayOfJobs.pop(choice-1)

  #change the status of the job from "open" to "closed"
  for item in arrayOfApplications:
    if (item['title'] == deletedJob['Title'] and item['employer'] == deletedJob['Employer'] and item['postedBy'] == deletedJob['PostedBy']):
      item['status'] = "closed"

  for item in arrayOfSavedJobs:
    if (item['title'] == deletedJob['Title'] and item['employer'] == deletedJob['Employer'] and item['postedBy'] == deletedJob['PostedBy']):
      item['status'] = "removed"
      
        
  with open('jobApplications.json', 'w') as f:
    json.dump(application, f)
  with open('jobs.json', 'w') as f:
    json.dump(data, f)
  with open('savedJobs.json', 'w') as f:
    json.dump(savedJobs, f)
      
    
    
    
      
      
   


def ApplyJob(username):
    data = {}
    application = {}

    with open('jobs.json') as f:
        data = json.load(f)
    with open('jobApplications.json') as f:
        application = json.load(f)

    size = len(data['jobPostings'])
    # Check if there is any job postings
    if (size == 0):
        print("Currently no job available. Please come back later.\n\n")
        return

    #The purpose of this while loop is to get the index of the job from the job.json
    index = 1
    while (index >= 0 and index < size + 1):

        try:
            index = int(
                input("Which job are you interested in? (1-" + str(size) +
                      "). Enter 0 to return to previous page otherwise\n"))
        except ValueError:
            print("Input must be an integer! Try again\n")
            index = 1
            continue
        # Validate the input
        if (index < 0 or index > size):
            print("Invalid Input! Please only enter (1-" + str(size) + ")\n\n")
            index = 1
            continue

        #return to previous page
        if (index == 0):
            return
        # Check if the applicant is the person who posted the job posting
        if (username == data['jobPostings'][index - 1]['PostedBy']):
            print(
                "Sorry, you are not allowed to apply to the job that you have posted\n\n"
            )
            continue
        break

    # the job object that we found from the job.json
    job = data['jobPostings'][index - 1]

    # this for loop intends to prevent the applicant to apply to the same job twice
    for item in application['jobApplications']:
        if (item['applicant'] == username and item['title'] == job['Title']
                and item['employer'] == job['Employer']
                and item['postedBy'] == job['PostedBy']):
            print(
                "You are not allowed to apply to the same job more than once.\nPlease come back later.\n\n"
            )
            return

    graduation = ""
    startingDate = ""
    while (True):
        try:
            print("Please enter your graduation date")
            day = int(input("Day: "))
            month = int(input("Month: "))
            year = int(input("Year: "))
            date_string = str(year) + "-" + str(month) + "-" + str(day)
            # giving the date format
            date_format = '%Y-%m-%d'
            # formatting the date using strptime() function
            dateObject = datetime.datetime.strptime(date_string, date_format)
            graduation = str(dateObject)
            break
        # If the date validation goes wrong
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue

    while (True):
        try:
            print("Please enter your a date you can start working")
            day = int(input("Day: "))
            month = int(input("Month: "))
            year = int(input("Year: "))
            date_string = str(year) + "-" + str(month) + "-" + str(day)
            # giving the date format
            date_format = '%Y-%m-%d'
            # formatting the date using strptime() function
            dateObject = datetime.datetime.strptime(date_string, date_format)
            startingDate = str(dateObject)
            break
        # If the date validation goes wrong
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue

    explainYourself = input(
        "Please enter a paragraph text explaining why you think you would be a good fit for this job.\n"
    )

    tempDict = {
        "applicant": username,
        "title": job['Title'],
        "employer": job['Employer'],
        "postedBy": job['PostedBy'],
        'explainYourself': explainYourself,
        "graduation date": graduation,
        "starting date": startingDate,
        "status": "open"
    }
    application['jobApplications'].append(tempDict)

    with open('jobApplications.json', "w") as f:
        json.dump(application, f)

def JobRemovedNotification(username):
  i = 0
  application = {}
  with open('jobApplications.json') as f:
    application = json.load(f)
  for item in application['jobApplications']:
    if (item['applicant'] == username and item['status'] == "closed"):
      print("The job that you applied to have been removed from the system.\nDetails of the job:\n\n")
      print("Job Title: " + item['title'] + "\nEmployer: " + item['employer'] + "\nPosted By: " + item['postedBy'] + "\n\n")
      application['jobApplications'].pop(i)
      break
    i+=1
  

  with open('jobApplications.json', 'w') as f:
    json.dump(application, f)

def listOfAppliedJob(username):
  application = {}
  with open('jobApplications.json') as f:
    application = json.load(f)
  arrayOfApplications = application['jobApplications']
  
  if (len(arrayOfApplications) == 0):
    print("User has not applied for any job yet\n\n")
    return
    
  check = False
  for item in arrayOfApplications: 
    if (item['applicant'] == username):
      check = True

  if (not check):
    print("User has not applied for any job yet\n\n")
    return

  i = 1
  print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" + "\nList of applied job titles\n" +"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n\n")
  for item in arrayOfApplications:
    if (item['applicant'] == username and item['status'] == 'open'):
      print("{" +str(i) + "} " + "Job Title: " + item['title'] + "\n\tEmployer: " + item['employer'] + "\n\tPosted By: " + item['postedBy'] + "\n")
      i += 1

def listOfUnappliedJob(username):
  data = {}
  application = {}
  with open('jobApplications.json') as f:
    application = json.load(f)
  with open('jobs.json') as f:
    data = json.load(f)

  arrayOfApplications = application['jobApplications']
  arrayOfJobs = data['jobPostings']
  copyOfJobsArray = arrayOfJobs.copy()

  if (len(arrayOfJobs) == 0):
    print("No job is available at the moment. Come back later\n\n")
    return
    

  for item in arrayOfApplications:
    if (item['applicant'] == username and item['status'] == 'open'):
      i = 0
      for job in copyOfJobsArray:
        if(job["Title"] == item['title'] and job["Employer"] == item['employer'] and job["PostedBy"] == item['postedBy']):
          copyOfJobsArray.pop(i)
        i += 1

  i = 1
  print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" + "\nList of Unapplied jobs\n" +"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n\n")
  for item in copyOfJobsArray:
    print("{" +str(i) + "} " + "Job Title: " + item['Title'] + "\n\tEmployer: " + item['Employer'] + "\n\tPosted By: " + item['PostedBy'] + "\n")
    i += 1      
def JobSaving(username):
  jobs = {}
  savedJobs = {}

  with open('jobs.json') as f:
      jobs = json.load(f)
  with open('savedJobs.json') as f:
      savedJobs = json.load(f)

  size = len(jobs['jobPostings'])
  # Check if there is any job postings
  if (size == 0):
      print("Currently no job available. Please come back later.\n\n")
      return

  #The purpose of this while loop is to get the index of the job from the job.json
  index = 1
  while (index >= 0 and index < size + 1):

      try:
          index = int(
              input("Which job do you want to save for later? (1-" + str(size) +
                    "). Enter 0 to return to previous page otherwise\n"))
      except ValueError:
          print("Input must be an integer! Try again\n")
          index = 1
          continue
      # Validate the input
      if (index < 0 or index > size):
          print("Invalid Input! Please only enter (1-" + str(size) + ")\n\n")
          index = 1
          continue

      #return to previous page
      if (index == 0):
          return
      # Check if the applicant is the person who posted the job posting
      if (username == jobs['jobPostings'][index - 1]['PostedBy']):
          print(
              "Sorry, you are not allowed to save the job that you have posted\n\n"
          )
          continue
      break

  # the job object that we found from the job.json
  job = jobs['jobPostings'][index - 1]

  # this for loop intends to prevent the applicant to apply to the same job twice
  for item in savedJobs['savedJobs']:
      if (item['username'] == username and item['title'] == job['Title']
              and item['employer'] == job['Employer']
              and item['postedBy'] == job['PostedBy']):
          print(
              "You are not allowed to save the same job more than once.\nPlease come back later.\n\n"
          )
          return

  tempDict = {
      "username": username,
      "title": job['Title'],
      "employer": job['Employer'],
      "postedBy": job['PostedBy'],
      "status": 'open'
  }
  savedJobs['savedJobs'].append(tempDict)

  with open('savedJobs.json', "w") as f:
      json.dump(savedJobs, f)
    

def listOfSavedJobs(username):
  data = {}
  with open('savedJobs.json') as f:
    data = json.load(f)

  arrayOfSavedJobs = data['savedJobs']
    
  if (len(arrayOfSavedJobs) == 0):
    print("User has not saved any job yet\n\n")
    return
    
  check = False
  for item in arrayOfSavedJobs: 
    if (item['username'] == username):
      check = True

  if (not check):
    print("User has not saved any job yet\n\n")
    return

  i = 1
  print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" + "\nList of Saved Jobs\n" +"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n\n")
  for item in arrayOfSavedJobs:
    if (item['username'] == username and item['status'] == 'open'):
      print("{" +str(i) + "} " + "Job Title: " + item['title'] + "\n\tEmployer: " + item['employer'] + "\n\tPosted By: " + item['postedBy'] + "\n")
      i += 1
    elif (item['username'] == username and item['status'] == 'removed'):
      print("{" +str(i) + "} " + "Job Title: " + item['title'] + "\n\tEmployer: " + item['employer'] + "\n\tPosted By: " + item['postedBy'] + "\n(Removed)" +"\n")
      i += 1
def RemovingSavedJob(username):
  savedJobs = {}
  with open('savedJobs.json') as f:
      savedJobs = json.load(f)
  size = 0
  for item in savedJobs['savedJobs']:
    if (item['username'] == username):
      size += 1
  # Check if there is any job postings
  if (size == 0):
      print("User has not saved any job posting yet.\n\n")
      return

  #The purpose of this while loop is to get the index of the job from the job.json
  index = 1
  while (index >= 0 and index < size + 1):

      try:
          index = int(
              input("Which job do you want to remove from your save list? (1-" + str(size) +
                    "). Enter 0 to return to previous page otherwise\n"))
      except ValueError:
          print("Input must be an integer! Try again\n")
          index = 1
          continue
      # Validate the input
      if (index < 0 or index > size):
          print("Invalid Input! Please only enter (1-" + str(size) + ")\n\n")
          index = 1
          continue

      #return to previous page
      if (index == 0):
          return
      break

  # the job object that we found from the job.json
  j = 0
  for item in savedJobs['savedJobs']: 
    if (item['username'] == username and index == 1):
      savedJobs['savedJobs'].pop(j)
      break
    if (item['username'] == username and index > 1):
      index -= 1
    j += 1
      
    

  with open('savedJobs.json', "w") as f:
      json.dump(savedJobs, f)
  