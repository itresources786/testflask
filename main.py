from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/api/read')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅 It has been changed"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
