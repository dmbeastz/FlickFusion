from flask import Flask

app = Flask(__name__)

@app.route("/flicks")

def index():
    return {"flick"  : ["Flick1", "Flick2", "Flick3"]}

if __name__ == "__main__":
    app.run(debug=True)