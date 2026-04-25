class Laptop:
    storage_type="SSD"
    def __init__(self , RAM ,storage):
        self.RAM=RAM
        self.storage=storage

    def get_info(self): #instance methods
        print(f"Laptop has {self.RAM} RAM & {self.storage} storage")
    
    @staticmethod
    def calc_discount(price, discount):
        final_price = price-(discount*price/100)
        print(f"discounted price is {final_price}")
l1=Laptop("16gb","512gb")
l2=Laptop("8gb","256gb")

l1.get_info()
l1.calc_discount(40_000, 10)
