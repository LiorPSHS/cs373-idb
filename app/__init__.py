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

@app.route('/about')
def about():
	return render_template('about.html')

# @app_instance.route('/api/papers/<int:page>', methods=['GET'])
# @app_instance.route('/api/papers', methods=['GET'])
# def get_games(page=1):
#     request = Paper.query.paginate(page=page, per_page=25)
#     papers = request.items
#     return jsonify({'papers': [paper.to_json() for paper in papers] })

# @app_instance.route('/api/journals/<int:page>', methods=['GET'])
# @app_instance.route('/api/journals', methods=['GET'])
# def get_games(page=1):
#     request = Game.query.paginate(page=page, per_page=25)
#     journals = request.items
#     return jsonify({'journals': [journal.to_json() for journal in journals] })

# @app_instance.route('/api/year/<int:page>', methods=['GET'])
# @app_instance.route('/api/year', methods=['GET'])
# def get_games(page=1):
#     request = Game.query.paginate(page=page, per_page=25)
#     year = request.items
#     return jsonify({'year': [year.to_json() for year in year] })    

# @app_instance.route('/api/paper/<int:id>', methods=['GET'])
# def get_paper(id):
# 	request = Paper.query.filter_by(id=id).first()
#     if request is None:
#         abort(404)
#     return jsonify(request.to_json(list_view=True))

# @app_instance.route('/api/journal/<int:id>', methods=['GET'])
# def get_journal(id):
# 	request = Journal.query.filter_by(id=id).first()
#     if request is None:
#         abort(404)
#     return jsonify(request.to_json(list_view=True))

# @app_instance.route('/api/year/<int:id>', methods=['GET'])
# def get_year(id):
# 	request = Year.query.filter_by(id=id).first()
#     if request is None:
#         abort(404)
#     return jsonify(request.to_json(list_view=True))

# Static pages, get rid of these later
@app.route('/papers1')
def papers1():
	return render_template('papers1.html')
@app.route('/papers2')
def papers2():
	return render_template('papers2.html')
@app.route('/papers3')
def papers3():
	return render_template('papers3.html')

@app.route('/journal1')
def journal1():
	return render_template('journals1.html')
@app.route('/journal2')
def journal2():
	return render_template('journals2.html')
@app.route('/journal3')
def journal3():
	return render_template('journals3.html')

@app.route('/years1')
def years1():
	return render_template('years1.html')
@app.route('/years2')
def years2():
	return render_template('years2.html')
@app.route('/years3')
def years3():
	return render_template('years3.html')

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
