<?php
	define('DBNAME','progettogpoi');
	define('DBHOST','localhost');
	define('DBUSER','adminZizzo');
	define('DBPASS','CiaoMondo1');
	
	$con = new mysqli(DBHOST,DBUSER,DBPASS,DBNAME);
	
	if($con->connect_errno){
		$codice = $con->connect_errno;
		$descErrore = $con->connect_error;
		die("Errore connection: $codice - $descErrore");
	}
	
	echo "Accesso";
?>