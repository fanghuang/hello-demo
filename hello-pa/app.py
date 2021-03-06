from flask import Flask
import os, socket

app = Flask(__name__)

@app.route("/pa/predict")
def hello():
    return os.getenv("NAME") + " PA Hostname: " + socket.gethostname()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
