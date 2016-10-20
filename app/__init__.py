from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from models import Paper,Journal,Year
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)
manager = Manager(app)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/years')
def years():
	#b = Year.query.all()
	#return render_template('years.html', years=b)
	return render_template('years.html')

@app.route('/journals')
def countries():
	#a = Journal.query.all()
	#return render_template('journals.html', journals=a)
	return render_template('journals.html')

@app.route('/papers')
def papers():
	#c = Paper.query.all()
	#return render_template('papers.html', papers=c)
	return render_template('papers.html')

@app.route('/header.html')
def header():
	return render_template('header.html')

def shell_context():
	context = {
		'app': app,
		'db': db,
		'Paper': Paper,
		'Journal': Journal,
		'Year' : Year
	}
	return context

manager.add_command('shell', Shell(make_context=shell_context))

if __name__ == "__main__":
        manager.run()
