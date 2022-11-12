import skill
from profiles import edit_profile_menu
import jobSearch, connect,important_links, viewProfiles, viewYourProfile
from show_network import show_network
import message

def homepage(username, log_in):
  message.checkMessages(username)
  message.messageNotification(username)
  choice2 = 1
  while (choice2 != 0):
    try:
      choice2 = int(input("\n\n[1] job search/internship\n[2] Find someone you know\n[3] Learn a new skill\n[4] General Links\n[5] Look at friends\n[6] Edit User Profile\n[7] View your friend's profiles\n[8] View your profile\n[9] Send message\n[0] Logout\nHow can I help you: "))
      if (choice2 == 1):
        print("\n")
        jobSearch.job(username, log_in);
      elif (choice2 == 2):
        print("\n")
        connect.findByCon(username)
      elif (choice2 == 3):
        print("\n")
        skill.learnSkill();
      elif(choice2 == 4):
        print("\n")
        important_links.importantLinks(log_in, username)
      elif(choice2 == 5):
        print("\n")
        show_network(username,log_in)
      elif(choice2 == 6):
        print("\n")
        edit_profile_menu(username)
      elif(choice2 == 7):
        print("\n")
        viewProfiles.viewFriendProfile(username)
      elif(choice2 == 8):
        print("\n")
        viewYourProfile.viewProfile(username)
      elif(choice2 == 9):
        message.message(username)
      elif (choice2 == 0):
        break
      else:
        print("Please select a vaild option.")

    except ValueError:
      print("\n\nAn exception occured in homepage!\n\n")