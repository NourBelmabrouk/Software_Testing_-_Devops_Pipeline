from unittest import TestCase, main
from unittest.mock import patch
from app import insert_data,get_all_rows_from_table,delete_data,modify_data
from app import app, db ,User



class TestUsers(TestCase):

    def setUp(self):
        self.db_uri = 'sqlite:///info.db'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQL_ALCHEMY_DATABASE_URI'] = self.db_uri
        self.app = app.test_client()
        db.create_all()


    def test_add_user(self):

        #given
        number_users=len(User.query.all())+1

        #when 
        insert_data("ali",23133667,"ali@gmail.com","retired")

        #then
        self.assertEqual(len(User.query.all()),number_users)

    def test_delete_user(self):

        #given
        number_users=len(User.query.all())-1

        #when 
        delete_data(6)

        #then
        self.assertEqual(len(User.query.all()),number_users)

    
    def test_modify_data(self):

        #given
        expected_change="graduated"

        #when 
        modify_data("5","job","graduated")
        user=User.query.filter_by(id='5').first()

        #then
        self.assertEqual(user.job,expected_change)

    def test_fetch_all(self):

        #given
        expected_number_users=5

        #when 
        number_users=len(get_all_rows_from_table())

        #then
        self.assertEqual(number_users,expected_number_users)




    
