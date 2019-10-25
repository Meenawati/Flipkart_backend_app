class Seller:
    __selling_products_and_quantities={}

    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def add_product_and_quanity(self, product, quantity):
        if self.__selling_products_and_quantities.get(product) is None:
            self.__selling_products_and_quantities.update({product: quantity})
        else:
            q1 = self.__selling_products_and_quantities.get(product)
            q1 = q1 + quantity
            self.__selling_products_and_quantities.update({product: q1})

    def get_selling_products_and_quantities(self):
        return self.__selling_products_and_quantities

    def get_quantities_for_product(self, product):
        return self.__selling_products_and_quantities.get(product)