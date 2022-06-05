from unittest import TestCase, main
from unittest.mock import patch
from functions import insert_data,get_all_rows_from_table,delete_data,modify_data
import os

os.environ['DATABASE_FILENAME'] = 'info.db'

class TestUsers(TestCase):

    @patch("functions.sqlite3")
    def test_add_user(self,mock_class):

        # given
        mock_execute= (mock_class.connect.return_value.execute)

        #when 
        insert_data("ali",23133667,"ali@gmail.com","retired")

        #then
        mock_execute.assert_called_once()

    @patch("functions.sqlite3")
    def test_fetch_all(self,mock_class):
        # Given
        mock_class.connect().cursor().execute().fetchall.return_value = [
            ('Lee',12,'lee@aol.com','student'),
            ('Kory',13,'kory@aol.com','UX Developer'),
            ('Laura',14,'laura@aol.com','Project Manager')
            ]
        expected_users=[
            ('Lee',12,'lee@aol.com','student'),
            ('Kory',13,'kory@aol.com','UX Developer'),
            ('Laura',14,'laura@aol.com','Project Manager')
            ]

        #When
        result_users=get_all_rows_from_table()

        #Then
        self.assertEqual(expected_users, result_users)

    @patch("functions.sqlite3")
    def test_delete_user(self,mock_class):

        # given
        mock_execute= (mock_class.connect.return_value.execute)

        # When
        delete_data(0)

        #Then
        mock_execute.assert_called_once()

    @patch("functions.sqlite3")
    def test_update_name_user(self,mock_class):

        # given
        mock_execute= (mock_class.connect.return_value.execute)

        # When
        modify_data(0,'name','nour')

        #Then
        mock_execute.assert_called_once()

    @patch("functions.sqlite3")
    def test_update_phone_user(self,mock_class):

        # given
        mock_execute= (mock_class.connect.return_value.execute)

        # When
        modify_data(0,'phone',147)

        #Then
        mock_execute.assert_called_once()


    @patch("functions.sqlite3")
    def test_update_email_user(self,mock_class):

        # given
        mock_execute= (mock_class.connect.return_value.execute)

        # When
        modify_data(0,'email','nour@gmail.com')

        #Then
        mock_execute.assert_called_once()

    @patch("functions.sqlite3")
    def test_update_job_user(self,mock_class):

        # given
        mock_execute= (mock_class.connect.return_value.execute)

        # When
        modify_data(0,'job','retired')

        #Then
        mock_execute.assert_called_once()

 




    
