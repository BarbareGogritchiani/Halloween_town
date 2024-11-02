from city import *
from costumeShop import *
from customer import *

# city
city = City("Halloween Town", 5000)

# shops and their costumes
shop1 = CostumeShop("halloween costumes")
shop1.add_costume("Zombie", 50, 20)
shop1.add_costume("Vampire", 30, 25)
shop1.add_costume("Ghost", 40, 15)

shop2 = CostumeShop("costumes for gamers")
shop2.add_costume("Sherrif", 60, 22)
shop2.add_costume("Assasin", 20, 30)
shop2.add_costume("John Martson", 35, 18)

shop3 = CostumeShop("disneyween")
shop3.add_costume("Cruella de Vil", 50, 20)
shop3.add_costume("Mulan", 30, 30)
shop3.add_costume("Sullivan", 25, 35)

city.add_shop(shop1)
city.add_shop(shop2)
city.add_shop(shop3)

# simulation
# city.simulate_demand()
# city.report()


shop3.adjust_price("Sulliva",40) #in this case price won't be changed
shop1.adjust_price("Zombie",40) #price will be changed

shop1.adjust_stock("Sherrif",75) # isn't in shop1
shop2.adjust_stock("Sherrif",75) #stock will be 75 instead of 60

city.simulate_demand()
# city.report()

#users
customer1 = Customer("barbare", 100)
customer2 = Customer("nino", 500)
customer3 = Customer("luka",400)

#wishlist
customer1.add_to_shopping_list("Zombie")
customer1.add_to_shopping_list("Ghost")


customer2.add_to_shopping_list("Sherrif")
customer2.add_to_shopping_list("Vampire")
customer2.add_to_shopping_list("Ghost")

customer3.add_to_shopping_list("Sullivan")
customer3.add_to_shopping_list("Ghost")

#buying
customer1.buy_costume(shop1, "Zombie", 2)
customer2.buy_costume(shop2, "John Martson", 1)
customer2.buy_costume(shop2,"Sherrif",1)
customer3.buy_costume(shop2, "Cruella de Vil", 1) #this costume isn't in this shop
customer3.buy_costume(shop3, "Cruella de Vil", 1)


#report for each customer
customer1.shop_report()
customer2.shop_report()
customer3.shop_report()


#checking polymorphism
city.report()
customer1.report()
shop1.report()

