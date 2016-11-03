from unittest import main, TestCase
from app import Paper,Journal,Year
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/swe'

db = SQLAlchemy(app)

class TestIDB(TestCase):
    def setUp(self):
        self.connection = db.engine.connect()
        self.trans = self.connection.begin()
        Session = sessionmaker(bind=db.engine)
        self.session = Session()

    def tearDown(self):
        self.session.rollback()

    def test_paper1(self):
        p = new Paper(title = "Flying", authors = "Steve",journal = "Journal",year = 1978, abstract = "Does stuff")
        self.assertEqual(p.title, "Flying")
        self.assertEqual(p.authors, "Steve")
    def test_paper2(self):
        p = new Paper(title = "Flying", authors = "Steve",journal = "Journal",
                      year = 1978, abstract = "Does stuff")
         self.assertEqual(repr(p), "<Paper Flying>")
    def test_paper3(self):
        p = new Paper(title = "Flying", authors = "Steve",journal = "Journal",
                      year = 1978, abstract = "Does stuff")
        self.session.add(p)
        p = self.session.query(Paper).filter(Paper.name == "Flying").first()
        self.assertEqual(p.abstract, "Does stuff")
        self.assertEqual(p.year, 1978)
    def test_journal1(self):
        j = new Journal(name = "Journal", papers = 12, top_subject = "Physics", top_year = 1992, top_country = "USA")
        self.assertEqual(j.top_subject, "Physics")
        self.assertEqual(j.papers, 12)
    def test_journal2(self):
        j = new Journal(name = "Journal", papers = 12, top_subject = "Physics", top_year = 1992, top_country = "USA")
        self.assertEqual(repr(j), "<Journal Journal>")
    def test_journal3(self):
        j = new Journal(name = "Journal", papers = 12, top_subject = "Physics", top_year = 1992, top_country = "USA")
        self.assertEqual(j.top_country, "USA")
        self.assertEqual(j.top_year,1992)
    def test_year1(self):
        y = new year(id = 5, name = "1252",papers = 125)
        self.assertEqual(y.name, "1252")
        self.assertEqual(y.papers, 125)
    def test_year2(self):
        y = new year(name = "1995")
        self.assertEqual(repr(y), "<Year 1995>")
    def test_year3(self):
        y = new year(id = 5, name = "1252",papers = 125)
        self.assertEqual(id, 5)
    
    def test_get_paper_1:
        paper = getPaper(1)
        test = {"name":"Oxide of silver","journal":128,"authors":"Author(s) unknown.","year":10,"abstract":"Abstract not available.","id":1}
        assert paper == test
        pass
    def test_get_paper_2:
        paper = getPaper(2)
        assert type(paper) is type(dict)
        pass
    def test_get_paper_3:
        paper = getPaper(1)
        assert paper.keys().count("name") == 1
        pass

    def test_get_papers_1:
        papertable = getPapers()
        assert type(papertable) is type(dict)
        pass
    def test_get_papers_2:
        papertable = getPapers()
        assert count(papertable["papers"]) == 25
        pass
    def test_get_papers_3:
        papertable = getPapers()
        assert papertable["papers"][0].keys().count("name") == 1
        
    def test_jsonify_paper_1:
        paper = jsonify_paper(getPaper(1))
        test = jsonify({"name":"Oxide of silver","journal":128,"authors":"Author(s) unknown.","year":10,"abstract":"Abstract not available.","id":1})
        assert paper == test
        pass
    def test_jsonify_paper_2:
        paper = jsonify_paper(getPaper(1))
        test = jsonify({"name":"Bro-xide of silver","journal":128,"authors":"Author(s) unknown.","year":10,"abstract":"Abstract not available.","id":1})
        assert paper != test
        pass
    def test_jsonify_paper_3:
        paper = jsonify_paper(getPaper(1))
        test = jsonify({"name":"Oxide of silver","journal":128,"authors":"Author(s) unknown.","year":10,"abstract":"Abstract not available.","id":1})
        assert len(paper)==len(test)
        pass


    def test_get_journal_1:
        paper = getJournal(1)
        test = {"name":"Applied Scientific Research","num_papers":1788,"top_subject":"Mechanics (1788)","latest_year":166,"latest_year_count":50,"top_year":162,"top_year_count":119,"id":1}
        assert paper == test
        pass
    def test_get_journal_2:
        paper = getJournal(2)
        assert type(paper) is type(dict)
        pass
    def test_get_journal_3:
        paper = getJournal(1)
        assert paper.keys().count("name") == 1
        pass

    def test_get_journals_1:
        papertable = getJournals()
        assert type(papertable) is type(dict)
        pass
    def test_get_journals_2:
        papertable = getJournals()
        assert count(papertable["journals"]) == 25
        pass
    def test_get_journals_3:
        papertable = getJournals()
        assert papertable["journals"][0].keys().count("name") == 1
        
    def test_jsonify_journal_1:
        paper = jsonify_journal(getJournal(1))
        test = jsonify({"name":"Applied Scientific Research","num_papers":1788,"top_subject":"Mechanics (1788)","latest_year":166,"latest_year_count":50,"top_year":162,"top_year_count":119,"id":1})
        assert paper == test
        pass
    def test_jsonify_journal_2:
        paper = jsonify_journal(getJournal(1))
        test = jsonify({"name":"TOTALTRASHApplied Scientific Research","num_papers":1788,"top_subject":"Mechanics (1788)","latest_year":166,"latest_year_count":50,"top_year":162,"top_year_count":119,"id":1})
        assert paper != test
        pass
    def test_jsonify_journal_3:
        paper = jsonify_journal(getJournal(1))
        test = jsonify({"name":"Applied Scientific Research","num_papers":1788,"top_subject":"Mechanics (1788)","latest_year":166,"latest_year_count":50,"top_year":162,"top_year_count":119,"id":1})
        assert len(paper)==len(test)
        pass

    def test_get_year_1:
        paper = getYear(12)
        test = {"year":1843,"num_papers":93,"top_subject":"Physics (50)","top_country":"USA (2)","top_journal":177,"top_journal_count":50,"id":12}
        assert paper == test
        pass
    def test_get_year_2:
        paper = getYear(2)
        assert type(paper) is type(dict)
        pass
    def test_get_year_3:
        paper = getYear(12)
        assert paper.keys().count("year") == 1
        pass

    def test_get_years_1:
        papertable = getYears()
        assert type(papertable) is type(dict)
        pass
    def test_get_years_2:
        papertable = getYears()
        assert count(papertable["years"]) == 25
        pass
    def test_get_years_3:
        papertable = getYears()
        assert papertable["years"][0].keys().count("year") == 1
        
    def test_jsonify_year_1:
        paper = jsonify_year(getYear(12))
        test = jsonify({"year":1843,"num_papers":93,"top_subject":"Physics (50)","top_country":"USA (2)","top_journal":177,"top_journal_count":50,"id":12})
        assert paper == test
        pass
    def test_jsonify_year_2:
        paper = jsonify_year(getYear(12))
        test = jsonify({"year":1843,"num_papers":93,"top_subject":"Physics (50)","top_country":"USA (2)","top_journal":177,"top_journal_count":50,"id":12})
        assert paper != test
        pass
    def test_jsonify_year_3:
        paper = jsonify_year(getYear(12))
        test = jsonify({"year":1843,"num_papers":93,"top_subject":"Physics (50)","top_country":"USA (2)","top_journal":177,"top_journal_count":50,"id":12})
        assert len(paper)==len(test)
        pass
    
