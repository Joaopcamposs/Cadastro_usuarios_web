from unittest import mock, TestCase
from backend.app.main import app
from fastapi.testclient import TestClient


class TestAPI(TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_get_root_main_return_status_200(self):
        response = self.client.get("/api")
        self.assertEqual(200, response.status_code)

    def test_get_root_main_return_json(self):
        response = self.client.get("/api")
        self.assertEqual('application/json', response.headers.get('content-type'))

    @mock.patch('backend.app.crud.get_all_users')
    async def test_get_all_users_return_json_and_status_200(self, mock_api):
        response = self.client.get('/api/users')
        self.assertEqual('application/json', response.headers.get('content-type'))
        self.assertEqual(200, response.status_code)

    @mock.patch('backend.app.crud.get_user_by_cpf')
    async def test_get_user_return_json_and_status_200(self, mock_api):
        response = self.client.get('/api/user/{user_cpf}')
        self.assertEqual('application/json', response.headers.get('content-type'))
        self.assertEqual(200, response.status_code)

    @mock.patch('backend.app.crud.create_user')
    async def test_create_user_return_json_and_status_200(self, mock_api):
        user = {
            "name": "string", "email": "string", "country": "string",
            "state": "string", "city": "string", "postal_code": "string",
            "street": "string", "number": "string", "complement": "string",
            "CPF": "string", "PIS": "string", "hashed_password": "string"
        }
        response = self.client.post('/api/user', json=user)
        self.assertEqual('application/json', response.headers.get('content-type'))
        self.assertEqual(200, response.status_code)

    @mock.patch('backend.app.crud.update_user')
    async def test_update_user_return_json_and_status_200(self, mock_api):
        user = {
            "name": "string", "email": "string", "country": "string",
            "state": "string", "city": "string", "postal_code": "string",
            "street": "string", "number": "string", "complement": "string",
            "CPF": "string", "PIS": "string", "hashed_password": "string"
        }
        response = self.client.put('/api/user/{user_cpf}', json=user)
        self.assertEqual('application/json', response.headers.get('content-type'))
        self.assertEqual(200, response.status_code)

    @mock.patch('backend.app.crud.delete_user')
    async def test_delete_user_return_json_and_status_200(self, mock_api):
        response = self.client.delete('/api/user/{user_cpf}')
        self.assertEqual('application/json', response.headers.get('content-type'))
        self.assertEqual(200, response.status_code)

    @mock.patch('backend.app.services.create_token')
    async def test_generate_token_return_json_and_status_200(self, mock_api):
        token = {
            'form_data.username': 'user', 'form_data.password': 'password'
        }
        response = self.client.post('/api/token', json=token)
        self.assertEqual('application/x-www-form-urlencoded', response.headers.get('content-type'))
        self.assertEqual(200, response.status_code)

    @mock.patch('backend.app.crud.get_user')
    async def test_get_current_user_return_json_and_status_200(self, mock_api):
        response = self.client.get('/api/users/me')
        self.assertEqual('application/json', response.headers.get('content-type'))
        self.assertEqual(200, response.status_code)
