<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Felipe Deschamps Newsletter for WeB</title>
</head>
<body>
    <h1>News</h1>
    <div class="content">
        <?php foreach ($resultData as $data): ?>
            

        <div>
            <h3><?= $converted_news_date= date("d-m-Y", strtotime($data['news_date'])); ?></h3>
            <p><?= $data['news_text']?><p>
        </div>
        <br>
        <?php endforeach; ?>
    </div>
</body>
</html>