import sqlite3

con = sqlite3.connect('hospital.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS path (abuID int PRIMARY KEY, pulse int, BPnum int,
 BPden int, O2stat int, status text, diag text, message text, lat real, lon real)''')



#cur.execute('''INSERT INTO tshirts VALUES ()''')


con.commit()