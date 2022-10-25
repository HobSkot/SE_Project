
def userOption():

    option = 0
    while True:
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please, enter a valid integer\n")
            continue
        else:
            #print(f'You entered: {option}')
            return option

