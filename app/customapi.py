import psycopg2, json

try:
    conn = psycopg2.connect("dbname='idb' user='postgres' host='localhost' password='Test123!'")
except:
    print "I am unable to connect to the database"

def pull_journal( name):
  connection = psycopg2.connect("dbname=<name> user=<user>")
  cursor = conn.cursor() #going to be using this cursor for queries
  cur.execute("SELECT * FROM \"journals\" WHERE \"name\" = \'%s\' LIMIT 1", (name))
  return json.dump(cur.fetchone())

def pull_papers( name):
  connection = psycopg2.connect("dbname=<name> user=<user>")
  cursor = conn.cursor() #going to be using this cursor for queries
  cur.execute("SELECT * FROM \"papers\" WHERE \"paper\" = \'%s\' LIMIT 1", (name))
  return json.dump(cur.fetchone())

def pull_year( name):
  connection = psycopg2.connect("dbname=<name> user=<user>")
  cursor = conn.cursor() #going to be using this cursor for queries
  cur.execute("SELECT * FROM \"years\" WHERE \"year\" = \'%s\' LIMIT 1", (name))
  return json.dump(cur.fetchone())

def pull_journaltable( pageNum):
  pageSize = 25
  startIndex = (pageNum - 1) * 25
  connection = psycopg2.connect("dbname=<name> user=<user>")
  cursor = conn.cursor() #going to be using this cursor for queries
  cur.execute("SELECT * FROM \"journals\" LIMIT %d, %d" % (startIndex, pageSize))
  return json.dump(cur.fetchall())

def pull_yeartable( pageNum):
  pageSize = 25
  startIndex = (pageNum - 1) * 25
  connection = psycopg2.connect("dbname=<name> user=<user>")
  cursor = conn.cursor() #going to be using this cursor for queries
  cur.execute("SELECT * FROM \"years\" LIMIT %d, %d" % (startIndex, pageSize))
  return json.dump(cur.fetchall())

def pull_papertable( pageNum):
  pageSize = 25
  startIndex = (pageNum - 1) * 25
  connection = psycopg2.connect("dbname=<name> user=<user>")
  cursor = conn.cursor() #going to be using this cursor for queries
  cur.execute("SELECT * FROM \"papers\" LIMIT %d, %d" % (startIndex, pageSize))
  return json.dump(cur.fetchall())
