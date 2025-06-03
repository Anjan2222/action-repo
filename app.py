import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/joke')
def get_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        joke = response.json()
        return jsonify({
            "setup": joke.get("setup"),
            "punchline": joke.get("punchline")
        })
    else:
        return jsonify({"error": "Could not fetch joke"}), 500

if __name__ == '__main__':
    app.run(debug=True)
