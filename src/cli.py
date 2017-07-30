import argparse

from .db import PostgresProvider
from .definition import DefinitionFileReader, DefinitionBuilder
from .execution import ExecutionPlanner

class CLI(object):
    def __init__(self):
        self.parser = self._make_parser()

    def _make_parser(self):
        parser = argparse.ArgumentParser(
            description='Optional app description'
        )

        parser.add_argument(
            '--filepath',
            type=str,
            help='The path to a Scrubby definition file (.scrub).'
        )

        parser.add_argument(
            '--database',
            type=str,
            help='Database connection string.'
        )

        parser.add_argument(
            '--explain',
            type=bool,
            nargs='?',
            help='Explain the execution plan.'
        )

        parser.add_argument(
            '--exclude',
            type=str,
            nargs='?',
            help='Tags in definition to exclude.'
        )

        parser.add_argument(
            '--include',
            type=str,
            nargs='?',
            help='Tags in definition to include.'
        )

        return parser

    def _action_run(self, db, definition, options):
        execution_planner=ExecutionPlanner()

        execution_plan = execution_planner.create(definition)

        if options['explain']:
            print(execution_plan.explain())
        else:
            execution_plan.run(db)

    def run(self):
        options={}

        args = self.parser.parse_args()

        host, username, password, dbname = args.database.split(';')
        db=PostgresProvider(host, username, password, dbname)

        with db:
            definition_reader = DefinitionFileReader()
            definition = definition_reader.read(args.filepath)

            db_tables = db.get_tables()
            definition_builder = DefinitionBuilder(db_tables)
            definition = definition_builder.build(definition)

            if args.exclude:
                options['exclude'] = args.exclude

            if args.include:
                options['include'] = args.include

            options['explain'] = bool(args.explain)

            self._action_run(db, definition, options)