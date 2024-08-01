from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name,phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name,phone, email, address, money) -> None:
        self.wallet = money
        self.order = None
        super().__init__(name,phone,email,address)
        
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
    
    
class Employee(User):
    def __init__(self, name, phone, email, address, salary,starting_date, department) -> None:
        self.salary = salary
        self.starting_date = starting_date
        self.department = department
        super().__init__(name, phone, email, address)
        
        
class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item) -> None:
        self.cooking_item = cooking_item
        super().__init__(name, phone, email, address, salary, starting_date, department)


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)
        
    def take_order(self, order):
        pass
    
    def transfer_order(self, order):
        pass
    
    def serve_food(self, order):
        pass
    
    def receive_tips(self, amount):
        self.tips_earning += amount
        

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        
        
