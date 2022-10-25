# USEFUL LINKS MENU

# General --> General Links 
# Browse InCollege --> "Under construction" to be displayed. 
# Business Solutions --> "Under construction" to be displayed. 
# Directories --> "Under construction" to be displayed. 

import OptionChoice,general_links
def usefulMenu():
  print("*****************USEFUL MENU*****************")
  print( "[1] General\n[2] Browse InCollege\n[3] Business Solutions\n[4] Directories\n[5] Back to previous page")

def usefulOpt():
  usefulMenu()
  options = OptionChoice.userOption()
  while options != 5:
    #General option
    if options == 1:
      #print("You choose the General Option")
      general_links.generalOption()
      usefulMenu()
      options = OptionChoice.userOption()
    #Browse option
    elif options == 2:
      print("\nUnder construction")
      usefulMenu()
      options = OptionChoice.userOption()

    #Business Option
    elif options == 3:
      print("\nUnder construction")
      usefulMenu()
      options = OptionChoice.userOption()

    #Directories option
    elif options == 4:
      print("\nUnder construction")
      usefulMenu()
      options = OptionChoice.userOption()

    else:
      print("\nInvalid option\n")
      usefulMenu()
      options = OptionChoice.userOption()





