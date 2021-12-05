class Library:
    def __init__(self, city: str, street: str, zip_code: int, open_hours: str, phone: int) -> object:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Miasto: {self.city}, godziny otwarcia: {self.open_hours}"
