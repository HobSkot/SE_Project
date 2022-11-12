from tud_test_base import set_keyboard_input, get_display_output
from jobSearch import *




def test_delJob():
  with open('jobs.json') as f:
    data = json.load(f)
  
  tempVar = data['jobPostings'][0].copy()
  set_keyboard_input(['1'])
  DeleteJob("sam")
  with open('jobs.json') as f:
    data = json.load(f)
  assert tempVar != data['jobPostings'][0]
    


def test_listAppliedJob():
  output = get_display_output()
  listOfAppliedJob("bobski")
  assert output == [] 