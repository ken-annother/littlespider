import sqlite3


def insertLinks(links):
    conn = sqlite3.connect("littlespider.db")
    c = conn.cursor()

    # execute multiple commands
    c.executemany('INSERT INTO links VALUES (?, ?, ?)', links)

    conn.commit()
    conn.close()


def queryLinks():
    conn = sqlite3.connect("littlespider.db")
    c = conn.cursor()
    c.execute('SELECT * FROM links LIMIT 20')
    return c.fetchall()
