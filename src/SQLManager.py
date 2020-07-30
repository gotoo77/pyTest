import mysql.connector


class SQLManager:
    def __init__(self, host, port, user, pwd, schema):
        self.host = host
        self.port = port
        self.user = user
        self.password = pwd
        self.db = schema
        self.conn = None
        self.curs = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.db
        )
        print(self.conn)
        self.curs = self.conn.cursor()

    def show_databases(self):
        if self.curs is None:
            print("Error, cursor has not been defined...")
        else:
            self.curs.execute("SHOW DATABASES")
            for x in self.curs:
                print(x)

    def select_DTsa(self, rowid):
        if self.curs is None:
            print("Error, cursor has not been defined...")
        else:
            self.curs.execute("SELECT * FROM fDT_systacc as sa WHERE sa.rowid_l=" + rowid)
            for x in self.curs:
                print(x)
