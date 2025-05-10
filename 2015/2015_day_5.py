#!/usr/bin/env python3

# Advent of Code 2015 - Day 5

inputString = open('/Users/maxnerdal/documents/AdventOfCode/2015/input/2015_day_5_input.txt').read()

# Part 1
def is_string_nice_part_one(inputString):
    vowels = set("aeiou")
    disallowedCombinations = {'ab', 'cd', 'pq', 'xy'}
    
    # Generator expressions 
    vowelCount = sum(1 for char in inputString if char in vowels)
    hasDoubleLetter = any(inputString[i] == inputString[i + 1] for i in range(len(inputString) - 1))
    hasDisallowedCombinations = any(subString in inputString for subString in disallowedCombinations)
    
    return vowelCount >= 3 and hasDoubleLetter and not hasDisallowedCombinations

# Part 2
"""
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
"""
def is_string_nice_part_two(inputString):
    
    #print(f"lenght teststring {len(testString)}")
    # Generator expressions 
    hasDoubleLetterWithOneletterInbetween = any(inputString[i] == inputString[i+2] for i in range(len(inputString) - 2))
    hasDoubleCombinations = any(inputString[i:i+2] in inputString[i+2:] for i in range(len(inputString) - 1))
    """
    for i in range(0, len(inputString) - 1,2):
        pair = inputString[i:i+2]
        print(f"Checking pair: {pair}")  # Debugging output
        if pair in inputString[i+2:]:
            print(f"Found repeated pair: {pair}")
            hasDoubleCombinations = True
            break
        else:hasDoubleCombinations = False
    """

    return hasDoubleLetterWithOneletterInbetween and hasDoubleCombinations



# Generator expressions
niceCountPartOne =sum(1 for line in inputString.splitlines() if is_string_nice_part_one(line))
niceCountPartTwo =sum(1 for line in inputString.splitlines() if is_string_nice_part_two(line))
print (f"part one {niceCountPartOne}")
print (f"part two {niceCountPartTwo}")