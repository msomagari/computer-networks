from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def home():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 0))
    return f"Application started on: {s.getsockname()[1]}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
