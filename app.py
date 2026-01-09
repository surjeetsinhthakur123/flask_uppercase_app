from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")

    if name:
        data = {
            "original": name,
            "upper": name.upper(),
            "reverse": name[::-1],
            "length": len(name),
            "time": datetime.now().strftime("%d %B %Y, %I:%M %p")
        }
        return render_template("index.html", data=data)

    return render_template("index.html", data=None)

@app.route("/shout/<name>")
def shout(name):
    return f"<h1 style='color:red;'>🔥 {name.upper()} 🔥</h1>"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")

    if name:
        data = {
            "original": name,
            "upper": name.upper(),
            "reverse": name[::-1],
            "length": len(name),
            "time": datetime.now().strftime("%d %B %Y, %I:%M %p")
        }
        return render_template("index.html", data=data)

    return render_template("index.html", data=None)

@app.route("/shout/<name>")
def shout(name):
    return f"<h1 style='color:red;'>🔥 {name.upper()} 🔥</h1>"

if __name__ == "__main__":
    app.run(debug=True)
