import json

def newJobsAPI():
  jobsArray = []
  with open('newJobs.txt') as f:
    content = f.read()
  jobs = content.split("=====")
  jobs.pop()
  for job in jobs:
    lines = job.strip().split('\n')
    i = 0
    title = lines[i]
    ind = lines.index('&&&')
    array = lines[1:ind]
    description = " ".join(array)
    i = ind + 1
    poster = lines[i]
    i += 1
    employer = lines[i]
    i += 1
    location = lines[i]
    i += 1
    salary = lines[i]
    
      
      
    tempJob = {"Title": title, "Description": description, "Employer": employer, "Location": location, "Salary": salary, "PostedBy": poster}
    
    jobsArray.append(tempJob)
        
  if (len(jobsArray) == 0):
    return
  
  with open('jobs.json') as f:
    jobs = json.load(f)
      
    for job in jobsArray:
      check = True
      for item in jobs['jobPostings']:
        if job['Title'] == item['Title']: 
          check = False
          break
      if (len(jobs['jobPostings']) == 10):
        return
      if (not check):
        continue
      jobs['jobPostings'].append(job)
      with open('jobs.json', "w") as f:
        json.dump(jobs, f)