<?php
$input_directions = str_split(file_get_contents('/Users/maxnerdal/Documents/adventofcode/2015/input/2015_day_1_input.txt'));

// Part one
function getFloor($input_directions) {
    $output_floor = 0;
    foreach ($input_directions as $char) { if ($char == "(") { $output_floor++; } elseif ($char == ")") { $output_floor--;} }
    return $output_floor;
}

echo "The final floor is: " . getFloor($input_directions) . "\n";

// Part two
function getNumberOfDirections($input_directions) {
    $output_floor = 0;
    $output_counter_directions = 0;
    foreach ($input_directions as $char) { 
        $output_counter_directions++;
        if ($char == "(") { $output_floor++; } elseif ($char == ")") { $output_floor--;}  
        if ($output_floor == -1) { break; }
    }
    return $output_counter_directions;
}

echo "The first time the basement is reached is at position: " . getNumberOfDirections($input_directions) . "\n"; 
