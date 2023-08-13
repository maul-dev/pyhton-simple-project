from helper import try_covert_int


class CoffeMaker:
    def __init__(self):
        self.resources = {
                "water": 100,
                "milk": 100,
                "coffee": 100,
        }

    def add_resources(self):
        """Add resources if user type in 'admin-add-resources'"""
        amount_water_str = input("How much water?: ")
        amount_water = try_covert_int(amount_water_str)
        amount_milk_str = input("How much milk?: ")
        amount_milk = try_covert_int(amount_milk_str)
        amount_milk_str = input("How much coffee?: ")
        amount_coffee = try_covert_int(amount_milk_str)
        self.resources["water"] += amount_water
        self.resources["milk"] += amount_milk
        self.resources["coffee"] += amount_coffee

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")