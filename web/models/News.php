 <?php 
   require_once('./configuration/connect.php');
    
    class NewsModel extends Connect{
        private $table;

        function __construct(){
            parent::__construct();
            $this->table = 'news';
        }

        function getAllNews(){
            $sqlSelect = $this -> connection->query("SELECT id, news_text, news_date FROM ".$this->table);
            return $resultQuery = $sqlSelect->fetchAll();
        }
        
    }
?>