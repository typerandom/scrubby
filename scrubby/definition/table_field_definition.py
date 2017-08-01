class TableFieldDefinition(object):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    @staticmethod
    def from_yaml(data):
        field, options = data

        return TableFieldDefinition(
            name=field,
            action=options.get('action', None),
        )

    def __repr__(self):
        return '<Field name={name} action={action} />'.format(
            name=self.name,
            action=self.action,
        )