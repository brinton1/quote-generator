from flask import Flask, render_template, jsonify
import requests
import webbrowser
import threading

app = Flask(__name__)

def get_online_quote():
    """Fetch a random motivational quote from ZenQuotes."""
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        data = response.json()
        quote = f"{data[0]['q']} — {data[0]['a']}"
        return quote
    except Exception:
        # Fallback quote if API or internet fails
        return "Keep going. Everything you need will come to you at the perfect time."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/quote")
def api_quote():
    return jsonify({"quote": get_online_quote()})

def open_browser():
    """Automatically open the app in your default web browser."""
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Launch browser automatically after Flask starts
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
