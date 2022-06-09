"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

def solution(s):
    string_list = []
    i = 0;
    while i < len(s):
        if (i == len(s) - 1)  and (len(s) % 2 != 0):
            string_list.append(s[i] + '_')
        else:
            string_list.append(s[i:i+2])
        i += 2;
    return string_list
  
