from tud_test_base import set_keyboard_input, get_display_output
from show_network import show_network
from friendRquest import send_request, show_request
from connect import findByCon, findByCondition
import json


def test_show_Network1():
    set_keyboard_input(["2"])
    show_network("sam", True)
    output = get_display_output()
    assert output == [
        "\n\n**********FRIENDS**********",
        "[1] bob",
        "[2] bonk",
        "\nWhat would you like to do now?\n1. Delete a friend\n2. Go Back\n",
    ]


def test_show_Network2():
    set_keyboard_input(["2"])
    show_network("sam", True)
    output = get_display_output()
    assert output == [
        "\n\n**********FRIENDS**********",
        "[1] bob",
        "[2] bonk",
        "\nWhat would you like to do now?\n1. Delete a friend\n2. Go Back\n",
    ]


def test_show_Network3():
    set_keyboard_input(["2"])
    show_network("aa", True)
    output = get_display_output()
    assert output == [
        "\n\n**********FRIENDS**********",
        "\nCurrently, there is no one added to the friend's list.\n"
    ]


def test_show_Network4():
    set_keyboard_input(["1", "1"])
    show_network("sam", True)
    output = get_display_output()
    assert output == [
        "\n\n**********FRIENDS**********", "[1] bob", "[2] bonk",
        "\nWhat would you like to do now?\n1. Delete a friend\n2. Go Back\n",
        "Which friend would you like to delete from your friends list?\nType the number to delete or 0 to go back.\n\n",
        "\nDeleted bob from your friends list.\n"
    ]

def test_sent_request(): 
  send_request("aa","sam")
  with open('friendsRequest.json') as f:
    data = json.load(f)
    requests = data['request']
    assert requests[0] == {'reciver':'aa' ,'senderFirst': 'sam', 'senderLast': 'ssh', 'sender': 'sam'}

def test_show_request():
  set_keyboard_input(["Y"])
  show_request("aa")
  output = get_display_output()
  assert output == ["======You have a friend request=====", "The user sam ssh want to add you as friend", "Would you like to add user as friend? Y/N", "=====Friend added====="
  ]

def test_find_by_condition():
  set_keyboard_input(["ssh"])
  findByCondition(1)
  output = get_display_output()
  assert output == ["Enter Last Name:", "== == LIST == ==", "[1] username: sam", "Name: sam ssh"]

def test_find_by_con():
  set_keyboard_input([1,"kers", "y", "ee" ])
  findByCon("sam")
  output = get_display_output()
  assert output == ["==============FIND FRIENDS==============", "[1] Search by last name\n[2] Search by university\n[3] Search by Major\n", "Enter Last Name:", "== == LIST == ==", "[1] username: ee", "Name: bonk kers", "Would you like to add friend?(Y/N)", "Enter the username: ", "=====SENDING FRIEND REQUEST====="]
  
  
      
    
    