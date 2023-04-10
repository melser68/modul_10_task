from collections import UserDict

#Ім'я контакту
class Name():
    def __init__(self, name) -> None:
        self.name = name

#Загальні поля для книги контактів
class Fields(Name):
    phone = []
    email = ''
    date_birth = ''

    def __init__(self, name) -> None:
        super().__init__(name)

#Процедури для перевірки коректності дій у класі Record
class TestingProcedures():
    pass

#Створення записів, зміна заптсів, видалення записів
class Record(Fields, TestingProcedures):
    
    def __init__(self, name) -> None:
        super().__init__(name)

#основний клас для створення екземплярів
class AddresBook(Record, UserDict):
    book_contact = UserDict()