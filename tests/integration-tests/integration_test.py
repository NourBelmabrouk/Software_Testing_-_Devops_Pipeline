import os
import pytest

from app import create_app
from db_init import create_db


@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ["DATABASE_FILENAME"] = str(database_filename)

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__)
    testing_client = flask_app.test_client(use_cookies=True)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_index(test_client):

    #Given
    expected_status_code = 200

    # When
    response = test_client.get('/')
    
    # Then
    assert expected_status_code == response.status_code

def test_add_user(test_client):

    # Given
    request_payload = {
        "name": "zoro",
        "phone": 25687562,
        "email": "zoro@gmail.com",
        "job": "swordsman"
    }

    expected_status_code = 200

    # When
    response = test_client.post('/submitted', data=request_payload)

    # Then
    assert expected_status_code == response.status_code



def test_view_database(test_client):

    #Given
    expected_status_code = 200

    # When
    response = test_client.get('/database')
    
    # Then
    assert expected_status_code == response.status_code


def test_delete_user(test_client):

    #Given
    expected_status_code = 200
    id_to_delete = 0

    # When
    response = test_client.post('/delete'+str(id_to_delete),follow_redirects=True)
    
    # Then
    assert expected_status_code == response.status_code


def test_update_name_user(test_client):
    
    #Given
    requested_payload={
	"name":"nour"
    }
    expected_status_code = 200
    id_to_update = 0
    field_to_update="name"

    # When
    response = test_client.post('/modify'+str(id_to_update)+"/"+field_to_update,
    data=requested_payload,
    follow_redirects=True)
    
    # Then
    assert expected_status_code == response.status_code

