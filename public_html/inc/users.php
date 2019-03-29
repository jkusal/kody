<?php
// users.php
ini_set('session.use_cookies', 1);
ini_set('session.use_only_cookies', 1);
ini_set('session.use_cookie_httponly', 1);
ini_set('session.save_path', 'sesje');

class User {
	var $uVal = 'uval';
	var $remTime = 7200; // 2 godz.
	var $remCookieDomain = '';
	var $remCookieName = 'sqlDB';
	var $keys = array('id', 'login', 'haslo', 'email', 'datad');
	var $dane = array();
	var $kom = array();

	function __construct() {
		$this->remCookieDomain = $this->remCookieDomain == '' ? $_SERVER['HTTP_HOST'] : $this->remCookieDomain;
		if (!isset($_SESSION)) session_start(); // rozpoczęcie sesji

		if (!empty($_SESSION[$this->uVal]))
			$this->is_user($_SESSION[$this->uVal]);
		if (isset($_COOKIE[$this->remCookieName]) && !$this->id) {
			$u = unserialize(base64_decode($_COOKIE[$this->remCookieName]));
			$this->login($u['login'], $u['haslo'], false, true);
		}

		if (!$this->id && isset($_POST['loguj'])) {
			$n = clrtxt($_POST['login']);
			$h = clrtxt($_POST['haslo']);
			$this->login($n, $h, true, true);
		}

		if (isset($_GET['unlog'])) $this->logout();

	}

	function login($login, $haslo, $remember=false, $loadUser=true) {
		$login = rescape($login);
		$haslo = rescape($haslo);
		if ($loadUser && $this->is_user('',$login,$haslo)) {
			if ($remember) { // zapisanie ciasteczka
			  $cookie = base64_encode(serialize(array('login'=>$login,'haslo'=>$haslo,'czas'=>time())));
			  $a = setcookie($this->remCookieName,$cookie,time()+$this->remTime,'/',$this->remCookieDomain,false,true);
			}
		} else {
				$this->kom[]='<b>Błędny login lub hasło!</b>';
				return false;
		}
		if ($remember) {
			$this->kom[]='Witaj '.$login.'! Zostałeś zalogowany.';
			return true;
		}
	}

	function logout($redirectTo = '') {
		setcookie($this->remCookieName,'', time()-($this->remTime*3),'/',$this->remCookieDomain,false,true);
		$this->dane=array();
		$_SESSION = array();
		if (ini_get("session.use_cookies")) {
    		$params = session_get_cookie_params();
    		setcookie(session_name(),'',time()-($this->remTime*3),$params["path"], $params["domain"],$params["secure"],$params["httponly"]);
		}
		if (session_destroy()) $this->kom[]='Zostałeś wylogowany.';
		if ($redirectTo != '' && !headers_sent()) {//ewentualne przekierowanie
			header('Location: '.$redirectTo);
			exit;//To ensure security
		}
	}

	function is_user($sid,$login=NULL,$haslo=NULL) {
		if (!empty($login)) {
			$qstr='SELECT * FROM users WHERE login = \''.$login.'\' AND haslo = \''.sha1($haslo).'\' LIMIT 1';
		} else return false;
		$ret=array();
		db_query($qstr,$ret);
		if (!empty($ret[0])) {
			$this->dane=array_merge($this->dane,$ret[0]);
			$sid=sha1($this->id.$this->login.session_id());
			$_SESSION[$this->uVal] = $sid; // zapis identyfikatora sesji
			return true;
		}
		return false;
	}

  function savtb() {//tab. asocjacyjna z kluczami: id#nick#haslo#email#datad
		if (strlen($this->haslo)<40) $this->haslo=sha1($this->haslo);
		$this->llog=time();
		if (!$this->id) {
			$qstr='INSERT INTO users VALUES (NULL,\''.$this->login.'\',\''.$this->haslo.'\',\''.$this->email.'\',time())';
			$ret=db_exec($qstr);
			$id = db_lastInsertID();
		}
		if ($ret) return true;
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

	function is_login($login) {
		$qstr='SELECT id FROM users WHERE login=\''.$login.'\' LIMIT 1';
    if (db_query($qstr)) return true;
    return false;
	}

	function is_email($email) {
		$qstr='SELECT id FROM users WHERE email=\''.$email.'\' LIMIT 1';
    if (db_query($qstr)) return true;
    return false;
	}

	function get_koms() {
    foreach ($this->kom as $k) echo '<p class="lead">'.$k.'</p>';
    $this->kom = array();
	}

}

?>