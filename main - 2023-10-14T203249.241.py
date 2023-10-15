class Character:
    def __init__(self):
        self.name = "Player"
        self.gold = 100
        self.inventory = {"Sword": 0, "Shield": 0, "Potion": 0}

    def display_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

    def display_finances(self):
        print(f"{self.name}'s Finances:")
        print(f"Gold: {self.gold}")

    def buy_item(self, item, price):
        if self.gold >= price:
            self.gold -= price
            self.inventory[item] += 1
            print(f"{self.name} bought a {item}.")
        else:
            print(f"{self.name} doesn't have enough gold to buy a {item}.")

    def start_game(self):
        print("Welcome to the RPG-Bookkeeper Game!")
        while True:
            print("\nOptions:")
            print("1. Display Inventory")
            print("2. Display Finances")
            print("3. Buy Item")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_inventory()
            elif choice == "2":
                self.display_finances()
            elif choice == "3":
                item_to_buy = input("Enter the item you want to buy (Sword, Shield, Potion): ")
                if item_to_buy in self.inventory:
                    price = 10  # Price of each item
                    self.buy_item(item_to_buy, price)
                else:
                    print("Invalid item.")
            elif choice == "4":
                print("Thanks for playing RPG-Bookkeeper. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    player = Character()
    player.start_game()
