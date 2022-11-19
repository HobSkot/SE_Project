import json

def profilesOutputAPI():

  # Open file to write to
  with open('MyCollege_profiles.txt', 'w') as f:
    # For job in jobs
    with open('profiles.json') as profilesj:
      data = json.load(profilesj)
      allProfiles = data["userProfiles"] 
      for i in allProfiles: # for each user in userProfiles
        f.write(i)
        f.write("\n")
        for j in allProfiles[i]:     # for each key in selected user
          if j == "experience":
            for jobs in allProfiles[i][j]: # for each experince--> job
              for key in allProfiles[i][j][jobs]:
                f.write(allProfiles[i][j][jobs][key])
                f.write("\n")
            
            continue
          if j == "education":
            for key in allProfiles[i][j]:
              f.write(allProfiles[i][j][key])
              f.write("\n")
            
            continue
          f.write(allProfiles[i][j]) # write keyValue.
          f.write("\n")
        f.write("=====\n")
  return