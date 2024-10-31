class CostumeShop:
    def __init__(self, name):
        self.name = name
        self.costumes = {}
        self.prices = {}
        self.demand = {}

    def add_costume(self, costume_name, stock, price):
        self.costumes[costume_name] = stock
        self.prices[costume_name] = price
        self.demand[costume_name] = 0

#changing prices
    def adjust_price(self, costume_name, new_price):
        try:
            if costume_name in self.prices:
                self.prices[costume_name] = new_price
            else:
                print(f"{costume_name} not found in {self.name}. Cannot adjust price.")
        except Exception as e:
            print(f"Error adjusting price for {costume_name} in {self.name}: {e}")

#changing stocks
    def adjust_stock(self, costume_name, new_stock):
        try:
            if costume_name in self.costumes:
                self.costumes[costume_name] = new_stock
            else:
                print(f"{costume_name} not found in {self.name}. Cannot adjust stock.")
        except Exception as e:
            print(f"Error adjusting stock for {costume_name} in {self.name}: {e}")
#changing demand
    def adjust_demand(self, costume_name, population):
        try:
            if costume_name in self.demand:
                self.demand[costume_name] += population // 100  #for the real demand
            else:
                print(f"{costume_name} not found in {self.name}. Cannot adjust demand.")
        except Exception as e:
            print(f"Error adjusting demand for {costume_name} in {self.name}: {e}")

    def sell_costume(self, costume_name, quantity):
        if costume_name in self.costumes and self.costumes[costume_name] >= quantity: #for example i bought 4 costumes , quantity is 4 , if stock is >= 4 shop can sell it
            self.costumes[costume_name] -= quantity
            self.demand[costume_name] += quantity * 1.1  #then increase demand on this costume with 10%
        else:
            print(f"Insufficient stock for {costume_name} in {self.name}.")

    def report_stock(self):
        print(f"Stock report for {self.name}:")
        for costume, stock in self.costumes.items():
            price = self.prices[costume]
            demand = self.demand[costume]
            print(f"  {costume}: {stock} in stock, Price: {price}, Demand: {demand}")
