from menu import menu, resources
number_of_coffee_choices = ["espresso", "latte", "cappuccino"]
ingredient_name = []
ingredient_bank = []
total_money = 0
last_money = 0
for resource in resources:
    ingredient_bank.append(resources[resource])
    ingredient_name.append(resource)
ingredient_bank_non_espresso = ingredient_bank
ingredient_bank_espresso = [ingredient_bank[0], ingredient_bank[-1]]
last_water = ingredient_bank[0]
last_milk = ingredient_bank[1]
last_bean = ingredient_bank[2]


def ingredient_constructor():
    """This prepares the extracted values for printing out in the menu"""
    water_resource = ingredient_name[0].title(
    ) + ': ' + str(ingredient_bank[0])
    milk_resource = ingredient_name[1].title() + ': ' + str(ingredient_bank[1])
    coffee_resource = ingredient_name[2].title(
    ) + ': ' + str(ingredient_bank[2])
    money_resource = 'Money: $0'
    return f"{water_resource}\n{milk_resource}\n{coffee_resource}\n{money_resource}"


def ingredient_constructor_2(last_water, last_milk, last_bean, total_money):
    """This prepares the extracted values for printing out in the menu"""
    water_resource = ingredient_name[0].title() + ': ' + str(last_water)
    milk_resource = ingredient_name[1].title() + ': ' + str(last_milk)
    coffee_resource = ingredient_name[2].title() + ': ' + str(last_bean)
    money_resource = 'Money: $' + str(total_money)
    return f"{water_resource}\n{milk_resource}\n{coffee_resource}\n{money_resource}"


resources_formatted = ingredient_constructor()


def coffee_matcher(user_coffee_choice):
    """This returns ingredients of the requested coffee"""
    coffee = menu[user_coffee_choice]
    coffee_ingredient = coffee["ingredients"]
    if user_coffee_choice == "espresso":
        coffee_cost = coffee["cost"]
        coffee_water = coffee_ingredient["water"]
        coffee_bean = coffee_ingredient["coffee"]
        return coffee_cost, coffee_water, coffee_bean
    elif user_coffee_choice == "latte" or user_coffee_choice == "cappuccino":
        coffee_cost = coffee["cost"]
        coffee_water = coffee_ingredient["water"]
        coffee_milk = coffee_ingredient["milk"]
        coffee_bean = coffee_ingredient["coffee"]
        return coffee_cost, coffee_water, coffee_milk, coffee_bean


def capacity_checker_espresso(ingredient_bank_espresso, espresso_list):
    """"This returns difference between capacity and requested coffee except espresso"""
    difference = []
    zip_object = zip(ingredient_bank_espresso, espresso_list)
    for item1, item2 in zip_object:
        difference.append(item1 - item2)
        for item in difference:
            if item < 0:
                return False
            else:
                return True


def capacity_checker_not_espresso(ingredient_bank_non_espresso, not_espresso_list):
    """"This returns difference between capacity and requested coffee for espresso"""
    difference = []
    zip_object = zip(ingredient_bank_non_espresso, not_espresso_list)
    for item1, item2 in zip_object:
        difference.append(item1 - item2)
    for item in difference:
        if item < 0:
            return False
        else:
            return True


def which_items_is_lacking_espresso(coffee_water, coffee_bean):
    """Returns lacking item or items as string for espresso"""
    difference = []
    zip_object = zip(ingredient_bank_espresso, espresso_list)
    for item1, item2 in zip_object:
        difference.append(item1 - item2)
    if difference[0] < coffee_water and difference[1] < coffee_bean:
        return "water and bean"
    elif difference[0] < coffee_water:
        return "water"
    elif difference[1] < coffee_bean:
        return "bean"


