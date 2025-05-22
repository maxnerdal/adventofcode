#!/usr/bin/python3

#Advent Of Code 2015 day 8

def getLines(inFile):
    with open(inFile, 'r') as f:
        return [line.rstrip('\n') for line in f]
    
def countCaracters(input):
    countRawCaracters = sum(len(line) for line in input)
    countEvalCaracters = sum(len(eval(line)) for line in input)
    return countRawCaracters - countEvalCaracters

def getNewString(line):
        line = line.replace('\\', '\\\\')
        line = line.replace('"', '\\"')
        return '"'+line+'"'

def main():
    lines = getLines("/Users/maxnerdal/documents/adventofcode/input/aoc_2015_day_8_input.txt")
    linesEncoded = [getNewString(line) for line in lines]
    print("Part 1: ", countCaracters(lines))
    print("Part 2: ", countCaracters(linesEncoded))
 
if __name__ == '__main__':
    main()