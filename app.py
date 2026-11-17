from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
fn index():
    return "Hello! Tumatakbo na ang aking Flask app para sa Figma wireframe."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
