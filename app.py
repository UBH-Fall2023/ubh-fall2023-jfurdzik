from flask import Flask, render_template 


app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add.html")
def add():
    return render_template('add.html')

@app.route("/index.html")
def indexLink():
    return render_template('index.html')

@app.route("/get.html")
def get():
    return render_template('get.html')

app.run(host="localhost", port="8080", debug=True)