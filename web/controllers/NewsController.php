<?php
    require_once('./models/News.php');

    Class NewsController{
        private $model;

        function __construct(){
            $this->model = new NewsModel();
        }

        function getAllNews(){
            $resultData = $this->model->getAllNews();
            require_once('./views/index.php');
        }
    }

?>