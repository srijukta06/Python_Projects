# Write a Python function to determine if a string is a palindrome

import re

def is_palindrome(phrase):
  forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
  backwards = forwards[::-1]
  return forwards == backwards
