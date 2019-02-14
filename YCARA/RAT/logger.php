<?php

if (isset($_GET['log']))
{
	if (!empty($_GET['log']))
	{
		$log = $_GET['log'] . "\n";
		$file = fopen("./log.txt", "a+");
		fwrite($file, $log);
		fclose($file);
	} else {
		echo 'Empty param log';
	}
} else {
	echo 'No log param provided';
}
