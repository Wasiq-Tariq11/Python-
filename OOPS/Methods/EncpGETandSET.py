class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def set_balance(self,new_balance):
        self.__balance=new_balance

    def get_balance(self):
        return self.__balance
    
Acc1=Bank("ABC","10000")
print(Acc1.name)
Acc1.set_balance("5000")
print(Acc1.get_balance())