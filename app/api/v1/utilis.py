import re
from flask import abort,jsonify,make_response
from .models import users, products

class Register:
    def pass_validate(self, data):

        if not re.search("[A-Z]",data["password"]):
            Response = "password must have an uppercase letter"
            abort(400,Response )

        elif not  re.search("[a-z]",data["password"]):
            Response = "password must have a lowercase letter"
            abort(400,Response )

        elif not re.search("[0-9]",data["password"]):
            Response = "password must have atleast one digit"
            abort(400,Response )

        elif not  re.search("[$#@]",data["password"]):
            Response = "password must have atleast one special character"
            abort(400,Response )

        elif len(data["password"])<6 or len(data["password"])>12:
            Response = "password must  have a minimum of 6 characters"
            abort(400,Response )

    def data_validate(self,data):
        if type(data["username"]) is not str or type(data["password"]) is not str or type(data["role"]) is not str :

            Response ="Strings only "

            abort(400, Response)

    def empty_validate(self, data):
        if data["username"] =="" or data["password"] =="" or data["role"] =="" :
            Response ="Details required"
            abort(400, Response)

    def space_validate(self,data):
        if " " in data["username"]:
            Response = "Remove space "
            abort(400, Response)
        if " " in data["password"]:
            Response = "Remove space"
            abort(400, Response)
        if " " in data["role"]:
            Response = "Remove space"
            abort(400, Response)
        

class Validateproduct:

    def detailsvalidate(self,data):

        if "name" not in data or "model_no" not in data or "price" not in data or "quantity" not in data :
            Response = "Provide all product Details"
            abort(400, Response)

    def emptydetails(self, data):
        if data["name"] =="" or data["model_no"] =="" or data["quantity"] =="" or  data["price"] =="":
            Response ="Details required"
            abort(400, Response)


    







        
    