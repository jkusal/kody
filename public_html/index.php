<?php
setlocale(LC_ALL, 'pl_PL.UTF-8');
date_default_timezone_set('Europe/Warsaw');
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('log_errors', 1);
ini_set('error_log', 'errorlog.txt');

define('DINC', 'inc/');
define('DBASE', 'baza/');
$dbfile = 'db.sqlite3';
$db=null;
require_once(DINC.'functions.php');
require_once(DINC.'db.php');
$kom=array();

init_baza(DBASE.$dbfile);
init_tables();

require_once(DINC.'users.php');
$user = new User(); // tworzenie obiektu użytkownika

if (isset($_GET['id'])) $id=$_GET['id']; else $id='witam';

include_once(DINC.'template.php');
?>
