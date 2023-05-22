from flask import Flask, request

app = Flask(__name__)


@app.route('/file')
def file():
    with open("demo.txt") as f:
        text = f.read()
    return text


if __name__ == '__main__':
    app.run(port=8090, host="0.0.0.0")