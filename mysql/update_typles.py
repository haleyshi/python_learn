import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "TESTDB")

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
      WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()