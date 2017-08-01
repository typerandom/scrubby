from .provider import Provider

class NullProvider(Provider):
    def connect(self):
        pass

    def close(self):
        pass

    def get_table_columns(self, table_name):
        return []

    def get_tables(self):
        return []

    def execute(self, query, **kwargs):
        return None

    def clear_table(self, table_name):
        pass

    def clear_table_column(self, table_name, column_name):
        pass