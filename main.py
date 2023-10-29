from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        if value is not None and value.strip():  # Перевірка, що ім'я не є пустим рядком або None
            super().__init__(value)
        else:
            raise ValueError("Name is required")


class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if Phone.is_valid_phone_number(value):
            super().__init__(value)
    def is_valid_phone_number(phone_number):
        # Перевірка чи номер телефону має 10 цифр
        return phone_number.isdigit() and len(phone_number) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone_number):
        # Метод для додавання об'єкта Phone до списку phones
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        # Метод для видалення об'єкта Phone зі списку phones
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_phone_number, new_phone_number):
        # Метод для редагування номера телефону
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number

    def find_phone(self, phone_number):
        # Метод для пошуку об'єкта Phone за номером телефону
        for phone in self.phones:
            if phone.value == phone_number:
                return phone


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        # Метод для додавання запису до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Метод для пошуку запису за ім'ям
        return self.data.get(name)

    def delete(self, name):
        # Метод для видалення запису за ім'ям
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()
    

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")