import subprocess
import shlex
from os import path
from flask import Flask, render_template, request, jsonify
from flask_script import Manager, Shell
from models import get_papers, get_paper, get_journals, get_journal, get_years, get_year, get_papers_by_year, get_papers_by_journal
import requests
import json
import random
from googleimages import get_top_image

app = Flask(__name__)

"""
execute a command as a background process
"""
def run_command(command):
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                        break
                if output:
                        print output.strip()
        rc = process.poll()
        return rc

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

#@app.route('/music')
#def music():
#       return render_template('music.html')

@app.route('/music')
def music():

        rand = random.randint(1,14800)
        api_url = "http://www.imusicdb.me/api/tracks/" + str(rand)
        d = requests.get( api_url)
        json_dict = json.loads(d.text)
        data = json_dict

        rand = random.randint(1,25)

        album_id = data["tracks"][rand]["album_id"]
        name = data["tracks"][rand]["name"]
        artist = data["tracks"][rand]["main_artist_id"]
        preview_url = data["tracks"][rand]["preview_url"]
        duration = data["tracks"][rand]["duration"]
        track_no = data["tracks"][rand]["track_no"]

        api_url = "http://www.imusicdb.me/api/artist/" + str(artist)
        d = requests.get(api_url)
        json_dict = json.loads(d.text)
        artist = json_dict["artist"]["name"]



        return render_template('music.html',album_id = album_id,name = name, artist = artist, preview_url = preview_url,duration = duration, track_no = track_no )

# Unit tests

@app.route('/run_tests')
def run_tests():
        p = path.join(path.dirname(path.realpath(__file__)), 'tests.py')
        output = run_command('python ' + p)
        return jsonify({'output': str(output)})


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
        journal_name = json_dict["journals"]["name"]
        journal_img = get_top_image(journal_name)
        return render_template('journal.html', data=json_dict, paper_data=paper_dict, img=journal_img)

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
        #journal(128)
