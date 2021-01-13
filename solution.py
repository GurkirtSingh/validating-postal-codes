# "Validating Postal Codes" is a coding challenge on the HackerRank Website.
# Link to problem:- https://www.hackerrank.com/challenges/validating-postalcode/problem

# Resources:-
# https://docs.python.org/3/library/re.html
# https://regexr.com/

import re

# create regex to validate a 6 digit number from 100000 to 999999
regex_integer_in_range = r"(^[1-9][0-9]{5}$)"

# create regex to validate alternating repetitive digit
regex_alternating_repetitive_digit_pair = r"(?=([0-9]).\1)"   

# get the input string
P = input()

# print true
# if string match "regex_integer_in_range"
# if input strig have more than one alternating repetitive digit
# else false
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
