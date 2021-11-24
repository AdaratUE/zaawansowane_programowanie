class Property:
    def __init__(self, area: int, rooms: int, price: int, address: str) -> object:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'{self.area} metrów kwadratowych, {self.rooms} pokoi, cena: {self.price} złotych, ' \
               f'adres: {self.address}'


class House(Property):
    def __init__(self, plot: int, area: int, rooms: int, price: int, address: str) -> object:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Rozmiar działki: {self.plot}, {self.area} metrów kwadratowych, {self.rooms} pokoi, cena: {self.price} złotych, ' \
               f'adres: {self.address}'


class Flat(Property):
    def __init__(self, floor: int, area: int, rooms: int, price: int, address: str) -> object:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Piętro: {self.floor}, {self.area} metrów kwadratowych, {self.rooms} pokoi, cena: {self.price} złotych, ' \
               f'adres: {self.address}'


dom = House(32, 121, 5, 321321, 'Jakastam 2')
mieszkanie = Flat(3, 44, 3, 222222, 'Ktoras 3')

print(dom)
print(mieszkanie)
