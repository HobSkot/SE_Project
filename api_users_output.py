import json

def usersOutputAPI():
  num = 0
  # Open file to write to
  with open('MyCollege_users.txt', 'w') as f:
    # For student in studentsLogin
    with open('students.json') as studentsj:
      data = json.load(studentsj)
      studentsArray = data["studentsLogin"] # studentsArray = array of users.
      for i in studentsArray: # for each dict in studentsLogin 
        f.write(studentsArray[num]["username"])
        f.write("\n")
        f.write(studentsArray[num]["Membership"])
        f.write("\n=====\n")
        num += 1
  return