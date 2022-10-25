import OptionChoice, newaccount

# GENERAL MENU LINKS

# General --> provide links to Sign Up-->userToSignInMenu, Help Center-->produce the message "We're here to help",
    # About-->" displays "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide. 
    # Press-->  result in the message "In College Pressroom: Stay on top of the latest news, updates, and reports" being displayed.,   # Blog --> "Under construction" to be displayed. 
    # Careers --> "Under construction" to be displayed.
    # Developers. --> "Under construction" to be displayed.
    # BE ABLE TO SELECT GENERAL

def generalMenu():
  print("*****************GENERAL MENU*****************")
  print("[1] Sign Up\n[2] Help Center\n[3] About\n[4] Press\n[5] Blog\n[6] Careers\n[7] Developers\n[8] Back to previous page")



def generalOption():
  generalMenu()
  options = OptionChoice.userOption()
  while options != 8:
    # Sign up option
    if options == 1:
      print("Sign up a new account")
      name = input("Please create a unique username: ")
      password = input("Please create a strong password: ")
      first = input("Enter your first name: ")
      last = input("Enter your last name: ")
      newaccount.newaccount(name, password, first, last)
      generalMenu()
      options = OptionChoice.userOption()
    #Help Center option
    elif options == 2:
      print("\nWe are here to help")
      generalMenu()
      options = OptionChoice.userOption()
    #About option
    elif options == 3:
      print("\nIn College: Welcome to In College, the world's largest college studentnetwork with many users in many countries and territories worldwide")
      generalMenu()
      options = OptionChoice.userOption()
    #Press option
    elif options == 4:
      print("\nIn College Pressroom: Stay on top of the latest news, updates, and reports")
      generalMenu()
      options = OptionChoice.userOption()
    #Blog option
    elif options == 5:
      print("\nUnder construction")
      generalMenu()
      options = OptionChoice.userOption()
    #Careers option
    elif options == 6:
      print("\nUnder construction")
      generalMenu()
      options = OptionChoice.userOption()
    #Developers option
    elif options == 7:
      print("\nUnder construction")
      generalMenu()
      options = OptionChoice.userOption()

    #Invalid option
    else:
      print("\nInvalid option\n")
      generalMenu()
      options = OptionChoice.userOption()



