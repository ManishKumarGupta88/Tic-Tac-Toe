# Tic Tac Toe Web App

A simple Tic Tac Toe game built with Python Flask and JavaScript.

## Run locally

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Start the server:

```bash
python app.py
```

3. Open `http://127.0.0.1:5000` in your browser.

## Push to GitHub

1. Create a GitHub repository.
2. Add, commit, and push your files:

```bash
git init
git add .
git commit -m "Add Tic Tac Toe Flask app"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Notes

- This project runs on localhost after you push or clone it.
- GitHub Pages does not host Python apps directly; the Flask server in `app.py` cannot run there.
- To make GitHub Pages show the game, the site must use static files (`index.html`, `static/style.css`, etc.).
- If you want a live online URL for the Flask version, use a Python-capable host such as Railway, Render, or Heroku.
