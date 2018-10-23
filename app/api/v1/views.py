from flask import make_response, request, jsonify
from flask import Flask
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import json
from instance.config import Config

from .models import *


#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'thisissecret'


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        user_data = None
        if 'access_token' in request.headers:
             token = request.headers['access_token']

        if not token:
            return make_response(jsonify({
                "message": "Login!!"
                }), 401)
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            for user in users:
                if user['username'] == data['username']:
                    user_data = user
        except:
            return jsonify({"message": "Invalid Token!"}), 401

        return f(user_data, *args, **kwargs)
    return decorator


class UserAccount(Resource):
    def get(self):
        return make_response(jsonify({
            "Status": "Ok",
            "Message": "Success",
            "UserAccount": users
            }), 200)

    def post(self):
        id = len(users) + 1
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        role = data["role"]

        register = Signup(username,password,role)
        register.add_user()

        return make_response(jsonify({
                    "Status": "Ok",
                    "Message": "Post Success",
                    "UserAccount": users
                }), 201)


class LoginUsers(Resource):
    def post(self):
        # print(users)
        data = request.get_json()
        username = data["username"]
        password = data["password"]


        if not data or not username or not password:
            return make_response(jsonify({
                                         'Status': 'Failed',
                                         'Message': "Login!!"
                                         }), 400)

        for user in users:
            if user['username'] == username and user['password'] == password:
                token = jwt.encode({'username': user['username'],
                                    'exp': datetime.datetime.utcnow() +
                                    datetime.timedelta(minutes=30)},
                                    Config.SECRET_KEY)
                return make_response(jsonify({
                                             'token': token.decode('UTF-8')
                                             }), 200)

        return make_response(jsonify({
                'Status': 'Failed',
                'Message': "No such user found"
                }), 404)
        # data=data

        # if not auth or not auth.username or not auth.password:
        #   return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login required!"'})
        # user=users.filter_by(name=auth.username).first()

        # if not user:
        #   return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login required!"'})

        # if check_password_hash(user.password,auth.password):
        #   token = jwt.encode({'id':users.id,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
        #   return jsonify({'token':token.decode('UTF-8')})
        # return make_response('Could not verify',401,{'WWW-Authenticate':'Basic realm="Login required!"'})


class Products(Resource):
    def get(self):
        return make_response(jsonify({

            "Status": "Ok",
            "Message": "Success",
            "MyProducts": products

            }), 200)
    @token_required
    def post(user_data,self):
        if user_data == "Admin":
           return make_response(jsonify({
                "message":"Not authorized"
                }) ,401)

        id = len(products) + 1
        data = request.get_json()
        name = data["name"]
        model_no = data["model_no"]
        price = data["price"]

        device = AddProducts(name,model_no,price)
        device.post_products()


        return make_response(jsonify({
                    "Status": "Ok",
                    "Message": "Post Success",
                    "MyProducts": products
                }), 201)


class SingleProduct(Resource):
        def get(self, productID):

            for product in products:
                if product["id"] == int(productID):

                    return make_response(jsonify({
                        "Status": "Ok",
                        "Message": "Success",
                        "MyProducts": product

                        }), 200)


class SaleRecords(Resource):
    @token_required
    def get(user_data, self):
        if  user_data["role"] != "Admin":
           return make_response(jsonify({
                "message":"Not authorized"
                }) ,401)

        return make_response(jsonify({
                        "Status":"Ok",
                        "Message":"Success",
                        "MySaleRecords":sale_records

                        }),200)
    @token_required   
    def post(user_data,self):

        if user_data["role"] != "storeattendant":
           return make_response(jsonify({
                "message":"Not authorized"
                }) ,401)       
        data=request.get_json()
        print(data)
        for product in products:
            if product['id'] == data:
                sale = {
                        'sale_id':len(sale_records)+1,
                        'sale':product,
                        'StoreAttendant_id':user_data["id"]
                        
                        }
                sale_records.append(sale)
            return make_response(jsonify({
                                    "Status":"Created",
                                    "Message":"Post Success",
                                    "MySaleRecords":sale_records
                                }),201)
class SingleSaleRecord(Resource):
        @token_required
        def get(user_data,self,saleID):
            
            for sale in sale_records:
                if user_data["role"] != 'Admin' or user_data["id"] != StoreAttendant_id:
                    return make_response(jsonify({
                        "message":"Not authorized"
                         }) ,401)
            for sale in sale_records:
                if sale['sale_id'] == int(saleID):
                    return make_response(jsonify({
                                "Status":"Ok",
                                "Message":"Success",
                                "MySaleRecords":sale

                                }),200)
            
