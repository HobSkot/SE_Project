import json

def jobsAppliedNotification(username):
  with open('jobApplications.json') as f:
    datadump = json.load(f)
  data = datadump['jobApplications']
  count = 0
  for i in data:
    if i['applicant'] == username:
      count += 1

  print("You have currently applied for " + str(count) + " jobs.\n")
  return