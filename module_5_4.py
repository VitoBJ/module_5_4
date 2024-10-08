class House:
    houses_history = []  

    def __new__(cls, name, number_of_floors):
        print(f"Creating a new house: {name}")
        instance = super(House, cls).__new__(cls)
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)
        print(f"Initialized house: {self.name}, Floors: {self.number_of_floors}")

    @classmethod
    def display_history(cls):
        print("History of created houses:")
        for house in cls.houses_history:
            print(house)


house1 = House('Sky Tower', 20)
house2 = House('Lakeside Villa', 5)
house3 = House('Mountain Lodge', 3)


House.display_history()