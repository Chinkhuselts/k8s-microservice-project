from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    pod_id = socket.gethostname()
    return f"Hello from Kubernetes! Served by Pod: {pod_id}\n"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)