import random

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.costume_shops = [] #list to append shops

    def add_shop(self, shop):
        self.costume_shops.append(shop) #when we enter the name of the shop it appends in list

    def simulate_demand(self):
        for shop in self.costume_shops: #for each shop
            for costume in shop.costumes: #for each costume in shop
                demand_percentage = random.uniform(0.1, 1.0)  # random demand percentage
                shop.adjust_demand(costume, int(self.population * demand_percentage))
                print(costume , round(demand_percentage,2)) #prints costume and its demand

    def report(self):
        print(f"Report for {self.name}:")
        for shop in self.costume_shops:
            shop.report_stock() #method from costumeshop class
