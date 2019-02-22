<?php
$pages = array(
    'witam' => 'Witamy',
    'baza' => 'Baza',
    'formularz' => 'Formularz',
    'login' => 'Logowanie',
);

function get_menu(&id) {
    global $pages;
    foreach ($pages as $p => $t) {
        echo '
            <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="?id='.$p.'">'.$t.'</a>
            </li>';
    }
}

function get_page_content($id) {
    if (file_exists($id.'.html'))
        include($id.'.html');
    else
        echo '<p>Brak takiej strony!</p>';
}
?>
