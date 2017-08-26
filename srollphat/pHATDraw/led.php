<?php

$data = $_POST["data"];
$brightness = $_POST["brightness"];

echo exec ("sudo /var/www/html/led.py '$data' $brightness");
