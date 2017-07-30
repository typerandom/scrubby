import yaml

from .definition import Definition
from .table_definition import TableDefinition

class DefinitionFileReader(object):
    def read(self, filepath):
        definition = Definition()

        with open(filepath, 'r') as stream:
            try:
                data = yaml.load(stream)

                for table in data.get('tables', {}).iteritems():
                    definition.tables.append(TableDefinition.from_yaml(table))
            except yaml.YAMLError as error:
                print(error)

        return definition