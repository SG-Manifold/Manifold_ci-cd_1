import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_register(client):
    # test register endpoint with valid input
    data = {
        'username': 'testuser5',
        'email': 'testuser5@example.com',
        'password': 'password123'
    }
    response = client.post('/register', json=data)
    assert response.status_code == 201
    assert response.json == {'message': 'User registered successfully', 'user_id': 14}

def test_login(client):
    # test login endpoint with valid input
    data = {
        'rusername': 'testuser2',
        'rpassword': 'password123'
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200
    assert response.json == {'message': 'User authenticated successfully', 'user_id': 11, 'is_superuser': False}

def test_create_tenant(client):
    # test create tenant endpoint with valid input
    data = {
        'name': 'testtenant2',
        'domain_name': 'testtenant2.example.com',
        'api_key': 'apikey12345'
    }
    response = client.post('/tenant', json=data)
    assert response.status_code == 201
    assert response.json == {'message': 'Tenant created successfully', 'tenant_id': 8}

def test_update_tenant(client):
    # test update tenant endpoint with valid input
    data = {
        'name': 'updatedtenant',
        'domain_name': 'updatedtenant.example.com',
        'api_key': 'updatedapikey123'
    }
    response = client.put('/tenant/3', json=data)
    assert response.status_code == 200
    assert response.json == {'message': 'Tenant updated successfully', 'tenant_id': 3}

def test_delete_tenant(client):
    # test delete tenant endpoint
    response = client.delete('/tenant/3')
    assert response.status_code == 200
    assert response.json == {'message': 'Tenant deleted successfully', 'tenant_id': 3}

def test_get_tenant(client):
    # test get tenant endpoint
    response = client.get('/tenant/3')
    assert response.status_code == 404

def test_list_tenants(client):
    # call the API endpoint
    response = client.get('/tenant')

    # assert that the response is successful
    assert response.status_code == 200

    # parse the response body as JSON
    response_body = json.loads(response.data)

    # assert that the response body is a list
    assert isinstance(response_body, list)

    # assert that each item in the list has the expected keys
    for item in response_body:
        assert set(item.keys()) == {'id', 'name', 'domain_name', 'api_key', 'created_at', 'updated_at'}

    # assert that each item in the list has the expected data types
    for item in response_body:
        assert isinstance(item['id'], int)
        assert isinstance(item['name'], str)
        assert isinstance(item['domain_name'], str)
        assert isinstance(item['api_key'], str)
        assert isinstance(item['created_at'], str)
        assert isinstance(item['updated_at'], str)

    # assert that the response body has the expected length
    assert len(response_body) == 3
