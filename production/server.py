from flask import Flask, render_template
from generate import generate_text

app = Flask(__name__)

@app.route('/')
def index():
    generated_text = generate_text('map.json', 200)
    return render_template('index.html', generated_text=generated_text)

app.run(host='0.0.0.0', port=5000, debug=True)