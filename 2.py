import json
from xml.etree import ElementTree



class OverpriceException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoProfitException(Exception):
    def __init__(self, message):
        super().__init__(message)



class Item:
    def __init__(self, expense: int, profit: int):
        if expense <= 1200:
            self.__expense = expense
        else:
            raise OverpriceException("Item in menu must be affordable!")
        
        if profit >= 20:
            self.__profit = profit
        else:
            raise NoProfitException("Item in menu must give profit!")
    
    def set_expense(self, expense):
        if expense <= 1200:
            self.__expense = expense
        else:
            raise OverpriceException("Item in menu must be affordable!")
    
    def set_profit(self, profit):
        if profit >= 20:
            self.__profit = profit
        else:
            raise NoProfitException("Item in menu must give profit!")
        
    def get_expense(self):
        return self.__expense

    def get_profit(self):
        return self.__profit



class NoItemsException(Exception):
    def __init__(self, message):
        super().__init__(message)



class Dish(Item):
    def __init__(self, name: str, expense, profit, amount: int, ):
        Item.__init__(self, expense, profit)
        
        self.name = name
        if amount > 0:
            self.amount = amount
        else:
            raise NoItemsException("No dishes left!")
        
    def to_dict(self):
        dish_dict = {
            "name": self.name,
            "expense": self.get_expense(),
            "profit": self.get_profit(),
            "amount": self.amount,
        }
        return dish_dict
    
    def set_name(self, name):
        self.name = name

    def set_amount(self, amount):
        if amount > 0:
            self.amount = amount
        else:
            raise NoItemsException("No dishes left!")

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.profit


    def experiment(self):
        print(self.get_name() + " is changing, expect rude customers...")

    def to_xml(self):
        Dish_element = ElementTree.Element("Dish")

        name_element = ElementTree.Element("name")
        name_element.text = self.name
        Dish_element.append(name_element)

        expense_element = ElementTree.Element("expense")
        expense_element.text = str(self.get_expense())
        Dish_element.append(expense_element)

        profit_element = ElementTree.Element("profit")
        profit_element.text = str(self.get_profit())
        Dish_element.append(profit_element)

        amount_element = ElementTree.Element("amount")
        amount_element.text = self.amount
        Dish_element.append(amount_element)

        xml_tree = ElementTree.ElementTree(Dish_element)
        return ElementTree.tostring(xml_tree.getroot(), encoding="utf-8", method="xml", xml_declaration=True)



class Drink(Item):
    def __init__(self, name: str, expense, profit, amount: int):
        Item.__init__(self, expense, profit)
        
        self.name = name
        if amount > 0:
            self.amount = amount
        else:
            raise NoItemsException("No drinks left!")
    
    def to_dict(self):
        drink_dict = {
            "name": self.name,
            "expense": self.get_expense(),
            "profit": self.get_profit(),
            "amount": self.amount,
        }
        return drink_dict
    
    def set_name(self, name):
        self.name = name

    def set_amount(self, amount):
        if amount > 0:
            self.amount = amount
        else:
            raise NoItemsException("No drinks left!")

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.profit

    def progress(self):
        print("Witches are making your drink... spooky Helloween... BOO!")

    def to_xml(self):
        Drink_element = ElementTree.Element("Drink")

        name_element = ElementTree.Element("name")
        name_element.text = self.name
        Drink_element.append(name_element)

        expense_element = ElementTree.Element("expense")
        expense_element.text = str(self.get_expense())
        Drink_element.append(expense_element)

        profit_element = ElementTree.Element("profit")
        profit_element.text = str(self.get_profit())
        Drink_element.append(profit_element)

        amount_element = ElementTree.Element("amount")
        amount_element.text = self.amount
        Drink_element.append(amount_element)

        xml_tree = ElementTree.ElementTree(Drink_element)
        return ElementTree.tostring(xml_tree.getroot(), encoding="utf-8", method="xml", xml_declaration=True)



class TooManyPositionsException(Exception):
    def __init__(self, message):
        super().__init__(message)



