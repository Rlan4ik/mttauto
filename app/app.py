from routes.cars import cars_blueprint
app.register_blueprint(cars_blueprint)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "mtt auto backend работает 🚗"

if name == "__main__":
    app.run(debug=True)
