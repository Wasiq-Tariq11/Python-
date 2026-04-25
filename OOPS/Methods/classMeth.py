class Laptop:
    storage_type="SSD"
    def __init__(self , RAM ,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod
    def get_storage(cls):
        print(f"storage type is {cls.storage_type}")

    
 
    def get_info(self): #instance methods
        print(f"Laptop has {self.RAM} RAM & {self.storage} storage")

l1=Laptop("16gb","512gb")
l2=Laptop("8gb","256gb")

l1.get_info()
l1.get_storage()


