import requests

api_url = ("https://api.openbrewerydb.org/breweries")
response = requests.get(api_url)
x = response.json()


class Brawery:
    def __init__(self, id: str, name: str, brewery_type: str, street: str,
                 address_2: str, address_3: str, city: str, state: str, country_province: str,
                 postal_code: str, country: str, longitude: str, latitude: str,
                 phone: str, webiste_url: str, updated_at: str, created_at: str) -> object:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.country_province = country_province
        self.postal_code = postal_code
        self.country = country
        self.longituted = longitude
        self.latituted = latitude
        self.phone = phone
        self.website_url = webiste_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        return f'ID: {self.id}, Nazwa: {self.name}, Miasto: {self.city}'


lista = []
y = 0
for item in x:
    if y < 20:
        y += 1
    else:
        break
    lista.append(Brawery(item['id'], item['name'], item['brewery_type'], item['street'], item['address_2'],
                         item['address_3'], item['city'], item['state'], item['county_province'], item['postal_code'],
                         item['country'], item['longitude'], item['latitude'], item['phone'], item['website_url'],
                         item['updated_at'], item['created_at']))

for x in range(len(lista)):
    print(lista[x])

# print(Brawery(response.name))
