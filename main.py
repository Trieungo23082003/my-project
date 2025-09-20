from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Xin chào Ngô Thanh Triều 🚀</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
