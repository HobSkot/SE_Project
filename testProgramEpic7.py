from tud_test_base import set_keyboard_input, get_display_output 
from message import message
from homepage import homepage 
from main import main
from login import login_page
from video import playVideo


def test_MsgRecieved():
  set_keyboard_input(["1","li","This is for PyTest.","0","0","n","1","li","Lili@1234"])
  message("sam")
  output = get_display_output()
  assert output == ["[1] Send a message\n[2] Generate a list of your friends\n[0]Return to previous page\n\n", "Enter the username of the receiver: ", "What do you want to tell them: ", "[1] Send a message\n[2] Generate a list of your friends\n[0]Return to previous page\n\n","\n\n[1] job search/internship\n[2] Find someone you know\n[3] Learn a new skill\n[4] General Links\n[5] Look at friends\n[6] Edit User Profile\n[7] View your friend's profiles\n[8] View your profile\n[9] Send message\n[0] Logout\nHow can I help you: ","A college student success story\nThere was a college student called Beau. He joined InCollege in 2000 and he became successful on the next year. Impressive and motivative story from Beau\n-Beau Gate\n\nA video about why students want to join InCollege\nWould you like to play the video?(y/n)\n" ,"1: Login\n2: Create new account\n3: Connect to other InCollege users\n4. Useful Links\n5. Important Links\n\n","Type a username: ","Type a password: ","======You have successfully logged in======\n","\nYou have an unread message from  sam \nMessage: This is for PyTest. \n"]

def test_FriendCheck():
  set_keyboard_input(["2","1","li"])
  message("wyne")
  output = get_display_output()
  assert output == ["\n**********FRIENDS LIST**********", "[1] lil\n[2] wyne\n********** END OF THE LIST**********\n\n[1] Send a message\n[2] Generate a list of your friends\n[0]Return to previous page\n\n", "Enter the username of the receiver: ", "You and ", "lil"," are not friend yet.\nDue to the limitation of your current membership, you are not allowed to send message to any InCollege users other than your InCollge friends.\n"]