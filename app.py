from flask import Flask
from flask import render_template

from config import configs
from lib.exts import db

app = Flask(__name__)
app.config.from_object(configs)
db.init_app(app)


@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
