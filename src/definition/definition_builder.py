class DefinitionBuilder(object):
    def __init__(self, db_tables):
        self.db_tables = db_tables

    def build(self, definition):
        errors = []
        valid_tables = {}

        for table in self.db_tables:
            valid_tables[table.name] = None

        for index, table in enumerate(definition.tables):
            if table.name == '*':
                # Iterate all fields and
                del definition.tables[index]
            elif not table.name in valid_tables:
                errors.append('Table {table} does not exist.'.format(
                    table=table.name,
                ))

        if errors:
            print('Found errors when parsing file:')

            for error in errors:
                print(' - ' + error)

            exit()

        return definition