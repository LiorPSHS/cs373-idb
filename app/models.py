from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)
manager = Manager(app)

journal_paper = db.Table('journal_paper',
    db.Column('journal_id', db.Integer, db.ForeignKey('journals.id')),
    db.Column('paper_gid', db.Integer, db.ForeignKey('papers.id'))
)

year_paper = db.Table('year_paper',
    db.Column('year_id', db.Integer, db.ForeignKey('years.id')),
    db.Column('paper_id', db.Integer, db.ForeignKey('papers.id'))
)

class Paper(db.Model):
	__tablename__ = 'papers'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	authors = db.Column(db.String)
	journal = db.Column(db.Int,db.ForeignKey('journals.id'))
	year = db.Column(db.Int, db.ForeignKey('years.id'))
	abstract = db.Column(db.String)

	def __repr__(self):
		return '<Paper %r>' % self.title

class Journal(db.Model):
	__tablename__ = 'journals'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	numPapers = db.Column(db.Integer)
	top_subject = db.Column(db.String)
	top_year = db.Column(db.Integer,db.ForeignKey("years.id"))
	top_country = db.Column(db.String)
	papers = db.relationship('Paper', secondary=journal_game, backref='journals')

	def __repr__(self):
		return '<Journal %r>' % self.name

class Year(db.Model):
	__tablename__ = 'years'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	numPapers = db.Column(db.Integer)
	top_subject = db.Column(db.String)
	top_keyword = db.Column(db.String)
	top_journal = db.Column(db.Integer, db.ForeignKey("journals.id"))
	papers = db.relationship('Paper', secondary=year_game, backref='years')


	def __repr__(self):
		return '<Year %r>' % self.name