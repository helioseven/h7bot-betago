from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon")

@app.route("/")
def hello():
    return "<h1 style='color:red'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")