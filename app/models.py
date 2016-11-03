from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)
manager = Manager(app)


class Paper(db.Model):
	"""
	A model for a scientific paper
	id: the unique id for each paper
	title: the title of the paper 
	authors: the authors of the paper 
	journal: the journal this was published in 
	year: year this was published in 
	abstract: the abstract of the paper
	"""
	__tablename__ = 'papers'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	authors = db.Column(db.String)
	journal = db.Column(db.Integer ,db.ForeignKey('journals.id'))
	year = db.Column(db.Integer, db.ForeignKey('years.id'))
	abstract = db.Column(db.String)

	def to_json(self):
        json_paper = {
            'id': self.id,
            'title': self.title,
            'authors': self.authors,
            'journal': self.journal
            'year': self.year
            'abstract': self.abstract
        }
        return json_paper

	def __repr__(self):
		return '<Paper %r>' % self.title


class Journal(db.Model):
	"""
	A model for a scientific journal
	id: the unique id for each journal
	name: the title of the journal 
	num_papers: the number of papers total published in the journal
	top_subject: the most published subject in the journal
	top_year: the year that the journal had the most publications 
	top_country: the country with the most paper published in this journal
	"""
	__tablename__ = 'journals'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	num_papers = db.Column(db.Integer)
	top_subject = db.Column(db.String)
	top_year = db.Column(db.Integer,db.ForeignKey("years.id"))
	latest_year = db.Column(db.Integer,db.ForeignKey("years.id"))

	def to_json(self):
        json_journal = {
            'id': self.id,
            'name': self.name,
            'num_papers': self.num_papers,
            'top_subject': self.top_subject
            'top_year': self.top_year
            'latest_year': self.latest_year
        }
        return json_journal

	def __repr__(self):
		return '<Journal %r>' % self.name

class Year(db.Model):
	"""
	a model for a specific year
	id: the unique id for the year
	year: the year
	num_papers: the number of papers published that year
	top_subject: the most published subject that year
	top_keyword: the most published keyword in that year
	top_journal: the journal with the most published that year
	"""
	__tablename__ = 'years'
	id = db.Column(db.Integer, primary_key=True)
	year = db.Column(db.Integer)
	num_papers = db.Column(db.Integer)
	top_subject = db.Column(db.String)
	top_country = db.Column(db.String)
	top_journal = db.Column(db.Integer, db.ForeignKey("journals.id"))
	top_journal_count = db.Column(db.Integer)

	def to_json(self):
        json_year = {
            'id': self.id,
            'year': self.year,
            'num_papers': self.num_papers,
            'top_subject': self.top_subject
            'top_country': self.top_country
            'top_journal': self.top_journal
            'top_journal_count': self.top_journal_count
        }
        return json_year


	def __repr__(self):
		return '<Year %r>' % self.year
