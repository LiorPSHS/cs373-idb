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