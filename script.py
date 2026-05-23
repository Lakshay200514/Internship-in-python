import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
sql="""
insert into emp values(1,"Lakshay","Jaipur","98985")
    
"""
conn.execute(sql)
conn.commit()
conn.close()