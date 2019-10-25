from flipkart import Flipkart
from admin import Admin
from seller import Seller
from product import Product
from product_categories import Product_Categories
from customer import Customer
from order import Order
from datetime import datetime

a1 = Admin("Baba")

flip = Flipkart()
flip.add_admin(a1)

seller1=Seller("Mohit")
seller2=Seller("Hitesh")

flip.add_seller(seller1)
flip.add_seller(seller2)

product1 = Product("Mobile")
product2 = Product("Top")
product3 = Product("Chhapal")
product4 = Product("light")

seller1.add_product_and_quanity(product1,20)
seller1.add_product_and_quanity(product2,12)
seller2.add_product_and_quanity(product2,10)
seller2.add_product_and_quanity(product3,43)
seller2.add_product_and_quanity(product4,3)
seller1.add_product_and_quanity(product4,5)

flip.add_product_into_category(product1,Product_Categories.ELECTRONICS)
flip.add_product_into_category(product2,Product_Categories.CLOTHING)
flip.add_product_into_category(product3,Product_Categories.FOOTWEAR)
flip.add_product_into_category(product4,Product_Categories.DECORATIONS)

c1 = Customer("Meena")
c1.add_product(product3)
c1.add_product(product2)
c1.add_product(product1)
flip.add_customer(c1)

t1=datetime(year=2019,month=10,day=19,hour=22,minute=30,second=12)
o1 = Order("Chappal","Meena",t1)
c1.add_order(o1)

###########################################
products = flip.get_products_by_category(Product_Categories.CLOTHING)
print(products[0].get_title())
sellers = flip.get_sellers()
print(sellers.keys())

