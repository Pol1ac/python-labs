from enum import Enum
class ClothingType(Enum):
    SHIRT = 1
    JEANS = 2
    JACKET = 3
    # Додайте інші типи одягу за необхідністю

class Clothing:
    def __init__(self, name, description, location, colour, size, clothing_type):
        self.name = name
        self.description = description
        self.location = location
        self.colour = colour
        self.size = size
        self.clothing_type = clothing_type

    def __lt__(self, other):
        return self.size < other.size

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Location: {self.location}")
        print(f"Colour: {self.colour}")
        print(f"Size: {self.size}")
        print(f"Type: {self.clothing_type}")

    def additional_method(self):
        print("This is an additional method for Clothing.")

class Wardrobe:
    def __init__(self):
        self.clothes = []

    def add_clothing(self, clothing):
        self.clothes.append(clothing)

    def go_out(self):
        types_count = len(set(clothing.clothing_type for clothing in self.clothes))
        ready_to_go_out = types_count > 3
        return ready_to_go_out

    def sort_clothes_by_size(self):
        self.clothes.sort()

# Приклад використання:
def main():
    wardrobe = Wardrobe()

    shirt1 = Clothing("T-Shirt", "Casual shirt", "Closet", "Blue", "M", ClothingType.SHIRT)
    jeans1 = Clothing("Denim Jeans", "Casual jeans", "Closet", "Black", "30", ClothingType.JEANS)
    jacket1 = Clothing("Leather Jacket", "Stylish jacket", "Closet", "Brown", "L", ClothingType.JACKET)

    wardrobe.add_clothing(shirt1)
    wardrobe.add_clothing(jeans1)
    wardrobe.add_clothing(jacket1)

    # Демонстрація виведення інформації про одяг
    for clothing_item in wardrobe.clothes:
        clothing_item.display_info()
        print()

    # Перевірка готовності вийти на вулицю
    if wardrobe.go_out():
        print("Готовий вийти на вулицю!")
    else:
        print("Не готовий вийти на вулицю.")

    # Сортування одягу за розміром
    wardrobe.sort_clothes_by_size()

    # Виклик додаткового методу для класу одягу
    shirt1.additional_method()

if __name__ == "__main__":
    main()
