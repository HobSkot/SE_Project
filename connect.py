import json, homepage, login, newaccount, friendRquest


def connect2ppl(username, log_in):
    choice5 = 1
    exists = False

    while (choice5 > 0 and choice5 < 3):
        choice5 = int(input("1:Search for other users\n2:Return to homepage\n"))
        if (choice5 == 1):
            print("Please enter the user's name you are looking for.\n")
            firstName = input("What is the user's first name?: ")
            lastName = input("And their Last Name?: ")
            with open('students.json') as f:
                data = json.load(f)
                for item in data['studentsLogin']:
                    if firstName.lower() in item['first'] and lastName.lower() in item['last']:
                        exists = True
                        print("They are a part of the InCollege system.")
                        print("We look forward to you joining us!")
                        # ask user to either join InCollege or creat account
                        userChoice = int(input("1: Log in\n2: Create Account\n3: Exit"))
                        if (userChoice == 1):
                            userName = input("Type a username: ")
                            passWord = input("Type a password: ")
                            result = login.login_page(userName, passWord)
                            if result == 0:
                                log_in = True
                                homepage.homepage(userName, log_in)

                        elif (userChoice == 2):
                            name = input("Please create a unique username: ")
                            password = input("Please create a strong password: ")
                            first = input("Enter your first name: ")
                            last = input("Enter your last name: ")
                            univ = input("Enter your university: ")
                            major = input("Enter your major: ")
                            newaccount.newaccount(name, password, first, last, univ, major)
                        elif (userChoice == 3):
                            print("Exiting...")
                            return
                        else:
                            print("Invalid input, please try again")

                if (not exists):
                    print("They are not yet a part of the InCollege system yet.")
        if (choice5 == 2):
            print("\n\n")
            return


def findByCon(username):
    print("==============FIND FRIENDS==============")
    find_choice = int(input("[1] Search by last name\n[2] Search by university\n[3] Search by Major\n"))
    counter = findByCondition(find_choice)
    if counter != 0:
        userchoice = input("Would you like to add friend?(Y/N)")
        if userchoice.lower() == 'y':
            reciver = input("Enter the username: ")
            print("=====SENDING FRIEND REQUEST=====")
            friendRquest.send_request(reciver, username)

        elif userchoice.lower() == 'n':
            print('=====BACKING TO UPPER PAGE=====')
            print()
        else:
            print("Invalid input")

    if counter == 0:
        print("User not found")
    return

def findByCondition(infoType):
    #counter = 0
    k = 0
    with open('students.json')as fp:
        item = json.load(fp)

        if infoType == 1:
            searchByLast = input("Enter Last Name:")
            item_last = item["studentsLogin"]
            print( '== == LIST == ==')
            for i in item_last:
                if i['last'] == searchByLast:
                    k += 1
                    print("[" + str(k) + "]" + " username: " + i['username'])
                    print("Name: " + i['first'] + ' ' + i['last'])

            return k


        elif infoType == 2:
            searchByUniv = input("Enter University Name:")
            item_last = item["studentsLogin"]
            print( '== == LIST == ==')
            for i in item_last:
                if i['university'] == searchByUniv:
                    k += 1
                    print("[" + str(k) + "]" + "username:" + i['username'])
                    print("Name:" + i['first'] + ' ' + i['last'])
            return k
        elif infoType == 3:
            searchByMajor = input("Enter Major:")
            item_last = item["studentsLogin"]
            print( '== == LIST == ==')
            for i in item_last:
                if i['major'] == searchByMajor:
                    k += 1
                    print("[" + str(k) + "]" + "username:" + i['username'])
                    print("Name:" + i['first'] + ' ' + i['last'])

            return k
        else:
            print("====Invalid input====\n====Try Again(Please Enter 1, 2 or 3)====")

    return