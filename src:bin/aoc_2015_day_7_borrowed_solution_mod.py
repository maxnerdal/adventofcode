#!/usr/bin/python3

d = {}
indent = 0

def getLines(inFile):
    with open(inFile, 'r') as f:
        return f.readlines()
    
def fillDict(lines):
    for line in lines:
        a = line.split(' -> ')
        d[a[1].strip()] = a[0] #set right side of split to dict key and left side to value/expression

def NOT(x):
    return (~x) % (1 << 16)

def AND(x, y):
    return (x & y) % (1 << 16)

def OR(x, y):
    return (x | y) % (1 << 16)

def RSHIFT(x, y):
    return (x >> y) % (1 << 16)

def LSHIFT(x, y):
    return (x << y) % (1 << 16)

def eval(x):
    try:
        global indent
        indent += 1
        #print(' ' * indent + 'start eval')
        if x.isdigit():
            return int(x)
        expr = d[x]
        print(' ' * indent + expr)
        tokens = expr.split(' ')
        #print(tokens)
        result = ''
        if len(tokens) == 1:
            result = eval(tokens[0])
        elif tokens[0] == 'NOT':
            result = NOT(eval(tokens[1]))
        elif tokens[1] == 'AND':
            result = AND(eval(tokens[0]), eval(tokens[2]))
        elif tokens[1] == 'OR':
            result = OR(eval(tokens[0]), eval(tokens[2]))
        elif tokens[1] == 'RSHIFT':
            result = RSHIFT(eval(tokens[0]), eval(tokens[2]))
        elif tokens[1] == 'LSHIFT':
            result = LSHIFT(eval(tokens[0]), eval(tokens[2]))
        print(' ' * indent + str(x) + ' = ' + str(result))
        d[x] = str(result)
        return result
        raise RecursionError()
    finally:
      #print(' ' * indent + 'exit ' + str(x))
        indent -= 1
        pass

if __name__ == '__main__':
    fillDict(getLines('/Users/maxnerdal/documents/AdventOfCode/2015/input/2015_day_7_input.txt'))
    print(eval('a'))
    #print(d)
    #fillDict(getLines('input7-2.txt'))
    #print(eval('a'))