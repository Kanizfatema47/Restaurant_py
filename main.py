from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Server, Manager
def main():
    menu = Menu()
    
    pizza1 = Pizza('Chicken Pizza', 1100, 'large', ['chicken', 'tomato', 'onion'])
    menu.add_menu_item('pizza', pizza1)
    
    pizza2 = Pizza('Beef Pizza', 1300, 'large', ['Beef', 'tomato', 'onion'])
    menu.add_menu_item('pizza', pizza2)
    
    pizza3 = Pizza('Vegetable Pizza', 900, 'large', ['Vegetable', 'tomato', 'onion'])
    menu.add_menu_item('pizza', pizza3)
    
    
    burger1 = Burger('Chicken Burger', 250, 'chicken', ['tomato', 'letus'])
    menu.add_menu_item('burger', burger1)
    
    burger2 = Burger('beef Burger', 250, 'beef', ['tomato', 'letus'])
    menu.add_menu_item('burger', burger2)
    
    burger3 = Burger('veg Burger', 250, 'veg', ['tomato', 'letus'])
    menu.add_menu_item('burger', burger3)
    
    coke = Drinks('Mojo', 25, True)
    menu.add_menu_item('drinks', coke)
    
    sprite = Drinks('7up', 25, False)
    menu.add_menu_item('drinks', sprite)
    
    mirinda = Drinks('mirinda', 25, True)
    menu.add_menu_item('drinks', mirinda)
    
    coffee = Drinks('Latte', 250, True)
    menu.add_menu_item('drinks', coffee)   
    
    #Show menu
    menu.show_menu()
    
    
    restaurant = Restaurant('KFC', 5000, menu)
     
    manager = Manager('Karim', 12345, 'karim@gmail.com', 'dhaka', 1200, '1 jan 2024', 'core dept' )
    restaurant.add_employee('manager', manager)
    
    chef = Chef('Rahim', 1234, 'karim@gmail.com', 'dhaka', 1100, '2 Feb 2024', 'chef' ,'chicken')
    restaurant.add_employee('chef', chef)
    
    server = Server('Abdul', 1234, 'abdul@gmail.com', 'dhaka', 900, '2 Feb 2024', 'server' )
    restaurant.add_employee('server', server)
     
    #show Employees
    restaurant.show_employees()


#call the main function    
if __name__ == '__main__':
    main()