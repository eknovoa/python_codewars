"""
Pair of gloves
Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

Examples:
input = ["red", "green", "red", "blue", "blue"]
result = 2 (1 red pair + 1 blue pair)

input = ["red", "red", "red", "red", "red", "red"]
result = 3 (3 red pairs)
"""

def number_of_pairs(gloves):
    count = 0
    if len(gloves) == 0:
        return 0
    pairs = []
    for glove_color in gloves:
        num = gloves.count(glove_color)
        if glove_color in pairs:
            continue
        else:
            pairs.append(glove_color)
            if num >= 2:
                if num == 2:
                    count += 1
                elif num > 2:
                    count = count + (num // 2)
    return count
  
  
