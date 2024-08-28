from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the log file
    return send_file('/app/log.txt', mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)
