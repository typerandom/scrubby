class ExecutionStep(object):
    def run(self, db):
        raise NotImplementedError('Method run(self, db) is not implemented.')

    def explain(self):
        raise NotImplementedError('Method explain(self) is not implemented.')