class Menu:
    def __init__(self, menu_place: int, menu_name: str):
        self.menu_place = menu_place
        self.menu_name = menu_name
        self.dishes = []  
        self.drinks = []  

    def add_dish(self, Dish):
        if len(self.dishes) <= 50:
            self.dishes.append(Dish)
        else:
            raise TooManyPositionsException('Menu can not be overcrowded with potatoes!')

    def add_drink(self, Drink):
        if len(self.drinks) <= 20:
            self.drinks.append(Drink)
        else:
            raise TooManyPositionsException('Twats do not need to drink that much buddy!')

    def to_dict(self):
        menu_dict = {
            "menu_place": self.menu_place,
            "menu_name": self.menu_name,
            "dishes": [Dish.to_dict() for Dish in self.dishes],
            "drinks": [Drink.to_dict() for Drink in self.drinks]
        }
        return menu_dict



    @classmethod
    def from_json(cls, json_data):

        menu_dict = json.loads(json_data)
        menu_place = menu_dict["menu_place"]
        menu_name = menu_dict["menu_name"]

        menu_json = cls (menu_place, menu_name)

        dishes_data = menu_dict.get("dishes", [])
        for dish_data in dishes_data:
            dish = Dish(
                name=dish_data["name"],
                expense=dish_data["expense"],
                profit=dish_data["profit"],
                amount=dish_data["amount"]
            )
            menu_json.add_dish(dish)
        
        drinks_data = menu_dict.get("dishes", [])
        for drink_data in drinks_data:
            drink = Drink(
                name=drink_data["name"],
                expense=drink_data["expense"],
                profit=drink_data["profit"],
                amount=drink_data["amount"]
            )
            menu_json.add_drink(drink)

        return menu_json

    def to_xml(self):

        menu_element = ElementTree.Element("Menu")

        menu_element.set("menu_place", str(self.menu_place))
        menu_element.set("menu_name", self.menu_name)

        if self.dishes:
            dishes_element = ElementTree.Element("dishes")
            for dish in self.dishes:
                dish_element = ElementTree.Element("dish")
                dish_element.set("name", dish.name)
                dish_element.set("expense", str(dish.get_expense()))
                dish_element.set("profit", str(dish.get_profit()))
                dish_element.set("amount", str(dish.amount))
                dishes_element.append(dish_element)
            menu_element.append(dish_element)

        if self.drinks:
            drinks_element = ElementTree.Element("drinks")
            for drink in self.drinks:
                drink_element = ElementTree.Element("drink")
                drink_element.set("name", drink.name)
                drink_element.set("expense", str(drink.get_expense()))
                drink_element.set("profit", str(drink.get_profit()))
                drink_element.set("amount", str(drink.amount))
                drinks_element.append(drink_element)
            menu_element.append(drink_element)

        xml_tree = ElementTree.ElementTree(menu_element)

        return ElementTree.tostring(xml_tree.getroot(), encoding="utf-8", method="xml")



    @classmethod
    def from_xml(cls, xml_data):

        xml_tree = ElementTree.ElementTree(ElementTree.fromstring(xml_data))
        menu_element = xml_tree.getroot()

        menu_place = int(menu_element.get("menu_place"))
        menu_name = menu_element.get("menu_name")

        menu_xml = cls(menu_place, menu_name)

        dishes_element = menu_element.find("dishes")
        if dishes_element is not None:
            for dish_element in dishes_element.findall("dish"):
                name = dish_element.get("name")
                expense = int(dish_element.get("expense"))
                profit = int(dish_element.get("profit"))
                amount = int(dish_element.get("amount"))
                dish = Dish(name, expense, profit, amount)
                menu_xml.dishes.append(dish)
        
        drinks_element = menu_element.find("drinks")
        if drinks_element is not None:
            for drink_element in drinks_element.findall("drink"):
                name = drink_element.get("name")
                expense = int(drink_element.get("expense"))
                profit = int(drink_element.get("profit"))
                amount = int(drink_element.get("amount"))
                drink = Drink(name, expense, profit, amount)
                menu_xml.drinks.append(drink)

        return menu_xml






# Zapolnim paru objectov

dish1 = Dish(name="Neverland", expense=1000, profit=100, amount=10)
dish2 = Dish(name="Trag", expense=430, profit=40, amount=5)
drink1 = Drink(name="Glup", expense=200, profit=100, amount=30)

menu = Menu(menu_place=1, menu_name="Stearter")

menu.add_dish(dish1)
menu.add_dish(dish2)
menu.add_drink(drink1)

dish1.experiment()
drink1.progress()

print(f"{dish1.get_name()} costs {dish1.get_expense()} and will profit us for {dish1.get_profit()}.")
print(f"{dish2.get_name()} costs {dish2.get_expense()} and will profit us for {dish2.get_profit()}.")
print(f"{drink1.get_name()} costs {drink1.get_expense()} and probably have margin like 95% ( it is basically a fraud ).")

# Obrabativaem exceptions

for i in range(0, 100):
    try:
        menu.add_drink(Drink(name="Opiat' eta martini", expense=1000, profit=1000, amount=2))
    except TooManyPositionsException:
        print("Exception poimana")
        break

# Obrabativaem ewe exception

try:
    print(menu.dishes[51])
except IndexError:
    print("IndexError poimana")





# Serijalizuem i zapisivaem v fail, potom deserializuem v object iz faila (json)

menu_json = menu.to_dict()

with open('menu_to_json.json', 'w') as json_file:
    json.dump(menu_json, json_file, indent=4)

try:
    with open('menu_from_json.json', 'r') as json_file:
        json_data = json_file.read()
        menu_from_json = Menu.from_json(json_data)
except FileNotFoundError:
    print("File is not found")

# Serijalizuem i zapisivaem v fail, potom deserializuem v object iz faila (xml)

menu_xml = menu.to_xml()

with open('menu_to_xml.xml', 'wb') as xml_file:
    xml_file.write(menu_xml)

try:
    with open('menu_from_xml.xml', 'r') as xml_file:
        xml_data = xml_file.read()
        menu_from_xml = Menu.from_xml(xml_data)
except FileNotFoundError:
    print("File is not found")
