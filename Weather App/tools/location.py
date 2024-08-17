class Location:
    def __init__(self, city, country=None) -> None:
        self.city = city
        self.country = country

    def __str__(self) -> str:
       return f"{self.city}, {self.country}" if self.country else self.city


if __name__ == "__main__":
    mytown = Location("Chino Hills", "USA")
    print(mytown)