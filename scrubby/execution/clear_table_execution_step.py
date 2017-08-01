from .execution_step import ExecutionStep

class ClearTableExecutionStep(ExecutionStep):
    def __init__(self, table_name):
        self.table_name = table_name

    def run(self, db):
        return db.clear_table(self.table_name)

    def explain(self):
        return 'Clear all rows on table {table}.'.format(
            table=self.table_name,
        )