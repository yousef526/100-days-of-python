MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources_var = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

COINS = {
    'quarters':0.25,
    'dimes':0.1,
    'nickles':0.05,
    'pennies':0.01
}

#print(MENU["cappuccino"])
# TODO 1. WRITE report function 
def report_function(resources,money):
    for resoure in resources:
        if resoure != 'coffee':
            print(f"{resoure}: {resources[resoure]}ml")
        else:
            print(f"{resoure}: {resources[resoure]}g")
    print(f"Money: ${money['value']}")




# TODO 2. write function to check resourses
def check_resources(order,resources):
    resource_with_problem = []
    for resource in MENU[order]['ingredients']:
        if resources[resource] < MENU[order]['ingredients'][resource]:
            resource_with_problem.append(resource)
    return resource_with_problem

# TODO 3. write function that take order and calculate
def take_order(quarters,dimes,nickles,pennies,order,resources,money):
    quarters = round(quarters * COINS["quarters"],2)
    dimes = round(dimes * COINS["dimes"],2)
    nickles = round(nickles * COINS["nickles"],2)
    pennies = round(pennies * COINS["pennies"],2)
    total_sum = round(quarters + dimes + nickles + pennies,2)
    if total_sum >= MENU[order]['cost']:
        for resource in MENU[order]['ingredients']:
            resources[resource] = resources[resource] - MENU[order]['ingredients'][resource]
        money['value']+=MENU[order]['cost']
        print(f"Here is ${round(total_sum - MENU[order]['cost'],2)} dollars in change.")
        print(f"Here is your {order} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

# TODO 4.close the program and end
def turn_off(close):
    if close.lower() == 'off':
        return True

while True:
    order_var = input("What would you like? (espresso/latte/cappuccino): ")
    if turn_off(order_var):
        break
    elif order_var.lower() == 'report':
        report_function(resources=resources_var,money=money)
        continue
    var = check_resources(order=order_var,resources=resources_var)
    if var == []:
        print("Please insert coins.")
        quarters_var = int(input("how many quarters?: "))
        dimes_var = int(input("how many dimes?: "))
        nickles_var = int(input("how many nickles?: "))
        pennies_var = int(input("how many pennies?: "))
        take_order(quarters=quarters_var,dimes=dimes_var,nickles=nickles_var,pennies=pennies_var,order=order_var,resources=resources_var,money=money)
    else:
        for x in var:
            print(f'Sorry there is not enough {x}.')
        continue
