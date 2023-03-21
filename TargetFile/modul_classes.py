from string import ascii_letters
from collections import UserDict

UA_LETTERS = "йцукенгшщзхїфівапролджєячсмитьбю'"
UA_LETTERS_UP = UA_LETTERS.upper()
LETTERS = ascii_letters + UA_LETTERS + UA_LETTERS_UP + ' '


class Fields:
    """Можна буде взяти статистику по номерам телефонів"""
    f_name = []
    f_phone = []
    f_email = []


class Name(Fields):    

    @property
    def contact_name(self):
        return self.name

    @contact_name.setter
    def contact_name(self, name):
        Record.fill_phonebook()        

        if len(name.strip(LETTERS)) == 0:
            if len(name) > 0:
                self.name = name
                self.f_name.append(name)
                return True
                
            else:
                print('name must contain at least one character')
                return False
        else:
            print('Name can only contain english or ukrainian letters and spaces')
            return False
    
    @contact_name.deleter
    def contact_name(self):
        self.f_name.remove(self.name)
        try:
            del self.phonebook[self.name]
        except KeyError:
            pass
        del self.data[self.name]
        del self.name
        del self.__dict__['phone']
        Record.save_record(self)       
        


class Phone(Fields):  

    
    def check_num_in_book(func):
        def wrapper(*args, **kwargs):
            for i in args:
                if i in self.f_phone:
                    print('This number already exists')
                else:
                    return func(args)
        return wrapper
    

    @property
    def number(self):
        return (', ').join(self.phone)

    
    @number.setter
    @check_num_in_book    
    def number(self, number):
              
        if len(number) == 13 and number[0] == '+' or len(number) == 0:
            if len(number) == 0:
                number = 'no phone'
            try:
                self.phone.append(number)                
            except AttributeError:
                self.phone = [number]
            if number != 'no phone':
                self.f_phone.append(number)                               
            if self.data.get(self.name) == None:
                self.data.update({self.name: {'phone':self.phone}})
            Record.save_record(self)
                
            return True               
        else:
            print('The entered number does not match the pattern')
            return False
    
    
    def del_number(self, number):
        self.f_phone.remove(number)
        self.phone.remove(number)
        if len(self.phone)  == 0:
            self.phonebook.update({self.name: {'phone':'no number phone'}})
        Record.save_record(self)
    




class AdressBook(UserDict, Phone, Name):
    phonebook = UserDict()    


class Record(AdressBook):

    def change_name(self, name_contact):
        res_search = {}
        for kontakt, list_num in self.phonebook.items():
            if name_contact.lower() in kontakt.lower():
                res_search.update({kontakt: list_num})

        return res_search

    def save_record(self):    
        with open('save_book.msf', 'w') as fh:
            for i, y in self.data.items():
                for a, b in y.items():
                    fh.write(i + ' : ' + (',').join(b) + '\n')
    @classmethod
    def fill_phonebook(cls):
        
        try:
            with open('save_book.msf') as fh:
                while True:
                    a = fh.readline()
                    if not a:
                        break
                    else:
                        cls.phonebook.update(
                            {a[:-1].split(' : ')[0]: {'phone': a[:-1].split(' : ')[1].split(',')}})
        except FileNotFoundError:
            with open('save_book.msf', 'w') as fh:
                pass


    @classmethod
    def print_all (cls):
        cls.fill_phonebook() 
        if len(cls.phonebook) == 0:
            print('No records')
        else:
            for i, y in cls.phonebook.data.items():
                for a, b in y.items():
                    print(i + ' : ' + (', ').join(b))



contact = AdressBook()
contact.contact_name = 'Serhii Melnyk'
contact.number ='+380672972960'
contact.number = '+380672972960'


Record.print_all()