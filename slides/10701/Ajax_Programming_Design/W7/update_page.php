<?php

echo "Welcome ~ ". $_POST["name"]."<br>";
echo "Your email address is: ".$_POST["email"]."<br>";


$servername = "localhost";
$username = "root";
$password = "";
$dbname = "1027";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "UPDATE personalinformation SET email = '".$_POST["email"]."' WHERE id = 1";

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

?>
