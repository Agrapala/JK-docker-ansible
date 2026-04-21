# Flask Essay Topics App

This project now supports running directly on your local PC and in Docker.

## Run on Local PC

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app/main.py
```

4. Open in browser:

- http://127.0.0.1:5000

## Run with Docker

```bash
docker build -t essay-app .
docker run --rm -p 5000:5000 essay-app
```

Open:

- http://localhost:5000

## Available Pages

- `/` -> list of essay topics
- `/essay/technology`
- `/essay/environment`
- `/essay/teamwork`
