# IMPORTANT LINKS MENU

# Copyright
# About
# Accessibility
# User Agreement
# Privacy Policy
# Cookie Policy
# Brand Policy
# Guest Controls
# !!!Languages!!!
import OptionChoice, privacy, json


def produceMenu():
  print("\n[1]. Copyright\n[2]. About\n[3]. Accesibility\n[4]. User Agreement\n[5]. Privacy Policy\n[6]. Cookie Policy\n[7]. Brand Policy\n[8]. Languages\n[9]. Go Back\n\n")
def spanishMenu():
  print("\n[1]. Derechos de autor\n[2]. Acerca de \n[3]. Accesibilidad\n[4]. Acuerdo de usuario\n[5]. Política de privacidad\n[6]. Política de Cookies\n[7]. Política de marca\n[8]. Idiomas\n[9]. Volver")

def importantLinks(log_in = False, username = ""):
  with open('userSetting.json') as f:
    data = json.load(f)
    
  produceMenu()
  selectChoice = OptionChoice.userOption()
    
  while (selectChoice != 9):
    if(selectChoice == 1): # copyright
      print("This is our Copyright. Please be smart before you get demonitized by us.")
      produceMenu()
      selectChoice = OptionChoice.userOption()
    elif (selectChoice == 2): # About
      produceMenu()
      selectChoice = OptionChoice.userOption()
    elif (selectChoice == 3): # Accessibility
      print("Access Denied.\n\n\n\n\n\n...Just kidding.")
      produceMenu()
      selectChoice = OptionChoice.userOption()
    elif (selectChoice == 4): # User Agreement
      print("Just like all User Agreements, you ticked that you read it without actually reading it... didn't you.")
      produceMenu()
      selectChoice = OptionChoice.userOption()
    elif (selectChoice == 5): # Privacy Policy
      if (log_in == False):
        print("Please log into your account to view private information.\n")
      else:
        privacy.privacy(username)
      produceMenu()
      selectChoice = OptionChoice.userOption()
    elif (selectChoice == 6): #Cookie Policy
      print("Careful leaving cookies out at night... there's a monster eating them all up.\n\n")
      produceMenu()
      selectChoice = OptionChoice.userOption()
    elif (selectChoice == 7): #Brand Policy
      print("A Great Idea Like Einstein. AGILE.")
      produceMenu()
      selectChoice = OptionChoice.userOption()
    elif (selectChoice == 8): #Languages 
      print("====SELECT LANGUANGE====\n[1] English\n[2] Spanish")
      userLanguage = OptionChoice.userOption()
      if(userLanguage == 1):
        print("System Setting.....")
        for elem in data['userSetting']:
          if (elem['username'] == username):
            del elem['language']
            elem['language'] = "eng"
        print("The system has been set to English")
        produceMenu()
      elif(userLanguage == 2):
        print("System Setting.....")
        for elem in data['userSetting']:
          if (elem['username'] == username):
            del elem['language']
            elem['language'] = "spa"
        print("El sistema se ha configurado para que esté en español")
        spanishMenu()
      selectChoice = OptionChoice.userOption() 
    else:
      print("Invalid input, please select a valid option...\n\n")
      produceMenu()
      selectChoice = OptionChoice.userOption()

  with open('userSetting.json', 'w') as f:
    json.dump(data, f)
