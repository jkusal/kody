<?php
setlocale(LC_ALL, "pl_PL.UTF-8");
date_default_timezone_set('Europe/Warsaw');
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('log_errors', 1);
ini_set('error_log', 'errorlog.txt');
define('DINC', '/inc');
require_once(DINC.'functions.php');
//todo: zdefiniować id

if (isset($_GET['id'])) $id=$_GET['id'];
else $id='witam';


include_once(DINC.'template.php');
?>
