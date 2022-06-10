"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

"""

def solution(string, ending):
    # dependent on length of ending variable so we know where to slice the string variable which is the first parameter
    count = len(ending)

    # we need to account for this case that if the length of ending string is 0 then we will automatically return true
    if len(ending) == 0:
        return True
    # slice the other variable, string, to get substring and see if it is equal to the ending variable
    elif string[-count:] == ending:
        return True
    return False
  
  
