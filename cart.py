class Cart:
    __products=[]

    def __init__(self,customer_name):
        self.customer_name=customer_name

    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product):
        self.__products.remove(product)