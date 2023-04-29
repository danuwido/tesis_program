<?php
#$output =  shell_exec("python phyton/app.py");
#echo $output;

exec("python phyton/app.py", $output, $ret_code);
for($i=0;$i<count($output);$i++){
    echo $i." = ".$output[$i][1]."\n";
} 


var_dump($output);
?>