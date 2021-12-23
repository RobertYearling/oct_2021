class Dessert:
    store_name = "Robs Pie Shop"
    def __init__(self, name, ingredients, season, quantity):
        # Attribute
        self.name = name
        self.ingreditents = ingredients
        self.season = season
        self.quantity = quantity

    def topping(self):
        return self

    def add_side(self, side):
        self.side = side
        return self

    def amount(self):
        if self.quantity < 6:
            return 'No Box'
        elif self.quantity < 36:
            return 'Needs Boxes'
        else:
            return 'Needs Carton'

    @classmethod
    def name_change(cls, name):
        cls.store_name = name

    # @staticmethod



# pie_two = Pie("Blueberry", "Chocolate Syrup", "All")

