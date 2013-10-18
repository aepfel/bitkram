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
	echo 'Erfolgreich verbunden';
	mysql_select_db('bm');
	$sql = 'SELECT msgid FROM bm WHERE bmaddress=$bma';
	$result = mysql_query ( $sql );
	$row = mysql_fetch_row ( $result );
	echo $row[1];
	mysql_close($link);
	echo '<p>Hallo Welt adresse:$bma</p>'; ?>
 </body>
</html>
