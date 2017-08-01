from .execution_step import ExecutionStep

class ClearTableColumnExecutionStep(ExecutionStep):
    def __init__(self, table_name, column_name):
        self.table_name = table_name
        self.column_name = column_name

    def run(self, db):
        return db.clear_table_column(self.table_name, self.column_name)

    def explain(self):
        return 'Clear all columns values of {column} on table {table}.'.format(
            table=self.table_name,
            column=self.column_name,
        )