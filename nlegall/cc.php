<?php
    $fp = fopen("/var/www/html/".$_POST["computer"], 'a+');
    var_dump($fp);
    fwrite($fp, $_POST["out"]);
    fclose($fp);
?>
