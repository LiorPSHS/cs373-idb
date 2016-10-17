from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)
manager = Manager(app)

class Paper(db.Model):
	__tablename__ = 'papers'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	authors = db.Column(db.String)
	journal = db.Column(db.String)
	year = db.Column(db.Int, db.ForeignKey('years.id'))
	abstract = db.Column(db.String)

	def __repr__(self):
		return '<Paper %r>' % self.title

class Journal(db.Model):
	__tablename__ = 'countries'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	papers = db.Column(db.Integer)
	top_subject = db.Column(db.String)
	top_year = db.Column(db.Integer)
	top_country = db.Column(db.String)

	def __repr__(self):
		return '<Country %r>' % self.name

class Year(db.Model):
	__tablename__ = 'years'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	papers = db.Column(db.Integer)
	top_subject = db.Column(db.String)
	top_keyword = db.Column(db.String)
	top_journal = db.Column(db.String)


	def __repr__(self):
		return '<Year %r>' % self.name

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/years')
def books():
	b = Year.query.all()
	return render_template('years.html', books=b)

@app.route('/countries')
def countries():
	a = Country.query.all()
	return render_template('countries.html', countries=a)

@app.route('/papers')
def papers():
	c = Paper.query.all()
	return render_template('papers.html', papers=c)

def shell_context():
	context = {
		'app': app,
		'db': db,
		'Paper': Paper,
		'Country': Country,
		'Year' : Year
	}
	return context

manager.add_command('shell', Shell(make_context=shell_context))

if __name__ == "__main__":
        manager.run()
