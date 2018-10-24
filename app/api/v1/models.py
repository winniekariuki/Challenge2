products = []
sale_records = []
users = []

class Signup():
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role


    def add_user(self):
        id = len(users) + 1
        user = {
            'username':self.username,
            'password':self.password,
            'role':self.role

        }
        users.append(user)

class Product():
    def __init__(self,name,model_no,price,quantity,date):
        self.name = name
        self.model_no = model_no
        self.price = price
        self.quantity = quantity
        self.date = date


    def post_products(self):
        
        item = {
            'id':len(products) + 1,
            'name':self.name,
            'model_no':self.model_no,
            'price':self.price,
            'quantity':self.quantity,
            'date':self.date

            }
        products.append(item)
class record():
    def __init__(self,id,product):
        self.id = id
        sale = {
                'sale_id':len(sale_records)+1,
                'sale':product,
                'StoreAttendant_id':user_data["id"]
                
                }
        sale_records.append(sale)


def clear_data():
    users.clear
    products.clear
    sale_records.clear    