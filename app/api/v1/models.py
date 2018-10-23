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

class AddProducts():
    def __init__(self,name,model_no,price):
        self.name = name
        self.model_no = model_no
        self.price = price

    def post_products(self):
        
        item = {
            'id':len(products) + 1,
            'name':self.name,
            'model_no':self.model_no,
            'price':self.price

            }
        products.append(item)

def clear_data():
    users.clear
    products.clear
    sale_records.clear    