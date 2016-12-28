import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "TESTDB")

cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
VALUES('Haley', 'Shi', 33, 'M', 35000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()