#!/usr/bin/python3

#Advent Of Code 2015 day 8

#from parse import get_lines


def diffLine(line):
    print(len(line.strip()))
    print(len(eval(line.strip())))
    return len(line.strip()) - len(eval(line.strip()))

def solve(lines):
    return sum(map(diffLine, lines))

def get_lines(filename):
    lines = []
    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline().rstrip('\n')
                if line == '':
                    break
                lines.append(line)
    except EOFError:
        pass
    return lines

if __name__ == '__main__':
    lines = (get_lines('/Users/maxnerdal/documents/adventofcode/input/aoc_2015_day_8_input_test.txt'))
    #lines = ["byc\x9dyxuafof\\\xa6uf\\axfozomj\\olh\x6a"] #43
    print(solve(lines))