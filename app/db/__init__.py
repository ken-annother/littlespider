from manage import *

conn = sqlite3.connect("littlespider.db")

c = conn.cursor()

# create tables
c.execute('''CREATE TABLE IF NOT EXISTS links
      (id INTEGER PRIMARY KEY AUTOINCREMENT , linkurl TEXT , checked BOOLEAN DEFAULT FALSE )''')

c.execute('''CREATE TABLE IF NOT EXISTS pics
      (id INTEGER PRIMARY KEY AUTOINCREMENT,
       picurl TEXT,
       downed BOOLEAN DEFAULT FALSE)''')

# save the changes
conn.commit()

# close the connection with the database
conn.close()

