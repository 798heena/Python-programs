#code for deletion
import sqlite3

#database name to be passed as parameter
conn = sqlite3.connect('pranshu.db')
c = conn.cursor()

#delete the person record
c.execute('delete from person where PERSON="SURESH"')
conn.commit()
c.execute('select * from person')
data = c.fetchall()
print(data)
c.close()
conn.close()