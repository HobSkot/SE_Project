import skill
from profiles import edit_profile_menu
import jobpost, connect,important_links, friendRquest, viewProfiles, viewYourProfile
from show_network import show_network

def homepage(username, log_in):
  choice2 = 1
  while (choice2 != 0):
    try:
      choice2 = int(input("[1] job search/internship\n[2] Find someone you know\n[3] Learn a new skill\n[4] General Links\n[5] Look at friends\n[6] Edit User Profile\n[7] View your friend's profiles\n[8] View your profile\n[0] Logout\n"))
      if (choice2 == 1):
        jobpost.PostJob(username, log_in);
      elif (choice2 == 2):
        connect.findByCon(username)
      elif (choice2 == 3):
        skill.learnSkill();
      elif(choice2 == 4):
        important_links.importantLinks(log_in, username)
      elif(choice2 == 5):
        show_network(username,log_in)
      elif(choice2 == 6):
        edit_profile_menu(username)
      elif(choice2 == 7):
        viewProfiles.viewFriendProfile(username)
      elif(choice2 == 8):
        viewYourProfile.viewProfile(username)
      elif (choice2 == 0):
        break
      else:
        print("Please select a vaild option.")

    except ValueError:
      print("\n\nAn exception occured in homepage!\n\n")