

class Name:
    __name = ''
    __surname = ''

    @property
    @classmethod
    def contact_name(cls):
        return cls.__name, ' ', cls.__surname

    @contact_name.__setattr__
    def contact_name(cls, name, surname):
        cls.__name = name
        cls.__surname = surname

class Fields(Name):
    name = Name.name
    surname = Name.surname
    phone = ''
    email = ''

