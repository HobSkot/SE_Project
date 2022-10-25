# This file will play a video 

def playVideo(): 
  choice = ""
  while (choice.lower() != "y" and choice.lower() != "n" ):
    print("A video about why students want to join InCollege")
    choice = input("Would you like to play the video?(y/n)\n")
    if (choice.lower() == "y"):
      print("Video is playing.\n")
    elif(choice.lower() == 'n'):
        break
    else:
      print("Incorrect Input! Please Try Again.\n")


