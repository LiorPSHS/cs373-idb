import psycopg2

def pull_journal( name):
   connection = psycopg2.connect("dbname=<name> user=<user>")
   cursor = conn.cursor() #going to be using this cursor for queries
   cur.execute("SELECT * FROM \"journals\" WHERE \"name\" = \'%s\' LIMIT 1", (name))
   return cur.fetchone()

def pull_papers( name):
   connection = psycopg2.connect("dbname=<name> user=<user>")
   cursor = conn.cursor() #going to be using this cursor for queries
   cur.execute("SELECT * FROM \"papers\" WHERE \"paper\" = \'%s\' LIMIT 1", (name))
   return cur.fetchone()

def pull_year( name):
   connection = psycopg2.connect("dbname=<name> user=<user>")
   cursor = conn.cursor() #going to be using this cursor for queries
   cur.execute("SELECT * FROM \"years\" WHERE \"year\" = \'%s\' LIMIT 1", (name))
   return cur.fetchone()

def pull_table( tablename)
    connection = psycopg2.connect("dbname=<name> user=<user>")
    cursor = conn.cursor() #going to be using this cursor for queries
    cur.execute("SELECT * FROM %s;", (tablename))
    return cur.fetchmany(5)
