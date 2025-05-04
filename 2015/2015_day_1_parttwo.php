<?php
$input_upordown = file_get_contents('/Users/maxnerdal/Documents/adventofcode/2015/input/2015_day_1_input.txt');
$output_floor = 0;
$output_counter_directions = 0;

$input_upordown = str_split($input_upordown);

foreach ($input_upordown as $char) {
    
    $output_counter_directions++;

    if ($char === "(") {
        $output_floor++;
    } elseif ($char === ")") {
        $output_floor--;
    }

    if ($output_floor === -1 )
    {
        break;
    }

}

echo "The first time the basement is reached is at position: " . $output_counter_directions . "\n"; 



