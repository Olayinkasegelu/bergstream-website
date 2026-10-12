from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Bergstream UG (haftungsbeschränkt)</h1>
    <p>Cybersecurity, AI and data — from Bergisch Gladbach.</p>
    <a href="/about">About</a>
    """

app.run(debug=True)
