from flask import Flask

app = Flask(__name__)

# ---------- ГЛАВНАЯ ----------
@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
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

    .card {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        margin: 20px auto;
        width: 300px;
        border-radius: 15px;
    }

    a {
        color: #60a5fa;
        text-decoration: none;
        font-size: 20px;
    }

    a:hover {
        color: #3b82f6;
    }
</style>
</head>

<body>

<div class="header">Milton Team?</div>

<div class="container">

    <h1>Добро пожаловать 👋</h1>

    <div class="card">
        <a href="/cars">🚗 Автопарк</a>
    </div>

    <div class="card">
        <a href="/rules">📜 Правила</a>
    </div>

    <div class="card">
        <a href="/family">👨‍👩‍👧 Семья</a>
    </div>

</div>

</body>
</html>
"""

# ---------- АВТОПАРК ----------
@app.route("/cars")
def cars():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Автопарк</title>
</head>

<body style="background:#0b1220; color:white; text-align:center; font-family:Arial;">

<h1>🚗 Автопарк</h1>

<div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Lamborghini_Aventador_LP700-4_%282%29.jpg" width="250">
    <h3>Машина 1</h3>
</div>

<div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/BMW_M4_Competition_G82.jpg" width="250">
    <h3>Машина 2</h3>
</div>

<div>
    <h3>Машина 3</h3>
</div>

<div>
    <h3>Машина 4</h3>
</div>

<div>
    <h3>Машина 5</h3>
</div>

<br>
<a href="/" style="color:#60a5fa;">⬅ Назад</a>

</body>
</html>
"""

# ---------- ПРАВИЛА ----------
@app.route("/rules")
def rules():
    return """
<!DOCTYPE html>
<html>
<body style="background:#0b1220; color:white; text-align:center; font-family:Arial;">

<h1>📜 Правила</h1>

<p>1. Запрещено оскорблять игроков семьи за это вы получите выговор, за мамкоёбство вы получите увал + чс.</p>
<p>2. Запрещено дм союзов и игроков семьи за это вы получите выговор/увал →[в зависимости от нарушения]</p>
<p>3. Запрещено выгружать транспорт семьи, без предупреждения (пример → [выгружаю "имя транспорта" и отсчёт от 1 до 5 секунд] за нарушение вы получите выговор.</p>

<br>
<a href="/" style="color:#60a5fa;">⬅ Назад</a>

</body>
</html>
"""

# ---------- СЕМЬЯ ----------
@app.route("/family")
def family():
    return """
<!DOCTYPE html>
<html>
<body style="background:#0b1220; color:white; text-align:center; font-family:Arial;">

<h1>👨‍👩‍👧 Семья</h1>

<p>Лидер: Angel_Andegraund</p>
<p>Замы: ...</p>
<p>Участники: ...</p>

<br>
<a href="/" style="color:#60a5fa;">⬅ Назад</a>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
