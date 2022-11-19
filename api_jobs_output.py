import json

def jobsOutputAPI():

  # Open file to write to
  with open('MyCollege_jobs.txt', 'w') as f:
    # For job in jobs
    with open('jobs.json') as jobsj:
      data = json.load(jobsj)
      allJobs = data["jobPostings"]
      for i in allJobs: # for each job-dict in jobPostings
        for j in i:     # for each key in selected job
          if j == "PostedBy":
            continue
          f.write(i[j]) # write keyValue.
          f.write("\n")
        f.write("=====\n")
  return
  

      
      
        
        
  
  
  