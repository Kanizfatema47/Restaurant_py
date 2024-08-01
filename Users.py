from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name) -> None:
        self.name = name

class Customer(User):
    def __init__(self, name, money) -> None:
        self.wallet = money
        self.order = None
        super().__init__(name)
        
    @property  #getter
    def order(self):
        return self.__order #private

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f'{self.name} placed an order {order.items}')
    
    def pay_for_order(self, amount):
        #Todo:Submit the money to the manager
        pass
    
    def give_tips(self, tips_amount):
        pass
    
    def write_review(self, stars):
        pass