from datetime import datetime, timedelta
import json

selectedStudent = 0

def lastLoginNotification(username):
  with open('students.json') as f:
    students = json.load(f)
  arrayIndex = 0
  for student in students['studentsLogin']:
    if student['username'] == username:
      selectedStudent = student
    arrayIndex += 1
  if selectedStudent == 0:
    print("Student not found in system - lastLogin.py")
    return
    
  #Check last login date, if >7 days, print
  selectedStudent['lastLoginDate'] = datetime.utcnow()
  sevenDaysAgo = datetime.utcnow() - timedelta(days=7)  # 7 days ago
  if (selectedStudent['lastLoginDate'] < sevenDaysAgo):
    print("Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
  else: print("Hi there wandering traveler.")
    
  # Now that user is logged in, record login date
  selectedStudent['lastLoginDate'] = datetime.utcnow()
  #write
  with open('students.json', 'w') as rea:
    json.dump(students, rea)
    