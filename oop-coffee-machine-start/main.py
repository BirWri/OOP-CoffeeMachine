from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True
while machine_on:

    #Print menu and ask input from user
    order = input(f"What would you like? {menu.get_items()}: ")

    #Turn off machine
    if order == "off":
        machine_on = False
    #Print report
    elif order == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        # Verify and Fetch the MenuItem
        drink = menu.find_drink(order)

        #Check resources
        confirmation_of_resources = coffee_maker.is_resource_sufficient(drink)

        if not confirmation_of_resources or drink == "None":
            machine_on = False
        else:
            #Check money
            confirmation_of_payment = money_machine.make_payment(drink.cost)

            if not confirmation_of_payment:
                machine_on = False
            else:
                coffee_maker.make_coffee(drink)
