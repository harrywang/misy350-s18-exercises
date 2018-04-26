from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "hello harry wang hahahah"


@app.route('/user')
def user():
    return "this is the page for users"


if __name__ == '__main__':
    app.run()
