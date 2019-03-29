<?php

$pages = array(
    'witam' => 'Witamy',
    'baza' => 'Baza',
    'formularz' => 'Formularz'
);

function get_page_title($id) {
    global $pages;
    if (array_key_exists($id, $pages))
        echo $pages[$id];
    else
        echo 'Aplikacja w PHP';
}

function get_menu($id) {
    global $pages, $user;
    foreach ($pages as $p => $t) {
        echo '
            <li class="nav-item">
                <a class="nav-link js-scroll-trigger" href="?id='.$p.'">'.$t.'</a>
            </li>';
    }
    if ($user->id) {
        echo '
            <li class="nav-item">
                <a class="nav-link js-scroll-trigger" href="?id=wyloguj">Wyloguj</a>
            </li>';
    } else {
        echo '
            <li class="nav-item">
                <a class="nav-link js-scroll-trigger" href="?id=login">Zaloguj się</a>
            </li>';
    }
}

function get_page_content($id) {
    if (file_exists($id.'.html'))
        include($id.'.html');
    else
        echo '<p>Brak takiej strony!</p>';
}

function get_koms() {
    global $kom;
    // foreach ($tb as $k) echo '<p>'.$k.'</p>';
    foreach ($kom as $k) echo '<p class="lead">'.$k.'</p>';
}

function clrtxt(&$el, $maxdl=30) {
    if (is_array($el)) {
        return array_map('clrtxt', $el);
    } else {
        $el = trim($el);
        $el = substr($el, 0, $maxdl);
        if (get_magic_quotes_gpc()) $el = stripslashes($el);
        $el = htmlspecialchars($el, ENT_QUOTES);
        return $el;
    }
}

function rescape($str) {
    if (!($isa=is_array($str))) $str=array($str);
    foreach ($str as $k => $w) $str[$k] = get_magic_quotes_gpc() ? stripslashes($w) : $w;
    if (!$isa) return $str[0]; else return $str;
}

?>
