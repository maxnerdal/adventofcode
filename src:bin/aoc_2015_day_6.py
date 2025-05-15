#!/usr/bin/env python3

"""
turn on 887,9 through 959,629
turn on 454,398 through 844,448
turn off 539,243 through 559,965
turn off 370,819 through 676,868
"""
InputInstructions = open('/Users/maxnerdal/documents/AdventOfCode/2015/input/2015_day_6_input.txt').read()
#InputInstructions = "turn on 887,9 through 959,629"

# Part One
def create_grid():
    grid = {}
    for x in range(1000):  # Iterate over the x-axis (0 to 999)
        for y in range(1000):  # Iterate over the y-axis (0 to 999)
            grid[(x, y)] = {"status": "off", "x": x, "y": y}  # Initialize each coordinate
    return grid

# Part Two
def create_grid_brightness():
    gridBrightness = {}
    for x in range(1000):  # Iterate over the x-axis (0 to 999)
        for y in range(1000):  # Iterate over the y-axis (0 to 999)
            gridBrightness[(x, y)] = {"brightness": 0, "x": x, "y": y}  # Initialize each coordinate
    return gridBrightness

def parse_instructions(InputInstructions):
    instructionsDictionary = []
    for line in InputInstructions.splitlines():
        parts = line.split()
        
        if parts[0] == "turn":
            action = parts[1]
            x1, y1 = map(int, parts[2].split(","))
            x2, y2 = map(int, parts[4].split(","))
        elif parts[0] == "toggle":
            action = parts[0]
            x1, y1 = map(int, parts[1].split(","))
            x2, y2 = map(int, parts[3].split(","))
        
        
        instructionsDictionary.append({
            "action": action,
            "coordinateOne": {"x": x1, "y": y1},
            "coordinateTwo": {"x": x2, "y": y2}
        })
    
    return instructionsDictionary

def execute_instructions(instructionsDictionary):

    global grid
    global gridBrightness

    #itterate instructions
    for instruction in instructionsDictionary:
        
        x1 = instruction["coordinateOne"]["x"]  # Fetch x for coordinateOne
        x2 = instruction["coordinateTwo"]["x"]  # Fetch x for coordinateTwo
        y1 = instruction["coordinateOne"]["y"]  # Fetch y for coordinateOne
        y2 = instruction["coordinateTwo"]["y"]  # Fetch y for coordinateTwo
        action = instruction["action"]

        #itterate x-axel
        for x in range(x1, x2+1):
            #itterate y-axel
            for y in range(y1, y2+1):
                if action == "on":
                    grid[(x, y)]["status"] = "on" #Part One
                    gridBrightness[(x, y)]["brightness"] += 1 #Part Two 
                elif action == "off":
                    grid[(x, y)]["status"] = "off" #Part One
                    if(gridBrightness[(x,y)]["brightness"] > 0): 
                        gridBrightness[(x, y)]["brightness"] -= 1 #Part Two
                elif action == "toggle":
                    gridBrightness[(x, y)]["brightness"] += 2 #Part Two
                    if grid[(x, y)]["status"] == "on":
                        grid[(x, y)]["status"] = "off" #Part One
                    else:
                        grid[(x, y)]["status"] = "on" #Part One
        


instructionsDictionary = parse_instructions(InputInstructions)
grid = create_grid()
gridBrightness = create_grid_brightness()
execute_instructions(instructionsDictionary)

CountLightsOn = sum(1 for light in grid.values() if light["status"] == "on")
CountLightBrightness = sum(light["brightness"] for light in gridBrightness.values())

print(f"Count of lights on: {CountLightsOn}")
print(f"Count total brightness of lights on: {CountLightBrightness}")




