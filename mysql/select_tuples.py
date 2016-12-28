import MySQLdb

db =MySQLdb.connect("localhost", "root", "root", "TESTDB")

cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE WHERE \
      INCOME > '%d'" % (10000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        fname = result[0]
        lname = result[1]
        age = result[2]
        sex = result[3]
        income = result[4]
        print "FIRST_NAME=%s, LAST_NAME=%s, AGE=%d, SEX=%s, INCOME=%d" % \
              (fname, lname, age, sex, income)
except:
    print "Error: failed to query data from database!"

db.close()