import json

def appliedJobsOutputAPI():
  num = 0
  # Open file to write to
  # Write job title
  # Check if title exist in each application in jobapp, if so, write username and explainYourself
  # Next

  
  with open('MyCollege_appliedJobs.txt', 'w') as f:
    # For job in jobs
    with open('jobApplications.json') as appsj:
      appData = json.load(appsj)
      applicationData = appData["jobApplications"]
    with open('jobs.json') as jobsj:
      data = json.load(jobsj)
      allJobs = data["jobPostings"]
      for i in allJobs: # for each job-dict in jobPostings
        jobTitle = allJobs[num]["Title"]
        f.write(jobTitle)
        f.write("\n")

        
        ### HERE, I'M CHECKING FOR THE TITLE IN EACH JOB APPLICAITON TO SEE IF ANY1 APPLIED FOR THE JOB.]
        appNum = 0
        for j in applicationData:     # for each dict in jobApplication.json
          if jobTitle == applicationData[appNum]["title"]: #if title is matching jobApplication title (yes, prone to error but for this project is good)
            f.write(applicationData[appNum]["applicant"])
            f.write("\n")
            f.write(applicationData[appNum]["explainYourself"])
            f.write("\n")
        f.write("=====\n")
        num += 1
  return
  

      
      
        
        
  
  
  