class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()
        return products

    def add(self, *products):
        with open(self.__file_name, 'r') as file:
            existing_products = file.readlines()
            existing_names = [product.strip().split(',')[0] for product in existing_products]
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_names:
                    file.write(f"{product}\n")
                else:
                    print(f"Продукт {product.name} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__ это первый запуск
print(s1.get_products()) # это первый запуск, после первого запуска удалить)))
# не пойму, как сделать так, чтобы при первом запуске показывало как в условиях задачи.
# поэтому, для получения второго запуска просьба удалить принт из строки 36.
s1.add(p1, p2, p3)


print(s1.get_products())
