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
</head>
<body>
    <h1>Essay Topics</h1>
    <p>Select a topic to read the essay:</p>
    <ul>
    {% for topic_key, essay in essays.items() %}
        <li><a href="/essay/{{ topic_key }}">{{ essay.title }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
"""

ESSAY_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>{{ essay.title }}</title>
</head>
<body>
    <h1>{{ essay.title }}</h1>
    <p>{{ essay.content }}</p>
    <p><a href="/">Back to topics</a></p>
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