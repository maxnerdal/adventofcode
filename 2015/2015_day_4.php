<?php
$inputSecretKey = trim(file_get_contents('/Users/maxnerdal/Documents/adventofcode/2015/input/2015_day_4_input.txt'));

// Part one
function getLowestPossibleNumber($input, $zerosInt) 
{
    //$input = "bgvyzdsv";
    $zerosString = "";
    if($zerosInt === 5) { $zerosString = "00000"; }
    else if($zerosInt === 6) { $zerosString = "000000"; }
    else { return -1;}
   
    echo $zerosInt . "\n";
    echo $zerosString . "\n";

    $md5Hash = "";
    for( $i = 0; $i < 10000000000; $i++) 
    {
        $md5Hash = md5($input . $i);
        if(substr($md5Hash, 0, $zerosInt) === $zerosString) { echo $md5Hash; return $i; } 
    }

    return -1; // This should never happen  
   
}


echo "Lowest possible number after secretkey with 5 zeros:" . getLowestPossibleNumber($inputSecretKey, 5) . "\n";
echo "Lowest possible number after secretkey with 6 zeros:" . getLowestPossibleNumber($inputSecretKey, 6) . "\n";