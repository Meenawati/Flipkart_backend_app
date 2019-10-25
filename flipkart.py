class Flipkart:
    __admins={}
    __sellers={}
    __category_and_products={None:[]}
    __customers={}

    def get_products_by_category(self, category):
        return self.__category_and_products.get(category)

    def add_product_into_category(self, product, category):
        if self.__category_and_products.get(category) is None:
            self.__category_and_products.update({category: [product]})
        else:
            list = self.__category_and_products.get(category)
            list.append(product)
            self.__category_and_products.update({category:list})

    def get_customers(self):
        return self.__customers

    def get_customer(self,name):
        return self.__customers.get(name)

    def add_customer(self, customer):
        self.__customers.update({customer.get_name(): customer})

    def remove_customer(self, name):
        customer = self.get_customer(name)
        self.__customers.pop(customer)

    def get_sellers(self):
        return self.__sellers

    def get_seller(self,name):
        return self.__sellers.get(name)

    def add_seller(self, seller):
        self.__sellers.update({seller.get_name():seller})

    def remove_seller(self, name):
        seller = self.get_sellers(name)
        self.__sellers.pop(seller)

    def get_admins(self):
        return self.__admins

    def get_admin(self,name):
        return self.__admins.get(name)

    def add_admin(self, admin):
        self.__admins.update({admin.get_name(): admin})

    def remove_admin(self, name):
        admin = self.get_admin(name)
        self.__admins.pop(admin)