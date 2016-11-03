from flask import Flask, render_template, request, jsonify
from flask_script import Manager, Shell
from models import get_papers, get_paper, get_journals, get_journal, get_years, get_year

app = Flask(__name__)

# Main pages
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/years')
def years():
	return render_template('years.html')

@app.route('/journals')
def countries():
	return render_template('journals.html')

@app.route('/papers')
def papers():
	return render_template('papers.html')

@app.route('/header.html')
def header():
	return render_template('header.html')

@app.route('/about')
def about():
	return render_template('about.html')

# API

@app_instance.route('/')
def run_tests():
    from subprocess import getoutput
    from os import path
    p = path.join(path.dirname(path.realpath(__file__)), 'tests.py')
    output = getoutput('python '+p)
    print(output)
    return jsonify({'output': str(output)})



@app.route('/api/papers/<int:page_number>', methods=['GET'])
def api_papers(page_number):
	papers = get_papers(page_number)
	return jsonify(papers)

@app.route('/api/paper/<int:paper_id>', methods=['GET'])
def api_paper(paper_id):
	paper = get_paper(paper_id)
	return jsonify(paper)

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
