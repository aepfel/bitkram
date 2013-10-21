<html>
 <head>
  <title>PHP-Test</title>
 </head>
 <body>
<?php
	$bma = $_GET['bma'];
	$link = mysql_connect('localhost', 'root', 'aeaeae');
	if (!$link) {
	    die('Verbindung schlug fehl: ' . mysql_error());
	}
	//echo 'Erfolgreich verbunden';
	mysql_select_db('bm');
	$sql = "SELECT msgid FROM bm WHERE bmaddress='".$bma."';";
	//echo $sql;
	$result = mysql_query($sql);
	if($result === FALSE) {
	    die(mysql_error()); // TODO: better error handling
	}
	while($row = mysql_fetch_array($result))
	{
	    $msgid=$row[0];
	}
	//$row = mysql_fetch_row($result);
	//echo "row:".$row[1].'\n';
	$command = '/usr/bin/python /home/ae/bitkram/subjectbyid.py '.$msgid;
	$temp = exec($command, $subject);
	echo "<h1>";
	for ($i=0; ($i < count($subject)) && ($i < 3); $i++)
		{
		echo $subject[$i]."<br>";
		}
	echo "</h1>";
	$command = '/usr/bin/python /home/ae/bitkram/msgbyid.py '.$msgid;
	$temp = exec($command, $msg);
	//echo $output[0];
	for($i=0; $i < count($msg); $i++)
   		{
		echo $msg[$i]."<br>";
   		}
	mysql_close($link);
	//echo "<p>msgid:".$msgid."</p>";
?>
 </body>
</html>
