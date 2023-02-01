class FoodKiosk:
    def __init__(self):
        print("             ------------------------------------            ")
        print("             |    WELCOME TO ASKIA CAFETERIA     |           ")
        print("             ------------------------------------")
        self.menu = {1: ("Hamburger", 59), 2: ("Fries", 39), 3: ("Soft Drink", 29), 4: ("Cheeseburger", 79), 5: ("Hotdog", 25), 6: ("Cheesy Hotdog", 59)}
        self.orders = []

    def view_menu(self):
        print("------------------------------------")
        for item, (name, price) in self.menu.items():
            print(f'{item}. {name} - ₱{price}')
        print("------------------------------------")

    def place_order(self):
        order = []
        while True:
            item = input("Enter an item number to order or 'q' to finish: ")
            print("------------------------------------")
            if item == 'q':
                break
            if item.isdigit() and int(item) in self.menu:
                order.append(self.menu[int(item)][0])
                print(f'{self.menu[int(item)][0]} added to order')
                print("------------------------------------")
            else:
                print(f'{item} is not a valid menu item')
        self.orders.append(order)
        print("Order placed successfully")

    def summarize_orders(self):
        order_summary = {}
        print("------------------------------------")
        for order in self.orders:
            for item in order:
                if item in order_summary:
                    order_summary[item] += 1
                else:
                    order_summary[item] = 1
        for item, count in order_summary.items():
            print(f'{item}: {count}')
            print("------------------------------------")

    def check_out(self):
        total = 0
        print("------------------------------------")
        for order in self.orders:
            for item in order:
                total += [price for num, (name, price) in self.menu.items() if name == item][0]
        print(f'Total: ₱{total}')
        print("------------------------------------")

    def main_menu(self):
        while True:
            choice = input(
"""
What would you like to do?
1. View Menu
2. Place an order
3. View order summary
4. Check out
5. Exit
Enter your choice: 
""")
            if choice == "1":
                self.view_menu()
            elif choice == "2":
                self.place_order()
            elif choice == "3":
                self.summarize_orders()
            elif choice == "4":
                self.check_out()
            elif choice == "5":
                print("--------------------------------------------")
                print("| THANK YOU! YOUR ORDER IS BEING PROCESSED |")
                print("--------------------------------------------")
                exit()
            else:
                print("Invalid choice, please try again")
# create an instance of the FoodKiosk class
kiosk = FoodKiosk()

# run the main menu
kiosk.main_menu()
