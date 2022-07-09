#Create a class for sqlite database connection
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, name TEXT, price TEXT)")
        self.conn.commit()
        self.conn.close()

    def insert(self, table, values):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO "+table+" VALUES ("+values+")")
        self.conn.commit()
        self.conn.close()

    def view(self, table):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM "+table)
        rows = self.cur.fetchall()
        self.conn.close()
        return rows

    def search(self, table, name):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM "+table+" WHERE name = '"+name+"'")
        rows = self.cur.fetchall()
        self.conn.close()
        return rows

    def delete(self, table, id):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM "+table+" WHERE id = "+id)
        self.conn.commit()
        self.conn.close()

    def update(self, table, id, name, price):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE "+table+" SET name = '"+name+"', price = '"+price+"' WHERE id = "+id)
