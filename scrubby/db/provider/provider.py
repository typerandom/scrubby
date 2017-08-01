class Provider(object):
    def connect(self):
        raise NotImplementedError('Method connect(self) is not implemented.')

    def close(self):
        raise NotImplementedError('Method close(self) is not implemented.')

    def get_tables(self):
        raise NotImplementedError('Method get_tables(self) is not implemented.')

    def clean_table(self, table_name):
        raise NotImplementedError('Method clean_table(self, table_name) is not implemented.')

    def clear_table_column(self, table_name, column_name):
        raise NotImplementedError('Method clear_table_column(self, table_name, column_name) is not implemented.')

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, type, value, traceback):
        self.close()