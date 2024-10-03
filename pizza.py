print("-------------------- WELCOME TO NGUAWOR PIZZA --------------------\n")

while True:
    name = input("Please enter your name: ")

    print("List Menu Pizza:")
    print("""
    Triple Cheese        - Rp 45.000 (Personal), Rp 85.000 (Medium), Rp 125.000 (Large)
    Meaty Overload       - Rp 60.000 (Personal), Rp 95.000 (Medium), Rp 140.000 (Large)
    Gourmet Fusion       - Rp 55.000 (Personal), Rp 90.000 (Medium), Rp 135.000 (Large)
    Spicy Inferno        - Rp 50.000 (Personal), Rp 85.000 (Medium), Rp 120.000 (Large)
    Veggie Delight       - Rp 40.000 (Personal), Rp 70.000 (Medium), Rp 110.000 (Large)
    Seafood Sensation    - Rp 65.000 (Personal), Rp 100.000 (Medium), Rp 145.000 (Large)
    BBQ Bliss            - Rp 55.000 (Personal), Rp 90.000 (Medium), Rp 130.000 (Large)
    Truffle Temptation   - Rp 75.000 (Personal), Rp 115.000 (Medium), Rp 160.000 (Large)
    """)

    pizza_name = ""
    crust_pizza = ""
    size_pizza = ""
    extra_cheese = ""
    total_bill = 0
    payment_method = ""

    pizza_prices = {
        "Triple Cheese": {"Personal": 45000, "Medium": 85000, "Large": 125000},
        "Meaty Overload": {"Personal": 60000, "Medium": 95000, "Large": 140000},
        "Gourmet Fusion": {"Personal": 55000, "Medium": 90000, "Large": 135000},
        "Spicy Inferno": {"Personal": 50000, "Medium": 85000, "Large": 120000},
        "Veggie Delight": {"Personal": 40000, "Medium": 70000, "Large": 110000},
        "Seafood Sensation": {"Personal": 65000, "Medium": 100000, "Large": 145000},
        "BBQ Bliss": {"Personal": 55000, "Medium": 90000, "Large": 130000},
        "Truffle Temptation": {"Personal": 75000, "Medium": 115000, "Large": 160000},
    }

    while True:
        choice_pizza = input("Enter the pizza you want (e.g., Triple Cheese, Meaty Overload): ").strip().lower()
        
        pizza_names = [pizza.lower() for pizza in pizza_prices.keys()]
        match = next((pizza for pizza in pizza_names if choice_pizza in pizza), None)

        if match:
            pizza_name = [pizza for pizza in pizza_prices.keys() if pizza.lower() == match][0]
            break
        else:
            print("Your pizza choice is not available. Please enter a valid name.")

    print("""
    \nChoice Crust:
    Regular Crust          - Rp 0
    Cheese Stuffed Crust   - Rp 16.000
    Sausage Stuffed Crust  - Rp 20.000
    """)

    crust_prices = {
        "Regular Crust": 0,
        "Cheese Stuffed Crust": 16000,
        "Sausage Stuffed Crust": 20000
    }

    while True:
        choice_crust = input("Enter the crust you want (Regular Crust, Cheese Stuffed Crust, Sausage Stuffed Crust): ").strip().lower()

        crust_names = [crust.lower() for crust in crust_prices.keys()]
        match = next((crust for crust in crust_names if choice_crust in crust), None)

        if match:
            crust_pizza = [crust for crust in crust_prices.keys() if crust.lower() == match][0]
            total_bill += crust_prices[crust_pizza]
            break
        else:
            print("Your crust choice is not available. Please enter a valid name.")

    print("""
    \nChoice Size:
    Personal
    Medium
    Large
    """)

    while True:
        choice_size = input("Enter the size you want (Personal, Medium, Large): ").strip().lower()

        size_options = [size.lower() for size in pizza_prices[pizza_name].keys()]
        match_size = next((size for size in size_options if choice_size in size), None)

        if match_size:
            total_bill += pizza_prices[pizza_name][match_size.capitalize()]
            size_pizza = f"{match_size.capitalize()} (Rp {pizza_prices[pizza_name][match_size.capitalize()]:,.0f})"
            break
        else:
            print("Your size choice is not available. Please enter a valid size.")

    while True:
        extra_cheese = input("\nWould you like extra cheese for Rp 13.000? (yes/no): ").strip().lower()

        if extra_cheese == "yes":
            total_bill += 13000
            extra_cheese = "Yes (Rp 13.000)"
            break
        elif extra_cheese == "no":
            extra_cheese = "No (Rp 0)"
            break
        else:
            print("Your choice is not available. Please enter 'yes' or 'no'.")

    print("\n\n-------------------- ORDER SUMMARY --------------------")
    print(f"Name          : {name}")
    print(f"Pizza         : {pizza_name}")
    print(f"Crust         : {crust_pizza}")
    print(f"Size          : {size_pizza}")
    print(f"Extra Cheese  : {extra_cheese}")
    print(f"Total Bill    : Rp {total_bill:,.0f}")

    choice = input("Is your order correct? (yes/no): ").strip().lower()

    if choice == "yes":
        break
    elif choice == "no":
        print("\nPlease make your order again.\n")
        continue
    else:
        print("Your choice is not available. Please enter 'yes' or 'no'.")

print("\nThank you for your order!\n")