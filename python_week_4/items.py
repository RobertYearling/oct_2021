from dessert import Dessert

class Pie(Dessert):
    def __init__(self, name, ingredients, season, quantity):
        super().__init__(name, ingredients, season, quantity)

    def topping(self):
        return 'Whipped Cream'


class Pastry(Dessert):
    def __init__(self, name, ingredients, season, quantity):
        super().__init__(name, ingredients, season, quantity)

    def topping(self):
        return 'Chocolate Syrup'

class Cupcake(Dessert):
    def __init__(self, name, ingredients, season, quantity):
        super().__init__(name, ingredients, season, quantity)

    def topping(self):
        return "Butter Cream"

# Object or Instance
pie_one = Pie("Apple Pie", "Apples", "All", 1)
pastry_one = Pastry("Chocolate Pastry", "Chocolate", "Fall/Winter", 6)
cupcake = Cupcake("Chocolate Chip", "Chocolate", "All", 40)

print(pie_one.name)
print(pastry_one.name)
print(cupcake.name)