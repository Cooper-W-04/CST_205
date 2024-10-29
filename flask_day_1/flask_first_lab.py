from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello world from Flask!'

@app.route('/fortnite')
def fort():
  return 'now this is epic'

@app.route('/fortnite_2')
def nite():
  return render_template('my_template_1.html')

#github i uploaded to:
#