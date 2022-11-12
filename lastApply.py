import time, json

selectedStudent = 0

def lastApplyNotification(username):
  with open('students.json') as f:
    students = json.load(f)
  for student in students['studentsLogin']:
    if student['username'] == username:
      selectedStudent = student
  if selectedStudent == 0:
    print("Student not found in system - lastLogin.py")
    return
    
  #Check last login date, if >7 days, print
  currentTime = int(time.time()) # seconds since epoc - decimal cut out.
  sevenDaysAgo = currentTime - 604800  # 7 days ago = 604800 seconds.
  if (selectedStudent['lastApplyDate'] < sevenDaysAgo): # closer to now, bigger the number is.
    print("Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
  return




#Injected Function by Cory   
def updateApplyTime(username):      
    selectedStudent = 0
  
    with open('students.json') as r:
      studentDataCollection = json.load(r)
    for student in studentDataCollection['studentsLogin']:
      if student['username'] == username:
        selectedStudent = student
    if selectedStudent == 0:
      print("Student not found in system - lastLogin.py")
      return
    selectedStudent['lastApplyDate'] = int(time.time())
    with open('students.json', 'w') as rea:
      json.dump(studentDataCollection, rea)
    return
    