<?php
include "config.php";
$con = mysqli_connect("localhost", "sqlctf", "sqlctfwillamete", "sqlctf");
$username = mysqli_real_escape_string($con, $_POST["username"]);
$password = mysqli_real_escape_string($con, $_POST["password"]);
$query = "SELECT * FROM users WHERE username='$username'";
$result = mysqli_query($con, $query);

if (mysqli_num_rows($result) !== 1) {
  echo "<h1>Login failed.</h1>";
  echo "<a href='index.php'>back</a>";
} else {
  echo "<h1>Logged in! Welcome admin</h1>";
  echo "<p>Your flag is: $FLAG</p>";
  echo "<a href='index.php'>back</a>";
}

?>
