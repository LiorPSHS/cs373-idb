from flask import Flask, render_template, request, jsonify
from flask_script import Manager, Shell
from models import get_papers, get_paper, get_journals, get_journal, get_years, get_year, get_papers_by_year, get_papers_by_journal
import requests
import json

app = Flask(__name__)

# Main pages
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/header.html')
def header():
	return render_template('header.html')

@app.route('/about')
def about():
	return render_template('about.html')

# Table pages
@app.route('/papers<int:page_number>', methods=['GET'])
def papers(page_number):
	api_url = "http://researchpapers.me/api/papers/" + str(page_number)
	d = requests.get(api_url)
	json_dict = json.loads(d.text)
	return render_template('papers.html', data=json_dict, pg=page_number)

@app.route('/journals<int:page_number>', methods=['GET'])
def journals(page_number):
	api_url = "http://researchpapers.me/api/journals/" + str(page_number)
	d = requests.get(api_url)
	json_dict = json.loads(d.text)
	return render_template('journals.html', data=json_dict, pg=page_number)

@app.route('/years<int:page_number>', methods=['GET'])
def years(page_number):
	api_url = "http://researchpapers.me/api/years/" + str(page_number)
	d = requests.get(api_url)
	json_dict = json.loads(d.text)
	return render_template('years.html', data=json_dict, pg=page_number)

# Pillar pages
@app.route('/paper<int:paper_id>', methods=['GET'])
def paper(paper_id):
	api_url = "http://researchpapers.me/api/paper/" + str(paper_id)
	d = requests.get(api_url)
	json_dict = json.loads(d.text)
	return render_template('paper.html', data=json_dict)

@app.route('/journal<int:journal_id>', methods=['GET'])
def journal(journal_id):
	api_url = "http://researchpapers.me/api/journal/" + str(journal_id)
	d = requests.get(api_url)
	json_dict = json.loads(d.text)

	paper_api_url = "http://researchpapers.me/api/papers/journal/" + str(journal_id)
	p = requests.get(paper_api_url)
	paper_dict = json.loads(p.text)
	return render_template('journal.html', data=json_dict, paper_data=paper_dict)

@app.route('/year<int:year_id>', methods=['GET'])
def year(year_id):
	api_url = "http://researchpapers.me/api/year/" + str(year_id)
	d = requests.get(api_url)
	json_dict = json.loads(d.text)

	paper_api_url = "http://researchpapers.me/api/papers/year/" + str(year_id)
	p = requests.get(paper_api_url)
	paper_dict = json.loads(p.text)
	return render_template('year.html', data=json_dict, paper_data=paper_dict)

# API
@app.route('/api/papers/<int:page_number>', methods=['GET'])
def api_papers(page_number):
	papers = get_papers(page_number)
	return jsonify(papers)

@app.route('/api/paper/<int:paper_id>', methods=['GET'])
def api_paper(paper_id):
	paper = get_paper(paper_id)
	return jsonify(paper)

@app.route('/api/papers/journal/<int:journal_id>', methods=['GET'])
def api_papers_journal(journal_id):
	papers = get_papers_by_journal(journal_id)
	return jsonify(papers)

@app.route('/api/papers/year/<int:year_id>', methods=['GET'])
def api_papers_year(year_id):
	papers = get_papers_by_year(year_id)
	return jsonify(papers)

@app.route('/api/journals/<int:page_number>', methods=['GET'])
def api_journals(page_number):
	journals = get_journals(page_number)
	return jsonify(journals)

@app.route('/api/journal/<int:journal_id>', methods=['GET'])
def api_journal(journal_id):
	journal = get_journal(journal_id)
	return jsonify(journal)

@app.route('/api/years/<int:page_number>', methods=['GET'])
def api_years(page_number):
	years = get_years(page_number)
	return jsonify(years)

@app.route('/api/year/<int:year_id>', methods=['GET'])
def api_year(year_id):
	year = get_year(year_id)
	return jsonify(year)

if __name__ == "__main__":
        app.run(debug=True)
