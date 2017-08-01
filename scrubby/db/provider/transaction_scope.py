class TransactionScope(object):
    def __init__(self, database):
        self._database = database
        self._cursor = cursor

    def begin(self):
        self._cursor = self.database.cursor()

    def rollback(self):
        self._cursor.rollback()

    def commit(self):
        self._cursor.commit()

    def execute(self, query):
        return self._cursor.execute(query)

    def __enter__(self):
        self.begin()

    def __exit__(self):
        try:
            self.commit()
        except:
            self.rollback()