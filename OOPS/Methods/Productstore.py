class Product:
    count=0
    def __init__(self, name,price):
        self.name= name
        self.price=price
        Product.count += 1

    
    def get_info(self):#instance
        print(f"the price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"the total products stored are{cls.count}")
    
    
    @staticmethod
    def get_discount(price,discount):
       discounted_price=(price*discount/10)
       print(f"Price after discount is {discounted_price}")
    
    
p1=Product("phone",15_000)
p2=Product("Laptop",50_000)
p1.get_info()
p1.get_discount(10_000,10)



    