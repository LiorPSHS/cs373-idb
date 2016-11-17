from flask import Flask, render_template
from sqlalchemy import create_engine, MetaData, Table, Column, Integer
from sqlalchemy.orm import mapper, sessionmaker

def connect(user, password, db, host='localhost', port=5432):
	'''Returns a connection and a metadata object'''
	# We connect with the help of the PostgreSQL URL
	# postgresql://federer:grandestslam@localhost:5432/tennis
	url = 'postgresql://{}:{}@{}:{}/{}'
	url = url.format(user, password, host, port, db)

	# The return value of create_engine() is our connection object
	con = create_engine(url, client_encoding='utf8')

	# We then bind the connection to MetaData()
	meta = MetaData(bind=con, reflect=True)

	return con, meta

def get_table(table_name, metadata):
	return Table(table_name, metadata, Column("id", Integer, primary_key=True), autoload = True, extend_existing=True)

class Papers(object):
	"""
	A model for a scientific paper
	id: the unique id for each paper
	title: the title of the paper 
	authors: the authors of the paper 
	journal: the journal this was published in 
	year: year this was published in 
	abstract: the abstract of the paper
	"""
	pass

class Journals(object):
	"""
	A model for a scientific journal
	id: the unique id for each journal
	name: the title of the journal 
	num_papers: the number of papers total published in the journal
	top_subject: the most published subject in the journal
	top_year: the year that the journal had the most publications 
	top_country: the country with the most paper published in this journal
	"""
	pass

class Years(object):
	"""
	a model for a specific year
	id: the unique id for the year
	year: the year
	num_papers: the number of papers published that year
	top_subject: the most published subject that year
	top_keyword: the most published keyword in that year
	top_journal: the journal with the most published that year
	"""
	pass

# Search API

def get_search_results(queries):
	papers_and = []
	journals_and = []
	papers_or = []
	journals_or = []
	search_query_and(queries, papers_and, journals_and)
	for query in queries:
		search_query_or(query, papers_and, journals_and, papers_or, journals_or)
	return { 'papers_and': [paper_json(paper) for paper in papers_and],
		 'papers_or': [paper_json(paper) for paper in papers_or],
		 'journals_and': [journal_json(journal) for journal in journals_and],
		 'journals_or': [journal_json(journal) for journal in journals_or] }

def search_query_and(queries, papers, journals):
	paper_results = session.query(Papers)
	journal_results = session.query(Journals)
	for query in queries:
		query_string = '%' + query + '%'
		paper_results = paper_results.filter(Papers.name.ilike(query_string))
		journal_results = journal_results.filter(Journals.name.ilike(query_string))
	papers.extend(paper_results.limit(15))
	journals.extend(journal_results.limit(15))

def search_query_or(query, papers_and, journals_and, papers_or, journals_or):
	query_string = '%' + query + '%'
	paper_results = session.query(Papers).filter(Papers.name.ilike(query_string)).limit(15)
	for paper in paper_results:
		if paper not in papers_and and paper not in papers_or:
			papers_or.append(paper)
	journal_results = session.query(Journals).filter(Journals.name.ilike(query_string)).limit(15)
	for journal in journal_results:
		if journal not in journals_and:
			journals_or.append(journal)

# Paper API

"""
convert Papers object to json
"""
def paper_json(paper):
	year = session.query(Years).get(paper.year)
	if year is None:
		year_string = "N/A"
	else:
		year_string = year.year
	journal = session.query(Journals).get(paper.journal)
	return {
		'id': paper.id,
		'name': paper.name,
		'journal': journal.name,
		'journal_id': paper.journal,
		'authors': paper.authors,
		'year': year_string,
		'year_id': paper.year,
		'abstract': paper.abstract
	}

"""
get all papers using given page number
"""
def get_papers(page_number=1):
	papers = session.query(Papers).offset(page_size * (page_number - 1)).limit(page_size).all()
	return { 'papers': [paper_json(paper) for paper in papers] }

"""
get all json for a specific paper"
"""
def get_paper(paper_id=1):
	paper = session.query(Papers).get(paper_id)
	return { 'papers': paper_json(paper) }

"""
get all json for papers belonging to the journal id
"""
def get_papers_by_journal(journal_id):
	papers = session.query(Papers).filter(Papers.journal == journal_id)
	return { 'papers': [paper_json(paper) for paper in papers] }

"""
get all json for papers belonging to the year id
"""
def get_papers_by_year(year_id):
	papers = session.query(Papers).filter(Papers.year == year_id)
	return { 'papers': [paper_json(paper) for paper in papers] }

# Journal API

"""
convert Journals object to json
"""
def journal_json(journal):
	latest_year = session.query(Years).get(journal.latest_year)
	if latest_year is None:
		latest_year_string = "N/A"
	else:
		latest_year_string = latest_year.year
	top_year = session.query(Years).get(journal.top_year)
	if top_year is None:
		top_year_string = "N/A"
	else:
		top_year_string = top_year.year
	return {
		'id': journal.id,
		'name': journal.name,
		'num_papers': journal.num_papers,
		'top_subject': journal.top_subject,
		'latest_year': latest_year_string,
		'latest_year_id': journal.latest_year,
		'latest_year_count': journal.latest_year_count,
		'top_year': top_year_string,
		'top_year_id': journal.top_year,
		'top_year_count': journal.top_year_count
	}

"""
get all journals using given page number
"""
def get_journals(page_number=1):
	journals = session.query(Journals).offset(page_size * (page_number - 1)).limit(page_size).all()
	return { 'journals': [journal_json(journal) for journal in journals] }

"""
get json for a specific journal
"""
def get_journal(journal_id=1):
	journal = session.query(Journals).get(journal_id)
	return { 'journals': journal_json(journal) }

# Year API

"""
convert Years object to json
"""
def year_json(year):
	top_journal = session.query(Journals).get(year.top_journal)
	return {
		'id': year.id,
		'year': year.year,
		'num_papers': year.num_papers,
		'top_subject': year.top_subject,
		'top_country': year.top_country,
		'top_journal': top_journal.name,
		'top_journal_id': year.top_journal,
		'top_journal_count': year.top_journal_count
	}

"""
get all years using the given page number
"""
def get_years(page_number=1):
	years = session.query(Years).order_by(Years.year.desc()).offset(page_size * (page_number - 1)).limit(page_size).all()
	return { 'years': [year_json(year) for year in years] }

"""
get json for a specific year
"""
def get_year(year_id=1):
	year = session.query(Years).get(year_id)
	return { 'years': year_json(year) }

# ------------------------ INIT -----------------------

page_size = 25

# Connect to db
engine, metadata = connect('postgres', 'Test123!', 'idb')

# Map tables
papers = get_table('papers', metadata)
mapper(Papers, papers)

journals = get_table('journals', metadata)
mapper(Journals, journals)

years = get_table('years', metadata)
mapper(Years, years)

# Load session
Session = sessionmaker(bind=engine)
session = Session()
