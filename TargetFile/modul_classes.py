from collections import UserDict, UserList

class Fields:
    name = None
    num_tel = None
    email = None
    date_birth = None

    class Record():
        pass

class AddressBook(UserDict, Fields):
    

# Заповнюємо словник існуючими контактами

    def fill_dict_phone(self, dict_phone=UserDict()):
        with open('phonebook.msf') as file_book:
            line_count = sum(1 for line in open('phonebook.msf'))

            if line_count > 0:
                for i in file_book:
                    key, value = i.split(' , ')
                    dict_phone[key] = value[:-1]

class Name():
    pass

class Phone():
    pass