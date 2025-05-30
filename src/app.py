from flask import Flask

PORT = 8000

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/correct')
def correct():
    return "Everything is correct!"

@app.route('/wrong')
def wrong():
    return "Something went wrong!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)