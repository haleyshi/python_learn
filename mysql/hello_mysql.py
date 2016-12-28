import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database Version: %s" % data

db.close()
