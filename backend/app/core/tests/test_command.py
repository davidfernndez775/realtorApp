'''
Test custom Django management commands
'''
from unittest.mock import patch    

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError     # simulate operational db errors
from django.test import SimpleTestCase

# simulate the method Command.check of the command wait_for_db 
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    '''Test commands'''

    def test_wait_for_db_ready(self, patched_check):
        '''Test waiting for database if database is ready'''

        # simulate the method Command.check and retrieve that the 
        # database is available
        patched_check.return_value = True
        # call the command
        call_command('wait_for_db')
        # check that the check method was call only one time
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        '''Test waiting for database when getting OperationalError'''

        # the method retrieve PsycopgError 2 times and OperationalError 3 times
        patched_check.side_effect = [
            Psycopg2Error]*2 + [OperationalError]*3+[True]
        # call the command
        call_command('wait_for_db')
        # check that the check method was call 6 times, 2 for PsycopgError,
        # 3 for OperationalError and 1 when the database is available 
        self.assertEqual(patched_check.call_count, 6)
        # check that the last time that call check method was with 
        # databases=['default'] argument
        patched_check.assert_called_with(databases=['default'])
