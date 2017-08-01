from .execution_step import ExecutionStep

class ExecutionPlan(object):
    def __init__(self, name=None):
        self.name = name
        self.execution_steps = []

    def add_step(self, step):
        if not isinstance(step, ExecutionPlan) and not isinstance(step, ExecutionStep):
            raise Exception('Execution step must be an instance of either ExecutionPlan or ExecutionStep.')

        self.execution_steps.append(step)

    def run(self, db):
        for step in self.execution_steps:
            print('Running: ' + step.explain())
            step.run(db)

        db._connection.commit()

    def explain(self):
        logs = []

        if self.name:
            logs.append(self.name + ':')

        for step in self.execution_steps:
            logs.append(step.explain())

        return '\n'.join(logs) + '\n'

    def __repr__(self):
        return '<ExecutionPlan>\n{steps}\n</ExecutionPlan>'.format(
            steps=self.execution_steps,
        )