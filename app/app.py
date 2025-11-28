from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "mtt auto backend работает 🚗"

if name == "__main__":
    app.run(debug=True)
