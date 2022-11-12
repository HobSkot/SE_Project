from tud_test_base import set_keyboard_input, get_display_output 
import jobsAppliedNotification
import createProfileNotification 
import notifys
import lastApply
import message


def test1_job_Applied_Notificaiton():
    set_keyboard_input([])
    jobsAppliedNotification.jobsAppliedNotification("li")
    output = get_display_output()
    assert output == [
        "You have currently applied for 1 jobs.\n"
    ]

def test2_job_Applied_Notificaiton():
    set_keyboard_input([])
    jobsAppliedNotification.jobsAppliedNotification("sam")
    output = get_display_output()
    assert output == [
        "You have currently applied for 0 jobs.\n"
    ]

def test1_profile_Notificaiton():
    set_keyboard_input([])
    createProfileNotification.remindProfileNotification("sam")
    output = get_display_output()
    assert output == [
    ]

def test2_profile_Notificaiton():
    set_keyboard_input([])
    createProfileNotification.remindProfileNotification("li")
    output = get_display_output()
    assert output == [ "Don't forget to create a profile"
    ]

def test1_notify():
  set_keyboard_input([])
  notifys.show_notify("sam")
  output = get_display_output()
  assert output == [ 
  ]
# Some changes would be made in studentNotification.json during the testing of test2_notify() . Make sure you revert the changes in studentNotification.json everytime after the testing is done.
def test2_notify():
  set_keyboard_input([])
  notifys.newJobNoty("Programmer")
  notifys.newUser("Eunice", "Blake")
  notifys.show_notify("sam")
  output = get_display_output()
  assert output == [ "******** A new user Eunice Blake has joined InCollege ********\n", "******** A new job Programmer has been posted ********\n"
  ]

def test1_lastApplied_Notificaiton():
    set_keyboard_input([])
    lastApply.lastApplyNotification('sam')
    output = get_display_output()
    assert output == [
        "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!"
    ]

def test2_lastApplied_Notificaiton():
    set_keyboard_input([])
    lastApply.lastApplyNotification('li')
    output = get_display_output()
    assert output == [
    ]
# Some changes would be made in students.json when this test run. Make sure you revert the changes in students.json everytime after this test is done.
def test3_lastApplied_Notificaiton():
    set_keyboard_input([])
    lastApply.updateApplyTime('sam')
    lastApply.lastApplyNotification('sam')
    output = get_display_output()
    assert output == [
    ]


def test_message_Notificaiton():
    set_keyboard_input([])
    message.checkMessages("li")
    output = get_display_output()
    assert output == ["=======You have messages waiting for you======="
    ]
