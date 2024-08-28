from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Execute the JAR file and get output
    result = subprocess.run(['java', '-jar', 'myapp-{}-SNAPSHOT.jar'.format(env.new_version)], capture_output=True, text=True)
    # Return the output
    return f"<pre>{result.stdout}</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
