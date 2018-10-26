import unittest
from app import create_app
from instance.config import app_config
import json
from app.api.v1.models import clear_data


class TestProducts(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.test_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        product_data = json.dumps({
            "name": "del",
            "model_no": "1523",
            "price": "2563",
            "quantity":"quantity"
        })
        self.sale_data = json.dumps({
            "id": 1
        })
        users_data = json.dumps({
            "username": "winnie",
            "password": "aS@1234",
            "role": "Admin"

        })
        login_data = json.dumps({
            "username": "winnie",
            "password": "aS@1234"

        })
        users_data_storeattendant = json.dumps({
            "username": "Ann",
            "password": "aS@1244",
            "role": "storeattendant"

        })
        login_data_storeattendant = json.dumps({
            "username": "Ann",
            "password": "aS@1244"

        })

        self.create_admin_user = self.test_client.post(
            '/api/v1/users', data=users_data, content_type='application/json')
        print(self.create_admin_user)
        self.login_admin_user = self.test_client.post(
            '/api/v1/login', data=login_data, content_type='application/json')

        self.create_attendant__user = self.test_client.post(
            '/api/v1/users', data=users_data_storeattendant, content_type='application/json')
        self.login_attendant_user = self.test_client.post(
            '/api/v1/login', data=login_data_storeattendant, content_type='application/json')
        print(self.login_admin_user)
        self.admin_token = json.loads(
            self.login_admin_user.data.decode())["token"]
        print(self.admin_token)
        self.storeattendant_token = json.loads(
            self.login_attendant_user.data.decode())["token"]

        self.create_product = self.test_client.post('api/v1/products', data=product_data, headers={
                                                    'content-type': 'application/json', 'access-token': self.admin_token})
        self.create_sale = self.test_client.post('api/v1/sales', data=self.sale_data, headers={
                                                 'content-type': 'application/json', 'access-token': self.storeattendant_token})
        

        print(self.create_product.data)
        print(self.create_sale.data)

    def tearDown(self):
        clear_data()

        self.app_context.pop()

    def test_signup(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "Aa@5050",
            "role": "Admin"
        })
        user = json.dumps({
            "username": "Morgan",
            "password": "Bb#6060",
            "role": "storeattendant"
        })

        response = self.test_client.post(
            '/api/v1/users', data=user, content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_login(self):
        login = json.dumps({
            "username": "winnie",
            "password": "aS@1234"
        })
        response = self.test_client.post(
            '/api/v1/login', data=login, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_products(self):

        response = self.test_client.get(
            'api/v1/products', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_products(self):
        data2 = json.dumps({
            "name": "del",
            "model_no": "1523",
            "price": "2516",
            "role": "role",
            "quantity":"quantity"

        })

        response = self.test_client.post('api/v1/products', data=data2, headers={
                                         'content-type': 'application/json', 'access-token': self.admin_token})
        self.assertEqual(response.status_code, 201)

    def test_get_sales(self):

        response = self.test_client.get(
            'api/v1/sales', headers={'content_type': 'application/json', 'access-token': self.admin_token})
        self.assertEqual(response.status_code, 200)

    def test_post_sales(self):

        response = self.test_client.post('api/v1/sales', data=self.sale_data, headers={
                                         'content_type': 'application/json', 'access-token': self.storeattendant_token})
        
        self.assertEqual(response.status_code, 201)


    def test_get_single_products(self):
        data2 = json.dumps({
            "name": "del",
            "model_no": "1523",
            "price": "2516",
            "role": "role",
            "quantity":"quantity"

        })

        response = self.test_client.post('api/v1/products', data=data2, headers={
                                         'content-type': 'application/json', 'access-token': self.admin_token})
        response2 = self.test_client.get(
            'api/v1/products/1', content_type='application/json')
        self.assertEqual(response2.status_code, 200)

    def test_get_single_sales_admin(self):

        response = self.test_client.get(
            'api/v1/sales/1', headers={'content_type': 'application/json', 'access-token': self.admin_token})

        self.assertEqual(response.status_code, 200)

    def test_get_single_sales_attendant(self):

        response = self.test_client.get('api/v1/sales/1', headers={
                                        'content_type': 'application/json', 'access-token': self.storeattendant_token})
        print(response)

        self.assertEqual(response.status_code, 200)

    def test_password_lowercase(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "A@5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have a lowercase letter")
        self.assertEqual(response.status_code, 400)

    def test_password_uppercase(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "a@5050",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have an uppercase letter")
        self.assertEqual(response.status_code, 400)

    def test_password_digit(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "a@Afff",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have atleast one digit")
        self.assertEqual(response.status_code, 400)

    def test_password_special_char(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "a1Afff",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have atleast one special character")
        self.assertEqual(response.status_code, 400)

    def test_password_length(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "a1A@",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})

        self.assertEqual(json.loads(response.data)
                         ['message'], "password must  have a minimum of 6 characters")
        self.assertEqual(response.status_code, 400)

    # def test_username_str(self):
    #     user = json.dumps({
    #         "username": int(Harriet),
    #         "password": "a1A@fffgh",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v1/users", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})

    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Strings only")
    #     self.assertEqual(response.status_code, 400)
    def test_empty_username(self):
        user = json.dumps({
            "username": "",
            "password": "Aa1@ffff",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Details required")
        self.assertEqual(response.status_code, 400)
    def test_empty_password(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "password must have an uppercase letter")
        self.assertEqual(response.status_code, 400)
    def test_empty_role(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "Aa1@ffff",
            "role": ""})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Details required")
        self.assertEqual(response.status_code, 400)

    def test_empty_space_role(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "Aa1@ffff",
            "role": "Ad min"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Remove space")
        self.assertEqual(response.status_code, 400)
    def test_empty_space_password(self):
        user = json.dumps({
            "username": "Harriet",
            "password": "Aa1 @ffff",
            "role": "Admin"})
        response = self.test_client.post("/api/v1/users", data=user,
                                         headers={
                                             'content-type': 'application/json'})
        self.assertEqual(json.loads(response.data)
                         ['message'], "Remove space")
        self.assertEqual(response.status_code, 400)

    # def test_empty_space_username(self):
    #     user = json.dumps({
    #         "username": " Harriet",
    #         "password": "Aa1@ffff",
    #         "role": "Admin"})
    #     response = self.test_client.post("/api/v1/users", data=user,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Remove space")
    #     self.assertEqual(response.status_code, 400)
    # def test_details_data(self):
    #     product = json.dumps({
    #         "name":""
    #         "model_no": "1523",
    #         "price": "2516",
    #         "role": "role",
    #         "quantity":"quantity"
    #         })
    #     response = self.test_client.post("/api/v1/users", data=product,
    #                                      headers={
    #                                          'content-type': 'application/json'})
    #     self.assertEqual(json.loads(response.data)
    #                      ['message'], "Provide all product Details")
    #     self.assertEqual(response.status_code, 400) 