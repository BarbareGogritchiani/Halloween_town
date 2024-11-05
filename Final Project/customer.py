class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.shopping_list = []
        self.purchased_items = []  # list of purchased items


    def add_to_shopping_list(self, costume_name):
        self.shopping_list.append(costume_name)

    def buy_costume(self, shop, costume_name, quantity=1):
        try:
            if costume_name in shop.costumes and shop.costumes[costume_name] >= quantity:
                total_cost = shop.prices[costume_name] * quantity
                if self.check_budget(total_cost):
                    shop.sell_costume(costume_name, quantity)
                    self.purchased_items.append((costume_name, quantity))
                    self.budget -= total_cost
                    print(f"{self.name} bought {quantity} {costume_name}(s) for {total_cost} from {shop.name}.")
                else:
                    print(f"{self.name} does not have enough budget for {costume_name}.")
            else:
                print(f"{costume_name} is not available in {shop.name}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_budget(self, costume_price):
        return self.budget >= costume_price

    def shop_report(self):
        print(f"{self.name}'s shopping report:")
        print(f"Remaining budget: {self.budget}")
        print("Shopping list:", ", ".join(self.shopping_list))

#for polymorphism
    def report(self):
        print(f"Customer Report: {self.name}")
        print(f"Budget: ${round(self.budget,2)}")
        print(f"Shopping List: {', '.join(self.shopping_list)}")

    def save_data_to_file(self, filename):

        try:
            # open the file in append mode to add data for each customer
            with open("customer_data.txt", "a") as file:
                file.write(f"Customer: {self.name}\n")
                file.write(f"Remaining Budget: ${self.budget}\n")
                file.write("Purchased Items:\n")
                for item, quantity in self.purchased_items:
                    file.write(f"- {item} x {quantity}\n")
                file.write("\n")
            print(f"{self.name}'s data saved to {filename}")
        except Exception as e:
            print(f"Error writing data to file: {e}")