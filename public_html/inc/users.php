<?php
// users.php
ini_set('session.use_cookies', 1);
ini_set('session.use_only_cookies', 1);
ini_set('session.use_cookie_httponly', 1);
ini_set('session.save_path', 'sesje');

class User {
    var $uVal = 'uval';
    var $remTime = 7200; // 2h
    var $remCookieDomain = '';
    var $remCookieName = 'sqlDB';
    var $keys = array('uid', 'login', 'haslo', 'email', 'datad');
    var $dane = array();
    var $kom = array();
    
    function __construct() {
        $this->remCookieDomain = $this->remCookieDomain == '' ? $_SERVER['HTTP_HOST'] : $this->remCookieDomain;
        if (!isset($_SESSION)) session_start();
        return;
        if (!empty($_SESSION[$this->uVal])) $this->is_user($_SESSION[$this->uVal]);
        if (isset($_COOKIE[$this->remCookieName])  && !$this->uid) {
            $u = unserialize(base_64_decode($_COOKIE[$this->remCookieName]));
            $this->login($u['login'], $u['haslo'], false, true);
        }
    }
    
    
    
    function login($login, $haslo, $remember=false, $loadUser=true) {
		$login = rescape($login);
		$haslo = rescape($haslo);
		if ($loadUser && $this->is_user('',$login,$haslo)) {
			if ($remember) { // zapisanie ciasteczka
			  $cookie = base64_encode(serialize(array('login'=>$login,'haslo'=>$haslo,'czas'=>time())));
			  $a = setcookie($this->remCookieName,$cookie,time()+$this->remTime,'/',$this->remCookieDomain,false,true);
			}
			$this->kom[]='Witaj '.$login.'! Zostałeś zalogowany.';
			return true;
		}
		$this->kom[]='<b>Błędny login lub hasło!</b>';
		return false;
}
    
    function is_user($sid,$login=NULL,$haslo=NULL) {
		if (!empty($login)) {
			$qstr='SELECT * FROM users WHERE login = \''.$login.'\' AND haslo = \''.sha1($haslo).'\' LIMIT 1';
		} else return false;
		$ret=array();
		db_query($qstr,$ret);
		if (!empty($ret[0])) {
			$this->dane=array_merge($this->dane,$ret[0]);
			$sid=sha1($this->uid.$this->login.session_id());
			$_SESSION[$this->uVal] = $sid;
			return true;
		}
		return false;
}
    
    function __set($k, $v) {
        $this->dane[$k] = $v;
    }
    
    function __get($k) {
        if (array_key_exists($k, $this->dane))
            return $this->dane[$k];
        else
            return null;
    }
    
}

$u = new User();
$u->login = 'romek';
echo $u->login."\n";
echo $u->email;

?>
