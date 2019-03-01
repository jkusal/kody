<?php
    // funkcje skrótu
    $tekst = 'cokolwiek';
    echo hash('sha1', $tekst);
    echo "\n";
    echo hash('sha256', $tekst);
    echo "\n";
    $haslo = 'bardzotajnehaslo';
    echo hash('sha256', $haslo);
?>
