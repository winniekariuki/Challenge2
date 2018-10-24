
from flask_restful import Api
from flask import Blueprint

from .views import Produce,SingleProduct,SaleRecord,SingleSaleRecord,UserAccount,LoginUser

version1 = Blueprint('api',__name__,url_prefix='/api/v1')

api=Api(version1)

api.add_resource(LoginUser,'/login')
api.add_resource(UserAccount,'/users')
api.add_resource(Produce,'/products')
api.add_resource(SingleProduct,'/products/<productID>')
api.add_resource(SaleRecord,'/sales')
api.add_resource(SingleSaleRecord,'/sales/<saleID>')
