from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

SECRET_PATH = "/etc/secrets/Data.json"

if os.path.exists(SECRET_PATH):
    DATA_PATH = SECRET_PATH
else:
    DATA_PATH = os.path.join(os.path.dirname(__file__), 'Data.json')

with open(DATA_PATH, 'r') as f:
    TIME_DATA = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/year/<int:year>')
def get_year(year):
    if year < 1900 or year > 2025:
        return jsonify({'error': 'Year must be between 1900 and 2025.'}), 400

    # Exact match
    if str(year) in TIME_DATA:
        return jsonify({'year': year, 'matched': year, 'data': TIME_DATA[str(year)]})


if __name__ == '__main__':
    app.run(debug=True)
