class MenuItems:
    def __init__(self,name,price,category,size="---------"):
        self.name = name 
        self.size = size
        self.price = price
        self.category = category
    def __str__(self):
        return f"{self.category:15}-{self.name:<20}-{self.size:<8}- {self.price:.2f}"

    
menu = []


small_pizza = {
    "Supreme Pizza": 630,
    "Fajita Pizza": 580,
    "Tikka Pizza": 580,
    "Peri Peri Pizza": 580,
    "Special Pizza": 630
}

medium_pizza = {
    "Supreme Pizza": 1290,
    "Fajita Pizza": 1190,
    "Tikka Pizza": 1190,
    "Peri Peri Pizza": 1190,
    "Special Pizza": 1290,
    "Chunky Munky Pizza": 1480,
    "Malai Boti Pizza": 1480,
    "Behari Pizza": 1480,
    "Kabab Stuffer Pizza": 1570,
    "Cheese Stuffer Pizza": 1570,
    "Royal Crust Medium Pizza": 1510
}

large_pizza = {
    "Supreme Pizza": 1890,
    "Fajita Pizza": 1670,
    "Tikka Pizza": 1670,
    "Peri Peri Pizza": 1670,
    "Special Pizza": 1890,
    "Chunky Munky Pizza": 2060,
    "Malai Boti Pizza": 2060,
    "Behari Pizza": 2060,
    "Kabab Stuffer Pizza": 2250,
    "Cheese Stuffer Pizza": 2250,
    "Royal Crust Medium Pizza": 2090
}

pizza_menu = {
    "Small": small_pizza,
    "Medium": medium_pizza,
    "Large": large_pizza
}

burgers_and_rolls = {
    "Wrapster": 480,
    "Pizza Sandwich": 760,
    "Behari Roll": 680,
    "Zingo Burger": 500,
    "Patty Burger": 330,
    "Spin Roll": 650,
    "Chilli Milli Roll": 680
}

wings_and_nuggets = {
    "Nuggets": 540,
    "Chicken Strips": 650,
    "Crispy Wings": 650,
    "Peri Peri Wings": 650,
    "BBQ Wings": 650,
    "Honey Wings": 680
}

fried_potatoes = {
    "Large Fries": 460,
    "BBQ Fries": 620,
    "Potamatoes Fries": 620,
    "Cheesy Mayo Fries": 540,
    "Small Fries": 290
}

oven_baked_pasta = {
    "Creamy Pasta": 770,
    "Flaming Pasta": 790,
    "Alfredo Pasta": 880
}

beverages = {
    "Mineral Water Small": 70,
    "Tin Pack": 110,
    "1500 ml Cold Drink": 220,
    "500 ml Cold Drink": 120
}

other_menu = {
    "Burgers and Rolls": burgers_and_rolls,
    "Wings and Nuggets": wings_and_nuggets,
    "Fried Potatoes": fried_potatoes,
    "Oven Baked Pasta": oven_baked_pasta,
    "Beverages": beverages
}

def show_menu():
    n = 1
    for category, items_dict in other_menu.items():
        # print(f"=== {category} ===".center(45))
        for name, price in items_dict.items():
            item = MenuItems(name, price,category)
            menu.append(item)
            # print(f"{n:<3} - {item}")
            n += 1
    
    for size, items_dict in pizza_menu.items():
        # print(f"=== {size} Pizzas ===".center(45))
        for name, price in items_dict.items():
            item = MenuItems(name, price,"Pizza", size)
            menu.append(item)
            # print(f"{n:<3} - {item}")
            n += 1
show_menu()

def final_show_menu():
    for n,i in enumerate(menu,start=1): print(f"{n}-{i}")
