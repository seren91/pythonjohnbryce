import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()
cur.execute(***
    insert into movies VALUES(
        'rrrvrvrvrv'
    )
***) 

con.commit()