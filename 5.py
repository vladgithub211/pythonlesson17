def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

active = True
while active:
    menu = input("Zakaz --> ")
    if menu == "out":break
make_pizza(menu)
make_pizza('mushrooms', 'green peppers', 'extra cheese')
