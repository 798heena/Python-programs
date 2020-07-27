#code for update operation
import sqlite3

#database name to be passed as parameter
conn = sqlite3.connect('pranshu.db')
c = conn.cursor()

#update the person record
c.execute('update person set PAN_CARD="ASTDG8527H" where PERSON="RAVI"')
conn.commit()
c.execute('select * from person')
data = c.fetchall()
print(data)
c.close()
conn.close()