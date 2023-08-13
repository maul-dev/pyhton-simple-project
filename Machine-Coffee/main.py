from coffee_maker import CoffeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine
coffe_maker = CoffeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    user_input = input(f"What would you like? {menu.get_items()}: ").lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffe_maker.report()
        money_machine.report()
    elif user_input == "admin-add":
        coffe_maker.add_resources()
    else:
        order = menu.find_drinks(user_input)
        if order is not None:
            if coffe_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffe_maker.make_coffee(order)




