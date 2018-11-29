from flask import Flask
import os, socket

app = Flask(__name__)

@app.route("/tvr/predict")
def hello():
    return os.getenv("NAME") + " TVR Hostname: " + socket.gethostname()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
