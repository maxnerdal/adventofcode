<?php
$input_upordown = file_get_contents('/Users/maxnerdal/Documents/adventofcode/2015/input/2015_day_1_input.txt');
$output_floor = 0;

$input_upordown = str_split($input_upordown);

foreach ($input_upordown as $char) {
    if ($char == "(") {
        $output_floor++;
    } elseif ($char == ")") {
        $output_floor--;
    }
}

echo "The final floor is: " . $output_floor . "\n";



