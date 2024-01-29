<?php
    require_once('./controllers/NewsController.php');

    $action = !empty($_GET['action']) ? $_GET['action'] : 'getAllNews';

    
    $controller = new NewsController();
    $controller->{$action}();

?>