
class FirstClass:

    def check_number(func):
        def wrapper(*args, **kwargs):
            for i in args:
                if i > 100:
                    print('Number > 100')
                else:
                    return func
        return wrapper

    @check_number
    def set_number(self, number):
        self.number = number


user = FirstClass()
user.set_number(101)
        



    
