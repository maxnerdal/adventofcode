<?php
$inputDirectionList = str_split(file_get_contents('/Users/maxnerdal/Documents/adventofcode/2015/input/2015_day_3_input.txt'));

//$inputDirectionList = str_split('^v^v^v^v^v'); // Test input
//print_r($housesVisited);


// Part one
function getHouses($input) {
    
    $housesVisitedList = [[0,0]]; // Initialize the array with the starting position
    $housesVisited = 1; // Access global variables
    $counter = 1; // Initialize counter
    $x = 0; // Initialize x coordinate
    $y = 0; // Initialize y coordinate

    foreach ($input as $inputDirection) 
    { 
        if      ($inputDirection == ">") { $x++; } 
        elseif  ($inputDirection == "<") { $x--; } 
        elseif  ($inputDirection == "^") { $y++; } 
        elseif  ($inputDirection == "v") { $y--; }
    
        // Check if the house has been visited
        if (in_array([$x, $y],$housesVisitedList) == false) { $housesVisited++;};
        // insert the coordinates into the array
        $housesVisitedList[] = [$x, $y];
    }

    return $housesVisited;
 
}

echo "The number of houses visited is: " . getHouses($inputDirectionList) . "\n";


// Part two
function getHousesWithRobot($input) {
    
    $housesVisitedList = [[0,0],[0,0]]; // Initialize the array with the starting position
    $housesVisited = 1; // Access global variables
    $counter = 0; // Initialize counter
    $xSanta = 0; // Initialize x coordinate
    $ySanta = 0; // Initialize y coordinate
    $xRobot = 0; // Initialize x coordinate
    $yRobot = 0; // Initialize y coordinate

    foreach ($input as $inputDirection) 
    { 
        if($counter % 2 == 0) { // Santa
            if      ($inputDirection == ">") { $xSanta++; } 
            elseif  ($inputDirection == "<") { $xSanta--; } 
            elseif  ($inputDirection == "^") { $ySanta++; } 
            elseif  ($inputDirection == "v") { $ySanta--; }
            // Check if the house has been visited
            if (in_array([$xSanta, $ySanta],$housesVisitedList) == false) { $housesVisited++;};
            // insert the coordinates into the array
            $housesVisitedList[] = [$xSanta, $ySanta];
        } else { // Robot
            if      ($inputDirection == ">") { $xRobot++; } 
            elseif  ($inputDirection == "<") { $xRobot--; } 
            elseif  ($inputDirection == "^") { $yRobot++; } 
            elseif  ($inputDirection == "v") { $yRobot--; }
            // Check if the house has been visited
            if (in_array([$xRobot, $yRobot],$housesVisitedList) == false) { $housesVisited++;};
            // insert the coordinates into the array
            $housesVisitedList[] = [$xRobot, $yRobot];
        }
        $counter++; // Increment counter
    }

    return $housesVisited;
 
}

echo "The number of houses visited with robot: " . getHousesWithRobot($inputDirectionList) . "\n";