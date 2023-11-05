from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(host="localhost", port="8080", debug=True)
