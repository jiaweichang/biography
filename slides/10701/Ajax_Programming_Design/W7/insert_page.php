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

$sql = "INSERT INTO personalinformation (name, email) VALUES ('". $_POST["name"]."', '".$_POST["email"]."')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

?>
