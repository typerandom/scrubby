class Definition(object):
    def __init__(self):
        self.tables = []

    def __repr__(self):
        return '<Definition>\n{tables}\n</Definition>'.format(
            tables='\n'.join([str(table) for table in self.tables]),
        )