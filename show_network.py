import json


# Let it be noted : multiple functions are in this file which could be put into their own files.
# But we're in too deep to fall back. THE TECH DEBT IS TOO MUCH. Haha.

# Make sure student is logged in correctly w/ no bugs, else return 1 indicating error. (should probably throw an
# error instead but... eh)
def check_log(username, log_in):
    # Open Student.json file to turn into dictionary.
    with open('students.json') as json_file:  # open students.json
        data = json.load(json_file)  # variable data becomes DICTIONARY of students.json
    if not log_in:
        print("Error: User is not logged in.")
        return 1
    for i in data['studentsLogin']:
        if username in i['username']:
            return 0
    print("User is NOT logged in.\nExiting...")
    return 1


# function to delete selected friend as well as vice versa.
def deleteFriend(loggedInUsername, friendToDelete):
    with open('userFriends.json') as friend_json:
        friends_json = json.load(friend_json)
        # Dictionary containing keys that are usernames and values that are Arrays of friends.

        userDelFriend = friends_json['studentFriends'][loggedInUsername]  # Array of user's friends
        friendDelUser = friends_json['studentFriends'][friendToDelete]  # Array of DELuser's friends

    # Logic to find and delete targeted friend in Array.
    i = 0
    while (userDelFriend[i].get("username") != friendToDelete):
        i += 1
    tempName = userDelFriend[i]["name"]  # Used later for print statement. # name of targeted friend.
    userDelFriend.pop(i)

    # Now, the selected friend (friendToDelete) will lose friend dictionary with loggedInUsername.
    i = 0
    while (friendDelUser[i].get("username") != loggedInUsername):
        i += 1
    friendDelUser.pop(i)
    print("\nDeleted " + tempName + " from your friends list.\n")

    # Rewrite file with updated information.
    with open('userFriends.json', 'w') as f:
        json.dump(friends_json, f)
    return


# Main function which shows logged in user's friend list.
def show_network(username, log_in):  # Main function

    check = check_log(username, log_in)  # Check if User is logged in
    if check == 1:
        return

    ### MAIN CODE STARTS
    with open('userFriends.json') as friend_json:
        friend_data = json.load(friend_json)
        friendArray = friend_data['studentFriends'][username]  # friendArray = Array of dictionaries. The dictionaries are the friend accounts associated with logged_in user.

    print("\n\n**********FRIENDS**********")
    k = 1
    if len(friendArray) > 0:  # if friendArray is not empty
        for i in friendArray:  # print out friends of logged_in user.
            print("[" + str(k) + "]" + " " + i['name'])
            k += 1
    else:
        print("\nCurrently, there is no one added to the friend's list.\n")
        return

    # MENU ON WHAT PERSON WISHES TO DO. DEPENDS ON LENGTH OF FRIENDS LIST 0 or more than 0.
    choice = input("\nWhat would you like to do now?\n1. Delete a friend\n2. Go Back\n")
    if (choice == "1"):
        deleteChoice = input(
            "Which friend would you like to delete from your friends list?\nType the number to delete or 0 to go back.\n\n")
        # Delete function
        if (int(deleteChoice) == 0):  # go back.
            return
        friendChoice = friendArray[int(deleteChoice) - 1]['username']
        deleteFriend(username, friendChoice)
    elif (choice == "2"):  # Return.
        return
    return
