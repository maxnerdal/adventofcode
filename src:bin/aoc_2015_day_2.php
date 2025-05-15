<?php

$input_dimensions_array = explode("\n",file_get_contents('/Users/maxnerdal/Documents/adventofcode/2015/input/2015_day_2_input.txt'));
//$input_dimensions_array = explode("\n","2x3x4
//1x1x10");

// Part one
function getArea($dimension) {
    if (trim($dimension," \n\r") === "") {
        return 0;
    }
    $single_dimension_array = explode("x",$dimension);
    $l = trim($single_dimension_array[0]);
    $w = trim($single_dimension_array[1]);
    $h = trim($single_dimension_array[2]);

    $area = 2*$l*$w + 2*$w*$h + 2*$h*$l;
 
    $area = $area + min($l*$w, $w*$h, $h*$l);

    return $area;
}

// Part two
function getLenght($dimension) {
    if (trim($dimension," \n\r") === "") {
        return 0;
    }
    $single_dimension_array = explode("x",$dimension);
    $l = trim($single_dimension_array[0]);
    $w = trim($single_dimension_array[1]);
    $h = trim($single_dimension_array[2]);

    $length = $l * $w * $h;
    
    sort($single_dimension_array); // Sorts in ascending order
    $smallest = $single_dimension_array[0];
    $smallest2 = $single_dimension_array[1];
    
    $length = $length + 2*$smallest + 2*$smallest2;
   
    return $length;
}

$area = 0;
$length = 0;
foreach ($input_dimensions_array as $input) { 
    $area = $area + getArea($input); 
    $length = $length + getLenght($input);
}

echo "The total area is: " . $area . "\n";
echo "The total length is: " . $length . "\n";