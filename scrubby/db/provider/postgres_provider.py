import psycopg2

from .provider import Provider
from ..entity import Table, Column

class PostgresProvider(Provider):
    def __init__(self, host, username, password, name):
        self.host = host
        self.username = username
        self.password = password
        self.name = name
        self._connection = None
        self._cursor = None

    def connect(self):
        self._connection = psycopg2.connect("dbname='{name}' user='{username}' host='{host}' password='{password}'".format(
            host=self.host,
            username=self.username,
            password=self.password,
            name=self.name,
        ))

        self._cursor = self._connection.cursor()

    def close(self):
        self._cursor.close()
        self._connection.close()

    def get_table_columns(self, table_name):
        columns = []

        with self._connection.cursor() as column_cursor:
            column_cursor.execute('SELECT column_name, is_nullable, data_type, character_maximum_length, column_default FROM information_schema.columns WHERE table_catalog=\'{name}\' AND table_name=\'{table}\''.format(
                name=self.name,
                table=table_name,
            ))

            for column_name, is_nullable, data_type, character_maximum_length, column_default in column_cursor.fetchall():
                columns.append(Column(
                    name=column_name,
                    type=data_type,
                    default_value=column_default,
                    is_primary=None,
                ))

        return columns

    def get_tables(self):
        tables = []

        def get_table_primary_key(table_name):
            query="SELECT pg_attribute.attname, format_type(pg_attribute.atttypid, pg_attribute.atttypmod) FROM pg_index, pg_class, pg_attribute, pg_namespace WHERE pg_class.oid = 'decisioning_modelresult'::regclass AND indrelid = pg_class.oid AND nspname = 'public' AND pg_class.relnamespace = pg_namespace.oid AND pg_attribute.attrelid = pg_class.oid AND pg_attribute.attnum = any(pg_index.indkey) AND indisprimary"

        with self._connection.cursor() as table_cursor:
            table_cursor.execute('SELECT relname FROM pg_class WHERE relkind=\'r\' AND relname !~ \'^(pg_|sql_)\';')

            for table in table_cursor.fetchall():
                table_name = table[0]

                columns = self.get_table_columns(table_name)

                tables.append(Table(table_name, columns))

        return tables

    def execute(self, query, **kwargs):
        formatted_query = query.format(**kwargs)
        #print('Executing query %s' % formatted_query)
        return self._cursor.execute(formatted_query)

    def clear_table(self, table_name):
        return self.execute(
            'TRUNCATE TABLE {table};',
            table=table_name,
        )

    def clear_table_column(self, table_name, column_name):
        return self.execute(
            'UPDATE {table} SET "{column}"=\'\';',
            table=table_name,
            column=column_name,
        )