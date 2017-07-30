from .table_field_definition import TableFieldDefinition

class TableDefinition(object):
    def __init__(self, name, action, fields):
        self.name = name
        self.action = action
        self.fields = fields

    @staticmethod
    def from_yaml(data):
        table, options = data

        fields = []

        for field in options.get('fields', {}).iteritems():
            fields.append(TableFieldDefinition.from_yaml(field))

        return TableDefinition(
            name=table,
            action=options.get('action', None),
            fields=fields,
        )

    def __repr__(self):
        return '<Table name={name} action={action}>\n{fields}\n</Table>'.format(
            name=self.name,
            action=self.action,
            fields='\n'.join(['  ' + str(field) for field in self.fields]),
        )