#Code for executing query using input data
import sqlite3

#create a database in RAM
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("create table person1(name,age,id)")

print("Enter 5 students names: ")
who = [input() for i in range(5)]
print("Enter their ages respectively: ")
age = [int(input()) for i in range(5)]
print("Enter their ids respectively: ")
p_id = [int(input()) for i in range(5)]
n = len(who)

for i in range(n):
    #This is the q-mark style:
    c.execute("insert into person1 values(?,?,?)", (who[i],age[i],p_id[i]))
    #And this is the named style:
    c.execute("select * from person1")
    #fetches all entries from table
    print(c.fetchall())