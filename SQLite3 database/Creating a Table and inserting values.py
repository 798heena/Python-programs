#Python code to demonstrate table creations and insertions with SQL
#importing module
import sqlite3

#connecting to the database
conn = sqlite3.connect('pranshu.db')

#cursor
c = conn.cursor()

#SQL command to create 2 tables in the database and execute the statement
c.execute('create table person(PERSON text,PAN_CARD text,AADHAR_CARD integer,STATE text)')
c.execute('create table product(PRODUCT text,PRODUCT_ID text,MARKED_PRICE integer,SELLING_PRICE integer)')

#using function
def main():
#SQL command to insert the data in the table 'person'
    c.execute("insert into person values('PRANSHU','ATAPV2431U',980123457825,'CHHATTISGARH')")
    c.execute("insert into person values('RAVI','ASDAV9811P',127894637085,'MAHARASHTRA')")
    c.execute("insert into person values('RAMESH','OHGWF4580I',786024830483,'ASSAM')")
    c.execute("insert into person values('SURESH','WDERT5479Y',864292178530,'RAJASTHAN')")
    c.execute("insert into person values('SHYAM','LADFV4561K',786048219762,'ORISSA')")

#to save the changes in the files.Never skip this.
#If we skip this nothing will be saved in the database.
    conn.commit()
#execute the command to fetch all the data from the table person
    c.execute('select * from person')
#store all the fetch data in the data variable
    data = c.fetchall()
#Since we have already selected all the data entries
#using the "SELECT *" SQL commandand stored them in
#the data variable, all we need to do now is to print
#out the data variable
    print(data)
main()
def main1():
    c.execute("insert into product values('FAIR & LOVELY','PV12345',498,458)")
    c.execute("insert into product values('DANT KANTI','DKL2345',72,68)")
    c.execute("insert into product values('DOVE','PV1234YAHA',55,45)")
    c.execute("insert into product values('WILD STONE','AT123BGJ',199,149)")
    c.execute("insert into product values('PUMA','PV12345',4499,3499)")
    conn.commit()
    c.execute('select * from product')
    data = c.fetchall()
    print(data)
main1()
c.close()
#close the connection
conn.close()



