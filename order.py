class Order:
    def __init__(self,product_name,customer_name, date):
        self.product_name=product_name
        self.customer_name=customer_name
        self.__date = date