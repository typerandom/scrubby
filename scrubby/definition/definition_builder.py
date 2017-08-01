from ..db.provider import NullProvider

class DefinitionBuilder(object):
    def __init__(self, db):
        self.valid_db = not isinstance(db, NullProvider)
        self.db_tables = db.get_tables()

    def build(self, definition):
        errors = []
        valid_tables = {}

        for table in self.db_tables:
            valid_columns = {}

            for column in table.columns:
                valid_columns[column.name] = None

            valid_tables[table.name] = valid_columns


        for index, table in enumerate(definition.tables):
            if table.name == '*':
                del definition.tables[index]
                continue
            elif self.valid_db and not table.name in valid_tables:
                errors.append('Table {table} does not exist.'.format(
                    table=table.name,
                ))

            for field_index, field in enumerate(table.fields):
                if field.name == '*':
                    del table.fields[field_index]
                elif self.valid_db and not field.name in valid_tables[table.name]:
                    errors.append('Column {column} does not exist on table {table}.'.format(
                        table=table.name,
                        column=field.name,
                    ))

        if errors:
            print('Found errors when parsing file:')

            for error in errors:
                print(' - ' + error)

            exit()

        return definition