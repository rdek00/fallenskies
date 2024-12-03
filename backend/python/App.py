from flask import Flask, render_template

app = Flask(__name__, static_folder="../build", template_folder="../build")

@app.route("/")
def index():
    return app.send_static_file("index.htm")

@app.route("/apod")
def index():
    return app.send_static_file("/apod/index.htm")

if __name__ == "__main__":
    app.run(debug=True)
