#!/usr/bin/python

from flask import (Flask,
                  render_template)


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', data=[i for i in "hello"])



if __name__ == '__main__':
   app.run()
