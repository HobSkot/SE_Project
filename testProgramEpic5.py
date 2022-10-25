from profiles import edit_profile_menu
from tud_test_base import set_keyboard_input, get_display_output
from viewYourProfile import viewProfile
from viewProfiles import viewFriendProfile
from homepage import homepage

def test_addProfileMenu():
    set_keyboard_input(["0"])
    edit_profile_menu("kk")
    output = get_display_output()
    assert output == [
        "*****************PROFILE MENU*****************",
        '[1] Title\n[2] Major\n[3] University Name\n[4] Information\n[5] Experience\n[6] Education\n[0] Back to previous page\n\n'
    ]


def test_addProfileTitle():
    set_keyboard_input(["1","1","student","0"])
    edit_profile_menu("kk")
    output = get_display_output()
    assert output == [
        '*****************PROFILE MENU*****************',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n',
        'Current Title: ',
        '\nWould you like to edit this info?\n[1] Yes\n[2] No\n\n',
        'Please enter new Title: ',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n'
    ]


def test_addProfileMajor():
    set_keyboard_input(["2","1","Computer Science","0"])
    edit_profile_menu("kk")
    output = get_display_output()
    assert output == [
        '*****************PROFILE MENU*****************',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n',
        'Current Major: ',
        '\nWould you like to edit this info?\n[1] Yes\n[2] No\n\n',
        'Please enter new major.\n',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n'
    ]

def test_addProfileUniversity():
    set_keyboard_input(["3","1","USF","0"])
    edit_profile_menu("kk")
    output = get_display_output()
    assert output == [
        '*****************PROFILE MENU*****************',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n',
        'Current University: ',
        '\nWould you like to edit this info?\n[1] Yes\n[2] No\n\n',
        'Please enter new University.\n',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n'
    ]


def test_addProfileSection():
    set_keyboard_input(["4","1","I love study","0"])
    edit_profile_menu("kk")
    output = get_display_output()
    assert output == [
        '*****************PROFILE MENU*****************',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n',
        'Current About Section: ',
        '\nWould you like to edit this info?\n[1] Yes\n[2] No\n\n',
        'Please enter new about description.\n',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n'
    ]


def test_addProfileJob():
    set_keyboard_input(["5","0","0"])
    edit_profile_menu("kk")
    output = get_display_output()
    assert output == [
        '*****************PROFILE MENU*****************',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n',
        #'Current About Section: ',
        'Which job profile would you like to look at? [1] [2] [3], or type [0] to exit.\nChoice: ',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n'
    ]

def test_addProfileEducation():
    set_keyboard_input(["6","1","ucf","0","0"])
    edit_profile_menu("kk")
    output = get_display_output()
    assert output == [
        '*****************PROFILE MENU*****************',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n',
        '[1] Schoolname: ',
        '[2] Degree: ',
        '[3] Years: ',
        '\nSelect what you wish edit: ',
        'Enter new school name: ',
        '\nSelect what you wish edit or type [0] to return: ',
        '[1] Title\n'
        '[2] Major\n'
        '[3] University Name\n'
        '[4] Information\n'
        '[5] Experience\n'
        '[6] Education\n'
        '[0] Back to previous page\n'
        '\n'
    ]

def test_printProfie():
    output = viewProfile("sam")
    assert output == 0

def test_viewFriendProfile():
    set_keyboard_input(["0"])
    viewFriendProfile("sam")
    output = get_display_output()
    assert output == [
        'Your current friends: ',
        '[1] Name: bob Username: kk',
        '[2] Name: bonk Username: ee',
        "Which friend's profile would you like to view?(Type 0 to return to the Homepage): "
    ]
