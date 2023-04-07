#case1-2

class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f'Name - {self.name}, type - {self.type}')

    def open_restaurant(self):
        print('Restaurant is open.')

restourant1 = Restaurant('Temruk', 'pizza')
print(restourant1.name)
print(restourant1.type)
restourant1.describe_restaurant()
restourant1.open_restaurant()

restourant2 = Restaurant('Krasnodar', 'sushi')
restourant2.describe_restaurant()
restourant3 = Restaurant('Krasnodar', 'pizza')
restourant3.describe_restaurant()


