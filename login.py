import json, friendRquest
from lastApply import lastApplyNotification
from createProfileNotification import remindProfileNotification
from notifys import show_notify


def login_page(username, password, log_in = False):
    while (log_in == False):
        with open('students.json') as f:
            data = json.load(f)
        for student in data['studentsLogin']:
            if (student['username'].lower() == username.lower() and student['password'] == password):
                print("======You have successfully logged in======\n")
                friendRquest.show_request(username)
                lastApplyNotification(username)
                remindProfileNotification(username)
                show_notify(username)
                log_in = True
                return 0

        if (log_in == False):
            print("Incorrect username/password, please try again\n")
            return 1
    else:
        print("Invalid choice. Please choose between 1 or 2.\n")
        return 1