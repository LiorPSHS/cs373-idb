from unittest import main, TestCase
from models import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/idb'

db = SQLAlchemy(app)

class TestIDB(TestCase):
    #def setUp(self):
    #    self.connection = db.engine.connect()
    #    self.trans = self.connection.begin()
    #    Session = sessionmaker(bind=db.engine)
    #    self.session = Session()

    #def tearDown(self):
    #    self.session.rollback()

    #def test_paper1(self):
    #    p = Paper(title = "Flying", authors = "Steve",journal = "Journal",year = 1978, abstract = "Does stuff")
    #    self.assertEqual(p.title, "Flying")
    #    self.assertEqual(p.authors, "Steve")
    #def test_paper2(self):
    #    p = Paper(title = "Flying", authors = "Steve",journal = "Journal",year = 1978, abstract = "Does stuff")
    #    self.assertEqual(repr(p), "<Paper Flying>")
    #def test_paper3(self):
    #    p = Paper(title = "Flying", authors = "Steve",journal = "Journal",year = 1978, abstract = "Does stuff")
    #    self.session.add(p)
    #    p = self.session.query(Paper).filter(Paper.name == "Flying").first()
    #    self.assertEqual(p.abstract, "Does stuff")
    #    self.assertEqual(p.year, 1978)
    #def test_journal1(self):
    #    j = Journal(name = "Journal", papers = 12, top_subject = "Physics", top_year = 1992, top_country = "USA")
    #    self.assertEqual(j.top_subject, "Physics")
    #    self.assertEqual(j.papers, 12)
    #def test_journal2(self):
    #    j = Journal(name = "Journal", papers = 12, top_subject = "Physics", top_year = 1992, top_country = "USA")
    #    self.assertEqual(repr(j), "<Journal Journal>")
    #def test_journal3(self):
    #    j = Journal(name = "Journal", papers = 12, top_subject = "Physics", top_year = 1992, top_country = "USA")
    #    self.assertEqual(j.top_country, "USA")
    #    self.assertEqual(j.top_year,1992)
    #def test_year1(self):
    #    y = Year(id = 5, name = "1252",papers = 125)
    #    self.assertEqual(y.name, "1252")
    #    self.assertEqual(y.papers, 125)
    #def test_year2(self):
    #    y = Year(name = "1995")
    #    self.assertEqual(repr(y), "<Year 1995>")
    #def test_year3(self):
    #    y = Year(id = 5, name = "1252",papers = 125)
    #    self.assertEqual(id, 5)
    
    def test_get_paper_1(self):
        paper = get_paper(1)
        test = {'papers': {'year_id': 10, 'name': u'Oxide of silver', 'authors': u'Author(s) unknown.', 'journal': u'Beitr\xc3\xa4ge zur Klinik der Tuberkulose und spezifischen Tuberkulose-Forschung', 'year': 1841, 'id': 1, 'abstract': u'Abstract not available.', 'journal_id': 128}}
	assert paper == test
        pass
    def test_get_paper_2(self):
        paper = get_paper(2)
	assert type(paper) is type({})
        pass
    def test_get_paper_3(self):
        paper = get_paper(1)
	assert paper["papers"].keys().count("name") == 1
        pass

    def test_get_papers_1(self):
        papertable = get_papers()
        assert type(papertable) is type({})
        pass
    def test_get_papers_2(self):
        papertable =get_papers()
        assert len(papertable["papers"]) == 25
        pass
    def test_get_papers_3(self):
        papertable = get_papers()
        assert papertable["papers"][0].keys().count("name") == 1
        
    def test_jsonify_paper_1(self):
        paper = get_paper(1)
        test = {'papers': {'year_id': 10, 'name': u'Oxide of silver', 'authors': u'Author(s) unknown.', 'journal': u'Beitr\xc3\xa4ge zur Klinik der Tuberkulose und spezifischen Tuberkulose-Forschung', 'year': 1841, 'id': 1, 'abstract': u'Abstract not available.', 'journal_id': 128}}
        assert paper == test
        pass
    def test_jsonify_paper_2(self):
        paper = get_paper(1)
        test = {'THIS IS WRONGpapers': {'year_id': 10, 'name': u'Oxide of silver', 'authors': u'Author(s) unknown.', 'journal': u'Beitr\xc3\xa4ge zur Klinik der Tuberkulose und spezifischen Tuberkulose-Forschung', 'year': 1841, 'id': 1, 'abstract': u'Abstract not available.', 'journal_id': 128}}
        assert paper != test
        pass
    def test_jsonify_paper_3(self):
        paper = get_paper(1)
        test = {'papers': {'year_id': 10, 'name': u'Oxide of silver', 'authors': u'Author(s) unknown.', 'journal': u'Beitr\xc3\xa4ge zur Klinik der Tuberkulose und spezifischen Tuberkulose-Forschung', 'year': 1841, 'id': 1, 'abstract': u'Abstract not available.', 'journal_id': 128}}
        assert len(paper)==len(test)
        pass


    def test_get_journal_1(self):
        paper = get_journal(1)
        test = {'journals': {'top_year_id': 162, 'top_year': 1993, 'latest_year': 1997, 'name': u'Applied Scientific Research', 'latest_year_count': 50, 'top_subject': u'Mechanics (1788)', 'num_papers': 1788, 'top_year_count': 119, 'latest_year_id': 166, 'id': 1}}
        assert paper == test
        pass
    def test_get_journal_2(self):
        paper = get_journal(2)
        assert type(paper) is type({})
        pass
    def test_get_journal_3(self):
        paper = get_journal(1)
        assert paper["journals"].keys().count("name") == 1
        pass

    def test_get_journals_1(self):
        papertable = get_journals()
        assert type(papertable) is type({})
        pass
    def test_get_journals_2(self):
        papertable = get_journals()
        assert len(papertable["journals"]) == 25
        pass
    def test_get_journals_3(self):
        papertable = get_journals()
        assert papertable["journals"][0].keys().count("name") == 1
        
    def test_jsonify_journal_1(self):
        paper = get_journal(1)
        test = {'journals': {'top_year_id': 162, 'top_year': 1993, 'latest_year': 1997, 'name': u'Applied Scientific Research', 'latest_year_count': 50, 'top_subject': u'Mechanics (1788)', 'num_papers': 1788, 'top_year_count': 119, 'latest_year_id': 166, 'id': 1}}
        assert paper == test
        pass
    def test_jsonify_journal_2(self):
        paper = get_journal(1)
        test = {'journals': {'top_year_id': 162, 'top_yearo': 1993, 'latest_year': 1997, 'name': u'Applied Scientific Research', 'latest_year_count': 50, 'top_subject': u'Mechanics (1788)', 'num_papers': 1788, 'top_year_count': 119, 'latest_year_id': 166, 'id': 1}}
        assert paper != test
        pass
    def test_jsonify_journal_3(self):
        paper = get_journal(1)
        test = {'journals': {'top_year_id': 162, 'top_year': 1993, 'latest_year': 1997, 'name': u'Applied Scientific Research', 'latest_year_count': 50, 'top_subject': u'Mechanics (1788)', 'num_papers': 1788, 'top_year_count': 119, 'latest_year_id': 166, 'id': 1}}
        assert len(paper)==len(test)
        pass

    def test_get_year_1(self):
        paper = get_year(12)
        test = {'years': {'top_journal_count': 50, 'top_country': u'USA (2)', 'top_journal': u'Zeitschrift f\xc3\xbcr Physik', 'top_journal_id': 177, 'year': 1843, 'num_papers': 93, 'top_subject': u'Physics (50)', 'id': 12}}
        assert paper == test
        pass
    def test_get_year_2(self):
        paper = get_year(2)
        assert type(paper) is type({})
        pass
    def test_get_year_3(self):
        paper = get_year(12)
        assert paper["years"].keys().count("year") == 1
        pass

    def test_get_years_1(self):
        papertable = get_years()
        assert type(papertable) is type({})
        pass
    def test_get_years_2(self):
        papertable = get_years()
        assert len(papertable["years"]) == 25
        pass
    def test_get_years_3(self):
        papertable = get_years()
        assert papertable["years"][0].keys().count("year") == 1
        
    def test_jsonify_year_1(self):
        paper = get_year(12)
        test = {'years': {'top_journal_count': 50, 'top_country': u'USA (2)', 'top_journal': u'Zeitschrift f\xc3\xbcr Physik', 'top_journal_id': 177, 'year': 1843, 'num_papers': 93, 'top_subject': u'Physics (50)', 'id': 12}}

        assert paper == test
        pass
    def test_jsonify_year_2(self):
        paper = get_year(12)
        test = {'years': {'top_journal_count': 50, 'top_coundtry': u'USA (2)', 'top_journal': u'Zeitschrift f\xc3\xbcr Physik', 'top_journal_id': 177, 'year': 1843, 'num_papers': 93, 'top_subject': u'Physics (50)', 'id': 12}}

        assert paper != test
        pass
    def test_jsonify_year_3(self):
        paper = get_year(12)
        test = {'years': {'top_journal_count': 50, 'top_country': u'USA (2)', 'top_journal': u'Zeitschrift f\xc3\xbcr Physik', 'top_journal_id': 177, 'year': 1843, 'num_papers': 93, 'top_subject': u'Physics (50)', 'id': 12}}
        assert len(paper)==len(test)
        pass
    


if __name__ == "__main__" :
	main()
