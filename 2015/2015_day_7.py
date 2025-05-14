#!/usr/bin/env python3
# Advent of Code 2015 - Day 7

inputString = open('/Users/maxnerdal/documents/AdventOfCode/2015/input/2015_day_7_input.txt').read()
wireDictionary = {}
counter = 0

# Part 1
def parse_instructions(InputInstructions):
    global wireDictionary
    instructionDictionary = {}
    operationString = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
    for line in InputInstructions.splitlines():
        parts = line.split()

        # declare all parts of instruction
        for i in range(len(parts)+1):
            if parts[i] in operationString:
                # if operation is "NOT", operand2 is None and operand1 is the next part
                if parts[i] == "NOT":
                    operation = parts[i]
                    operand1 = parts[i+1]
                    operand2 = None
                    # if operand1 is not a digit, add it as a wire to the wireDictionary
                    if not operand1.isdigit(): wireDictionary[operand1] = {"value": None, "resolved": False}
               
                # if operation is "AND", "OR", "LSHIFT", "RSHIFT", operand1 is the previous part and operand2 is the next part
                else:
                    operation = parts[i]
                    operand1 = parts[i-1]
                    operand2 = parts[i+1]
                    # if operand1 and operand2 is not a digit, add it as a wire to the wireDictionary
                    if not operand1.isdigit(): wireDictionary[operand1] = {"value": None, "resolved": False}
                    if not operand2.isdigit(): wireDictionary[operand2] = {"value": None, "resolved": False}
            # 
            elif (parts[i] == "->"):
                # if the instruction is 3 parts, the operation is None and operand1 is the previous part and operand2 is None
                if len(parts) == 3:
                    operation = None
                    operand1 = parts[i-1]
                    operand2 = None
                    wire = parts[i+1]
                    # the part after the "->" is always a wire
                    wireDictionary[wire] = {"value": None, "resolved": False}
                    break
                # The part after the "->" is always a wire
                else:
                    wire = parts[i+1]
                    wireDictionary[wire] = {"value": None, "resolved": False}
                    break
        
        instructionDictionary[wire] = {"operation": operation,"operand1": operand1,"operand2": operand2}
    
    return instructionDictionary

def resolve_wire(wire,instructionDictionary):
    global wireDictionary

    if wireDictionary[wire]["resolved"]:
        return
    
    if wire in instructionDictionary:
        instruction = instructionDictionary[wire]
        operation = instruction["operation"]
        operand1 = instruction["operand1"]
        operand2 = instruction["operand2"]
    else:
        return

    print(f"Resolving wire: {wire} operation: {operation} operand1: {operand1} operand2: {operand2}")

    # Resolve operands
    # Operand1 always need to be resolved
    # Operand2 needs to be resolved if it is not None 
    # 1: check if it is None
    # 2: chekk if it is a digit
    # 3: check if it is in the wireDictionary and resolved
    # 4: if not, return

    # resolve operand1
    if operand1 is None:
        return
    elif operand1.isdigit(): 
        operand1Value = int(operand1)
    elif operand1 in wireDictionary and wireDictionary[operand1]["resolved"]:
        operand1Value = int(wireDictionary[operand1]["value"])
    else: 
        return
    
    # resolve operand2
    if operand2 is not None:
        if operand2.isdigit():
            operand2Value = int(operand2)
        elif operand2 in wireDictionary and wireDictionary[operand2]["resolved"]:
            operand2Value = int(wireDictionary[operand2]["value"])
        else: 
            return

    # Perform operation
    if operation == "AND":
        value = operand1Value & operand2Value
    elif operation == "OR":
        value = operand1Value | operand2Value
    elif operation == "LSHIFT":
        value = operand1Value << int(operand2)
    elif operation == "RSHIFT":
        value = operand1Value >> int(operand2)
    elif operation == "NOT":
        value = ~operand1Value & 0xFFFF
    else:
        value = int(operand1Value)
    
    # Store the resolved value
    wireDictionary[wire]["value"] = value
    wireDictionary[wire]["resolved"] = True
    return
        


instructionDictionary = {}
instructionDictionary = parse_instructions(inputString)

# Part 2
wireDictionary["b"]["value"] = 3176
wireDictionary["b"]["resolved"] = True

# Keep iterating until all wires in wireDictionary are resolved
while not all(wireDictionary[wire]["resolved"] for wire in wireDictionary):
    for wire in instructionDictionary:
        counter += 1
        print(counter)
        resolve_wire(wire, instructionDictionary)

# Print the final results
for wire in wireDictionary:
    print(f"{counter} wire: {wire} value {wireDictionary[wire]['value']} resolved: {wireDictionary[wire]['resolved']}")

print(wireDictionary["a"]["value"])

