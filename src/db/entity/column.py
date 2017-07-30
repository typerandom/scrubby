class Column(object):
    def __init__(self, name, type, default_value, is_primary):
        self.name = name
        self.type = type
        self.default_value = default_value
        self.is_primary = is_primary

    def __repr__(self):
        return '<Column name={name} type={type} />'.format(
            name=self.name,
            type=self.type,
        )