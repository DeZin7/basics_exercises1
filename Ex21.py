class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self, restaurant_name, cuisine_type):
        print(f'{restaurant_name} é o nome do restaurante')
        print(f'{cuisine_type} é o tipo de cozinha')

    def open_restaurant(self):
        print('o restaurante está aberto!')


restaurante = Restaurant('Faustino', 'regional')
# print(f'o nome do restaurante é {restaurante.restaurant_name}')
# print(f'o tipo de cozinha do restaurante é {restaurante.cuisine_type}')

restaurante.describe_restaurant('Faustino', 'regional')
restaurante.open_restaurant()


