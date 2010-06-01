import MySQLdb

class Mysql:
    def __init__(self,
                 host,
                 user,
                 password,
                 database):

        self.db = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database)

        self.db.set_character_set('utf8')
        self.c = self._cursorUtf8(self.db.cursor())
    
    def _cursorUtf8(self, cursor):
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        return cursor
    
    def execute(self, query, *parameters):
        return self.c.execute(query, *parameters)

    def query(self, query, *parameters):
        return MysqlResult(self).execute(query, *parameters)

class MysqlResult:
    def __init__(self, mysql):
        self.c = mysql._cursorUtf8(mysql.db.cursor(MySQLdb.cursors.DictCursor))

    def execute(self, query, *parameters):
        self.c.execute(query, parameters)
        return self

    def fetchAll(self):
        return self.c.fetchall()
    
    def fetch(self):
        return self.c.fetchone()

    def close(self):
        self.c.close()
        return self