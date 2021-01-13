# "Validating Postal Codes" is a coding challenge on the HackerRank Website.
# Link to problem:- https://www.hackerrank.com/challenges/validating-postalcode/problem

# Resources:-
# https://docs.python.org/3/library/re.html
# https://regexr.com/

regex_integer_in_range = r""
regex_alternating_repetitive_digit_pair = r""


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
