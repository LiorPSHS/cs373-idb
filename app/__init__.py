from flask import Flask, render_template, request
from flask_script import Manager, Shell
#from models import Paper,Journal,Year
app = Flask(__name__)

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

@app.route('/about')
def about():
	return render_template('about.html')

# Single pages
@app.route('/paper<int:paper_id>', methods=['GET'])
def paper(paper_id):
	return render_template('papers1.html', pid=paper_id)

@app.route('/journal<int:journal_id>', methods=['GET'])
def journal(journal_id):
	return render_template('journals1.html')

@app.route('/year<int:year_id>', methods=['GET'])
def year(year_id):
	return render_template('years1.html')

if __name__ == "__main__":
        app.run()
