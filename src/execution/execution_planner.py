from .execution_plan import ExecutionPlan
from .clear_table_execution_step import ClearTableExecutionStep
from .clear_table_column_execution_step import ClearTableColumnExecutionStep

class ExecutionPlanner(object):
    '''
    Turns a definition into an execution plan.
    '''
    def create(self, definition):
        plan=ExecutionPlan()

        for table in definition.tables:
            sub_plan = ExecutionPlan(table.name)

            if table.action == 'clear':
                sub_plan.add_step(ClearTableExecutionStep(table.name))
            elif len(table.fields) > 0:
                for field in table.fields:
                    if field.action == 'clear':
                        sub_plan.add_step(ClearTableColumnExecutionStep(table.name, field.name))

            if len(sub_plan.execution_steps):
                plan.add_step(sub_plan)

        return plan