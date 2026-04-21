import os

from flask import Flask, abort, render_template_string

app = Flask(__name__)

ESSAYS = {
    "technology": {
        "title": "The Role of Technology in Education",
        "content": (
            "Technology has transformed education by making information more accessible, "
            "supporting interactive learning, and connecting classrooms across the world. "
            "When used thoughtfully, digital tools can improve both teaching quality and "
            "student engagement."
        ),
    },
    "environment": {
        "title": "Why Environmental Protection Matters",
        "content": (
            "Protecting the environment is essential for public health, economic stability, "
            "and future generations. Actions such as reducing waste, conserving energy, and "
            "preserving forests help maintain the natural balance that supports life on Earth."
        ),
    },
    "teamwork": {
        "title": "The Importance of Teamwork",
        "content": (
            "Teamwork allows people with different strengths to solve problems more effectively. "
            "In schools and workplaces, collaboration builds communication skills, trust, and "
            "shared responsibility, often leading to better outcomes than individual effort alone."
        ),
    },
}

INDEX_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Essay Topics</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
        }
        header {
            text-align: center;
            color: white;
            padding: 40px 20px;
        }
        header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        .essays-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }
        .essay-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-decoration: none;
            color: inherit;
            display: block;
        }
        .essay-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.15);
        }
        .essay-card-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .essay-card-header h2 {
            font-size: 1.3em;
        }
        .essay-card-body {
            padding: 20px;
            text-align: center;
            color: #666;
        }
        .essay-card-body p {
            font-size: 0.95em;
            margin-bottom: 15px;
        }
        .read-btn {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 10px 25px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s ease;
        }
        .read-btn:hover {
            background: #764ba2;
        }
        footer {
            text-align: center;
            color: white;
            padding: 30px;
            margin-top: 40px;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📚 Essay Topics</h1>
            <p>Explore insightful essays on important topics</p>
        </header>
        <div class="essays-grid">
        {% for topic_key, essay in essays.items() %}
            <div class="essay-card">
                <div class="essay-card-header">
                    <h2>{{ essay.title }}</h2>
                </div>
                <div class="essay-card-body">
                    <p>Click to read the full essay</p>
                    <a href="/essay/{{ topic_key }}" class="read-btn">Read Essay</a>
                </div>
            </div>
        {% endfor %}
        </div>
        <footer>
            <p>&copy; 2026 Essay Platform | Made with ❤️</p>
        </footer>
    </div>
</body>
</html>
"""

ESSAY_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>{{ essay.title }}</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f7fa;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }
        header h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
        }
        .content {
            padding: 40px 30px;
        }
        .content p {
            font-size: 1.05em;
            line-height: 1.8;
            color: #333;
            text-align: justify;
            margin-bottom: 20px;
        }
        .back-link {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 30px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background 0.3s ease;
        }
        .back-link:hover {
            background: #764ba2;
        }
        footer {
            background: #f5f7fa;
            padding: 20px;
            text-align: center;
            border-top: 1px solid #e0e0e0;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{{ essay.title }}</h1>
        </header>
        <div class="content">
            <p>{{ essay.content }}</p>
            <a href="/" class="back-link">← Back to Topics</a>
        </div>
        <footer>
            <p>&copy; 2026 Essay Platform</p>
        </footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(INDEX_TEMPLATE, essays=ESSAYS)


@app.route("/essay/<topic>")
def show_essay(topic):
    essay = ESSAYS.get(topic)
    if not essay:
        abort(404, description="Essay topic not found")
    return render_template_string(ESSAY_TEMPLATE, essay=essay)
    
if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", "5000"))
    app.run(host=host, port=port)