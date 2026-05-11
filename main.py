# 1. Car class
class Car:
    wheels = 4
    country = "Germany"

    def __init__(self, brand, color, price, speed):
        self.brand = brand
        self.color = color
        self.price = price
        self.speed = speed

    def show_car(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print(f"Speed: {self.speed}")
        print(f"Wheels: {Car.wheels}")
        print(f"Country: {Car.country}")

    def change_color(self, new_color):
        print(f"{self.brand} rangi o'zgardi: {self.color} -> {new_color}")
        self.color = new_color

    def increase_speed(self, km):
        self.speed += km
        print(f"{self.brand} tezligi oshdi: {self.speed}")

c1 = Car("BMW", "black", 50000, 200)
c2 = Car("Mercedes", "white", 80000, 220)

print("===== OLDIN =====")
c1.show_car()
print("------------")
c2.show_car()

print("\n===== O'ZGARISHLAR =====")
c1.change_color("red")
c1.increase_speed(50)
c2.change_color("blue")

print("\n===== KEYIN =====")
c1.show_car()
print("------------")
c2.show_car()


# 2. Phone class
class Phone:
    factory = "China"
    charger_type = "Type-C"

    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price

    def show_phone(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Memory: {self.memory}GB")
        print(f"Price: {self.price}")
        print(f"Factory: {Phone.factory}")
        print(f"Charger: {Phone.charger_type}")

    def change_price(self, new_price):
        print(f"{self.brand} narxi o'zgardi: {self.price} -> {new_price}")
        self.price = new_price

    def upgrade_memory(self, new_memory):
        print(f"{self.brand} xotirasi o'zgardi: {self.memory} -> {new_memory}")
        self.memory = new_memory

p1 = Phone("Samsung", "S24", 128, 1200)
p2 = Phone("iPhone", "15", 256, 1500)
p3 = Phone("Xiaomi", "13", 128, 800)

print("\n===== OLDIN =====")
p1.show_phone()
print("------------")
p2.show_phone()
print("------------")
p3.show_phone()

print("\n===== O'ZGARISHLAR =====")
p1.change_price(1100)
p1.upgrade_memory(256)
p2.change_price(1400)

print("\n===== KEYIN =====")
p1.show_phone()
print("------------")
p2.show_phone()


# 3. Employee class
class Employee:
    company_name = "Google"
    work_time = "09:00 - 18:00"

    def __init__(self, fullname, salary, position, age):
        self.fullname = fullname
        self.salary = salary
        self.position = position
        self.age = age

    def show_employee(self):
        print(f"Ism: {self.fullname}")
        print(f"Maosh: {self.salary}")
        print(f"Lavozim: {self.position}")
        print(f"Yosh: {self.age}")
        print(f"Kompaniya: {Employee.company_name}")
        print(f"Ish vaqti: {Employee.work_time}")

    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.fullname} maoshi oshdi: {self.salary}")

    def change_position(self, new_position):
        print(f"{self.fullname} lavozimi o'zgardi: {self.position} -> {new_position}")
        self.position = new_position

e1 = Employee("Azamat", 5000, "Junior", 22)

print("\n===== OLDIN =====")
e1.show_employee()

print("\n===== O'ZGARISHLAR =====")
e1.increase_salary(1000)
e1.change_position("Middle")

print("\n===== KEYIN =====")
e1.show_employee()


# 4. Animal class
class Animal:
    kingdom = "Animals"
    planet = "Earth"

    def __init__(self, name, color, weight, age):
        self.name = name
        self.color = color
        self.weight = weight
        self.age = age

    def show_animal(self):
        print(f"Nomi: {self.name}")
        print(f"Rangi: {self.color}")
        print(f"Vazni: {self.weight}kg")
        print(f"Yoshi: {self.age}")
        print(f"Kingdom: {Animal.kingdom}")
        print(f"Planet: {Animal.planet}")

    def change_weight(self, new_weight):
        print(f"{self.name} vazni o'zgardi: {self.weight} -> {new_weight}")
        self.weight = new_weight

a1 = Animal("Sher", "sariq", 200, 5)
a2 = Animal("Fil", "kulrang", 5000, 20)
a3 = Animal("Tulki", "qizil", 10, 3)

print("\n===== OLDIN =====")
a1.show_animal()
print("------------")
a2.show_animal()
print("------------")
a3.show_animal()

print("\n===== O'ZGARISHLAR =====")
a1.change_weight(210)
a2.change_weight(5100)

print("\n===== KEYIN =====")
a1.show_animal()
print("------------")
a2.show_animal()


# 5. Book class
class Book:
    library_name = "Central Library"
    language = "English"

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def show_book(self):
        print(f"Nomi: {self.title}")
        print(f"Muallif: {self.author}")
        print(f"Sahifalar: {self.pages}")
        print(f"Narx: {self.price}")
        print(f"Kutubxona: {Book.library_name}")
        print(f"Til: {Book.language}")

    def change_price(self, new_price):
        print(f"{self.title} narxi o'zgardi: {self.price} -> {new_price}")
        self.price = new_price

    def add_pages(self, count):
        self.pages += count
        print(f"{self.title} sahifalari oshdi: {self.pages}")

b1 = Book("Python", "Guido", 300, 50)

print("\n===== OLDIN =====")
b1.show_book()

print("\n===== O'ZGARISHLAR =====")
b1.change_price(45)
b1.add_pages(50)

print("\n===== KEYIN =====")
b1.show_book()


# 6. BankCard class
class BankCard:
    bank_name = "Anor Bank"
    currency = "UZS"

    def __init__(self, owner, balance, card_number, password):
        self.owner = owner
        self.balance = balance
        self.card_number = card_number
        self.password = password

    def show_card(self):
        print(f"Egasi: {self.owner}")
        print(f"Balans: {self.balance}")
        print(f"Karta raqami: {self.card_number}")
        print(f"Bank: {BankCard.bank_name}")
        print(f"Valyuta: {BankCard.currency}")

    def add_balance(self, amount):
        self.balance += amount
        print(f"Balans oshdi: {self.balance}")

    def remove_balance(self, amount):
        self.balance -= amount
        print(f"Balans kamaydi: {self.balance}")

bc1 = BankCard("Azamat", 1000000, "8600123456789", "1234")

print("\n===== OLDIN =====")
bc1.show_card()

print("\n===== O'ZGARISHLAR =====")
bc1.add_balance(500000)
bc1.remove_balance(200000)

print("\n===== KEYIN =====")
bc1.show_card()


# 7. Teacher class
class Teacher:
    school = "School 12"
    country = "Uzbekistan"

    def __init__(self, fullname, subject, experience, salary):
        self.fullname = fullname
        self.subject = subject
        self.experience = experience
        self.salary = salary

    def show_teacher(self):
        print(f"Ism: {self.fullname}")
        print(f"Fan: {self.subject}")
        print(f"Tajriba: {self.experience} yil")
        print(f"Maosh: {self.salary}")
        print(f"Maktab: {Teacher.school}")
        print(f"Mamlakat: {Teacher.country}")

    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.fullname} maoshi oshdi: {self.salary}")

    def change_subject(self, new_subject):
        print(f"{self.fullname} fani o'zgardi: {self.subject} -> {new_subject}")
        self.subject = new_subject

t1 = Teacher("Malika", "Math", 5, 3000)

print("\n===== OLDIN =====")
t1.show_teacher()

print("\n===== O'ZGARISHLAR =====")
t1.increase_salary(500)
t1.change_subject("Physics")

print("\n===== KEYIN =====")
t1.show_teacher()


# 8. Laptop class
class Laptop:
    ram_type = "DDR5"
    os = "Windows 11"

    def __init__(self, brand, cpu, ram_size, storage):
        self.brand = brand
        self.cpu = cpu
        self.ram_size = ram_size
        self.storage = storage

    def show_laptop(self):
        print(f"Brand: {self.brand}")
        print(f"CPU: {self.cpu}")
