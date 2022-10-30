import newaccount, homepage, login, video, connect
import useful_links,OptionChoice,important_links


choice = "0"
log_in = False
username = None


print("A college student success story\nThere was a college student called Beau. He joined InCollege in 2000 and he became successful on the next year. Impressive and motivative story from Beau\n-Beau Gate\n\n")

video.playVideo()

while choice != 6:
  
  choice = input("1: Login\n2: Create new account\n3: Connect to other InCollege users\n4. Useful Links\n5. Important Links\n\n")
  if (choice == "5"):
    important_links.importantLinks()
  if (choice == "4"): # Useful Links
      #print("choose the useful link")
      useful_links.usefulOpt()
  if(choice=="3"): # Connect to other InCollege users
    connect.connect2ppl(username, log_in)
  
  if(choice=="2"):  # new account
    
    name = input("Please create a unique username: ")
    password = input("Please create a strong password: ")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    univ = input("Enter your university: ")
    major = input("Enter your major: ")
    newaccount.newaccount(name, password,first,last, univ,major)
    print("Congrats on your new account!")
    #Continue from here.
    break
  elif(choice=="1"): # login
      username = input("Type a username: ")
      password = input("Type a password: ")
      result = login.login_page(username,password)
      if result == 0:
          log_in = True
          homepage.homepage(username,log_in) 







  