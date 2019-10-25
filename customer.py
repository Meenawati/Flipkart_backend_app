from cart import Cart

class Customer:
    __orders=[]
    __bank=None
    __amount=0
    __cart=None

    def __init__(self,name):
        self.__name=name
        self.__cart = Cart(name)

    def get_name(self):
        return self.__name

    def add_product(self,product):
        self.__cart.add_product(product)

    def get_orders(self):
        return self.__orders

    def add_order(self,order):
        self.__orders.append(order)

    def remove_order(self,order):
        self.__orders.remove(order)

    def get_bank(self):
        self.__bank

    def set_bank(self,bank):
        self.__bank=bank

    def get_amount(self):
        return self.__amount

    def set_amount(self,amount):
        self.__amount=amount

    def add_cart(self,cart):
        self.__cart=cart

    def get_cart(self):
        return self.__cart