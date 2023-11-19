from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def turn_off(close):
    if close.lower() == 'off':
        return True
money = MoneyMachine()
coffee = CoffeeMaker()
menu_in_order = Menu()

while True:
    order_var = input(f"What would you like? {menu_in_order.get_items()} ")
    if turn_off(order_var):
        break

    elif order_var.lower() == 'report':
        coffee.report()
        money.report()
        continue
    
    drink = menu_in_order.find_drink(order_var)
    resources_check = coffee.is_resource_sufficient(drink)
    if resources_check:
        if money.make_payment(drink.cost):
            coffee.make_coffee(drink)
     