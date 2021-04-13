import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]
order_management_db = myclient["order_management"]


def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code})

    return product

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({}):
        product_list.append(p)

    return product_list


def get_branch(code):
    branches_coll = products_db["branches"]
    branch = branches_coll.find_one({"code":code})

    return branch

def get_branches():
    branch_list = []
    branches_coll = products_db["branches"]

    for v in branches_coll.find({}):
        branch_list.append(v)

    return branch_list

def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user
    return branch_list

def update_password(username, newpassword):
    customers_coll = order_management_db['customers']
    updatepassword = customers_coll.update_one({"username":username},{"$set":{"password":newpassword}})
    return updatepassword

def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)

def get_pastorders():
    pastorder_list = []
    orders_coll = order_management_db["orders"]
    orderdetails_coll = orders_coll["details"]

    for order in orders_coll.find({},{"details":1}):
        for o in order["details"]:
            pastorder_list.append(o)

    return pastorder_list
