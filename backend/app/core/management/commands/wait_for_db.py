'''
Django command to wait for the database to be available
'''

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    '''Django command to wait for database'''

    def handle(self, *args, **options):
        '''Entry point for command'''
        # message in console 
        self.stdout.write('Waiting for database...')
        # first the database is not connected
        db_up = False
        # wait for database connection
        while db_up is False:
            try:
                # check if the database is available
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                # wait a second to try again
                time.sleep(1)
        # message in console
        self.stdout.write(self.style.SUCCESS('Database available!'))
