<!DOCTYPE html>

<head>
<link rel="stylesheet" type="text/css" href="main.css">

</head>

<body>

<?php
$servername = "localhost";
$username = "*******";
$password = "********";
$dbname = '*********';

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname, $port);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * 
FROM  `current_Weather` ";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        $temp = $row["currentTemperature"];
        $humidity = $row["currentHumidity"];
        $pressure = $row["currenPressure"];
    }
} else {
    echo "0 results";
}
$conn->close();
 
   // Use variables to insert the data into, such as $temp, $humidity, and etc

    

    echo '<p class="weatherHeaderText">WEATHER IN ********</p>';
    
    echo '<div class="table">';
        echo'<ul id="horizontal-list">';
            echo '<li>';
                echo '<ul class="weatherDiv">';
                    echo '<li class="weatherSubHeaderText">Temperature:</li>';
                    echo '<li class="weatherDataText">'.$temp.'</li>';   
                echo '</ul>';
            echo '</li>';
            echo '<li>';
                echo '<ul class="weatherDiv">';
                    echo '<li class="weatherSubHeaderText">Humidity:</li>';
                    echo '<li class="weatherDataText">'.$humidity.'</li>';
                echo '</ul>';
            echo '</li>';
            echo '<li>';
                echo '<ul class="weatherDiv">';
                    echo '<li class="weatherSubHeaderText">Pressure:</li>';
                    echo '<li class="weatherDataText">'.$pressure.'</li>';
                echo '</ul>';
            echo'</li>';
        echo'</ul>';
    echo '</div>';
?>
  
</body>
