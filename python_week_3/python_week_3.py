# pie_one = { 'name' : 'Apple', 'topping': 'ice cream', 'season_availability' : 'fall'}
# pie_two = { 'name' : 'Pecan Pie', 'topping': 'whipped cream', 'season_availability' : 'all'}
# pie_three = { 'name' : 'Pumpkin Pie', 'topping': 'whipped cream and ice cream', 'seasonavailability' : 'fall'}


# Create a blueprint
class Pie:
    def __init__(self, name, topping, season = "All"):
        # Attribute
        self.name = name
        self.topping = topping
        self.season = season

    # Methods
    def sub_topping(self, topping):
        self.topping = topping
        return self

    def no_topping(self):
        self.topping = None
        return self

    def change_of_season(self, season):
        self.season = season
        return self

pie_one = Pie("Apple Pie", "Ice Cream")
# pie_one.sub_topping("Chocolate Chip Cookie")
# pie_one.no_topping()
# print(pie_one.topping)
# pie_one.change_of_season('winter')
# print(pie_one.season)

# pie_two = Pie("Blueberry", "Chocolate Syrup", "All")
# print(pie_two.name)

# pie_three = Pie("Cherry Pie", "Powdered Sugar")
# print(pie_three.season)

print(pie_one.name, pie_one.topping, pie_one.season)
pie_one.change_of_season("winter").sub_topping("Chocolate Chip")
print(pie_one.season, pie_one.topping)
