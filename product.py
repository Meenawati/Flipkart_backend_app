class Product:
    __price=0
    __category_name=None

    def __init__(self,title):
        self.__title=title

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, category_name):
        self.__category_name = category_name