import json

#if get the title then call the new job function
def getTitle(jobTitle):
    job = jobTitle
    newJobNoty(job)

#this function for adding new job message to every user in order to print the notification
def newJobNoty(title):
  #open the notification file
    with open('studentNotification.json') as fp:
        newJob = json.load(fp)

#add new job content into each user's notification pending list
    for i in newJob['newNotify']:
        i['newJob'] = "A new job " + title + " has been posted"

    with open('studentNotification.json', 'w') as fp:
        json.dump(newJob, fp)
#this function for adding new user message to every user in order to print the notification
def newUser(first, last):
   #open the notification file
    with open('studentNotification.json') as fp:
        user = json.load(fp)
#add new user content into each user's notification pending list
    for i in user['newNotify']:
        i['newUser'] = "A new user " + first +" " + last +" has joined InCollege"

    with open('studentNotification.json', 'w') as fp:
        json.dump(user, fp)

#this function for printing all the new pending messages
def show_notify(user):

    #print("test part #1")
  #open the notification file
    with open('studentNotification.json') as fp:
        shows = json.load(fp)

    for i in shows['newNotify']:
        #print("test part #2")
      #looking up the username to print the pending messages
        if i['username'] == user:
            #print("test part #3")
            if i['newUser'] != " ":
                #print("test part #4")
                print("******** " + i['newUser'] + " ********\n")
                #print(i['newUser'])
              #reset message info into blank 
                i['newUser'] = " "
            if i['newJob'] != " ":
                print("******** " + i['newJob'] + " ********\n")
              #reset message info into blank 
                i['newJob'] = " "


    with open('studentNotification.json', 'w') as fp:
        json.dump(shows, fp)














