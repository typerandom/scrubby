class Table(object):
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

    def __repr__(self):
        columns = [str(column) for column in self.columns]
        return '<Table name={name}>\n  {columns}\n</Table>'.format(
            name=self.name,
            columns='\n  '.join(columns),
        )
