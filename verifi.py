# Verifies if input'd string follows all guidelines. Return 0 if it follows all criteria and returns 1 if an error occurs.
import re

def verifiPass(validate):
  if (len(validate) < 8 or len(validate) > 12):
    print("Invalid length of name.(The length should between 8 -- 12 characters) ")
    return 1
  if (re.search('[0-9]',validate) is None):
    print("Password requires a number ")
    return 1
  if (validate == validate.lower()):
    print("Require an uppercase letter. ")
    return 1
  if validate.isalnum():
    print("Password requires a special character")
    return 1
  return 0