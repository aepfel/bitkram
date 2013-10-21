<html>
 <head>
  <title>bitmessage-bouncer</title>
  <style type="text/css">
    #footer {
    position:fixed;
    bottom:0px;
}
</style>
 </head>
 <body>
<?php
        $clip = $_GET['clip'];
        $link = mysql_connect('localhost', 'root', 'aeaeae');
        if (!$link) {
         die('Verbindung schlug fehl: ' . mysql_error());
        }
        //echo 'Erfolgreich verbunden';
        mysql_select_db('bm');
        $sql = "SELECT txt FROM clip WHERE clipadd='".$clip."';";
        //echo $sql;
        $result = mysql_query($sql);
        if($result === FALSE) {
         die(mysql_error()); // TODO: better error handling
        }
        while($row = mysql_fetch_array($result))
        {
         $txt=$row[0];
        }
        echo "<h1><a href=clipb.php?clip=".$clip.">".$clip."</a></h1>";
        
        mysql_close($link);
        //echo "<p>msgid:".$msgid."</p>";
?>
 
<p id="footer">funktion :: anderes projekt :: anderes projekt :: etc <br>donationsadresse</p>
</body>
</html>
