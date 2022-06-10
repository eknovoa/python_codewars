"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""

def xo(s):
    # initalizing these counter variables to 0
    letter_x = 0
    letter_o = 0
    
    # use a for loop to iterate through each character in the string and check to see if it is an x or an o. If it is one of those incrememnt the appropriate
    # variable by 1
    
    for letter in s:
        if letter == 'x' or letter == 'X':
            letter_x += 1
        elif letter == 'o'or letter == 'O':
            letter_o += 1
    
    # if the count of 'x's are not equal to the count of 'o's then return false, else return true
    if letter_x != letter_o:
        return False
    return True
  
 
