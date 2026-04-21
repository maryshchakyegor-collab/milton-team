from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Milton Family</title>

<style>
    body {
        margin: 0;
        font-family: Arial;
        background: #0b1220;
        color: white;
    }

    .header {
        background: #111827;
        padding: 20px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #60a5fa;
    }

    .container {
        padding: 40px;
        text-align: center;
    }

    h1 {
        font-size: 40px;
    }

    .card {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        margin: 20px auto;
        width: 300px;
        border-radius: 15px;
    }

    .btn {
        display: inline-block;
        margin-top: 20px;
        padding: 10px 20px;
        background: #3b82f6;
        color: white;
        text-decoration: none;
        border-radius: 10px;
    }

    .btn:hover {
        background: #2563eb;
    }
</style>

</head>

<body>

<div class="header">
    MILTON_TEAM?
</div>

<div class="container">
    <h1>Добро пожаловать 👋</h1>
    <p>Информация о семье, автопарк и правила</p>

    <div class="card">
        <h3>🚗 Автопарк</h3>
        <p>Список автомобилей семьи</p>
    </div>

    <div class="card">
        <h3>📜 Правила</h3>
        <p>Правила семьи и поведения</p>
    </div>

    <div class="card">
        <h3>👨‍👩‍👧 Семья</h3>
        <p>Участники и ранги</p>
    </div>

    <a class="btn" href="#">Поддержка</a>
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)