def which_items_is_lacking_not_espresso(coffee_water, coffee_milk, coffee_bean):
    """Returns lacking item or items as string for non espresso coffeee"""
    difference = []
    zip_object = zip(ingredient_bank, not_espresso_list)
    for item1, item2 in zip_object:
        difference.append(item1 - item2)
    if difference[0] < coffee_water and difference[1] < coffee_milk and difference[2] < coffee_bean:
        return "water, milk and bean"
    elif difference[0] < coffee_water and difference[1] < coffee_milk:
        return "water and milk"
    elif difference[0] < coffee_water and difference[2] < coffee_bean:
        return "water and bean"
    elif difference[1] < coffee_milk and difference[2] < coffee_bean:
        return "milk and bean"
    elif difference[0] < coffee_water:
        return "water"
    elif difference[1] < coffee_milk:
        return "milk"
    elif difference[2] < coffee_bean:
        return "bean"


def coffee_calculator(quarters, dimes, nickles, pennies):
    """This calculates total we have here."""
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total


# TODO 1. Print Coffee
while True:
    user_coffee_choice = input(
        "What would you like? (espresso/latte/cappuccino): ")
    if user_coffee_choice == "report":
        if total_money == 0:
            print(resources_formatted)
        else:
            resources_formatted_2 = ingredient_constructor_2(
                last_water, last_milk, last_bean, total_money)
            print(resources_formatted_2)
    elif user_coffee_choice in number_of_coffee_choices:
        if user_coffee_choice == "espresso":
            coffee_cost, coffee_water, coffee_bean = coffee_matcher(
                user_coffee_choice)
            espresso_list = [coffee_water, coffee_bean]
            if capacity_checker_espresso(ingredient_bank, espresso_list) == True:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                total = coffee_calculator(quarters, dimes, nickles, pennies)
                if total > coffee_cost:
                    change = total - coffee_cost
                    change = round(change, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {user_coffee_choice}. Enjoy!")
                    last_money = coffee_cost
                    total_money += coffee_cost
                    last_water -= coffee_water
                    ingredient_bank_espresso[0] -= coffee_water
                    last_bean -= coffee_bean
                    ingredient_bank_espresso[1] -= coffee_bean
                    last_milk = last_milk
                elif total < coffee_cost:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    print(f"Here is your {user_coffee_choice}. Enjoy!")
                    last_money = coffee_cost
                    total_money += coffee_cost
                    last_water -= coffee_water
                    last_bean -= coffee_bean
                    last_milk = last_milk
            elif capacity_checker_espresso(ingredient_bank, espresso_list) == False:
                lacking_item = which_items_is_lacking_espresso(
                    coffee_water, coffee_bean)
                print(f'Sorry, there is not enough {lacking_item}')
        elif user_coffee_choice == "cappuccino" or user_coffee_choice == "latte":
            coffee_cost, coffee_water, coffee_milk, coffee_bean = coffee_matcher(
                user_coffee_choice)
            not_espresso_list = [coffee_water, coffee_milk, coffee_bean]
            if capacity_checker_not_espresso(ingredient_bank_non_espresso, not_espresso_list) == True:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                total = coffee_calculator(quarters, dimes, nickles, pennies)
                if total > coffee_cost:
                    change = total - coffee_cost
                    change = round(change, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {user_coffee_choice}. Enjoy!")
                    last_money = coffee_cost
                    total_money += last_money
                    last_water -= coffee_water
                    ingredient_bank_non_espresso[0] -= coffee_water
                    last_bean -= coffee_bean
                    ingredient_bank_non_espresso[1] -= coffee_milk
                    last_milk -= last_milk
                    ingredient_bank_non_espresso[2] -= coffee_bean
                elif total < coffee_cost:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    print(f"Here is your {user_coffee_choice}. Enjoy!")
                    last_money = coffee_cost
                    total_money += coffee_cost
                    last_water -= coffee_water
                    last_bean -= coffee_bean
                    last_milk = last_milk
            elif capacity_checker_not_espresso(ingredient_bank_non_espresso, not_espresso_list) == False:
                lacking_item = which_items_is_lacking_not_espresso(
                    coffee_water, coffee_milk, coffee_bean)
                print(f'Sorry, there is not enough {lacking_item}')
