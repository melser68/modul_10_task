
import os, calendar, time

dict_phone = {} 

# Заповнюємо словник існуючими контактами
def fill_dict_phone():
    file_book = open('phonebook.msf')
    line_count = sum(1 for line in open('phonebook.msf'))

    if line_count > 0:
        for i in file_book:
            key, value = i.split(' , ')
            dict_phone[key] = value[:-1]
    file_book.close()


#Перевірка номера на коректність
def check_number(number):
    if len(number) < 12:
        print('Incorrect phone number')
        return False
    else:
        return True


# Пошук існуючого контакту, або контактів у довіднику
def search_kontakts(name_contact):

    if len(dict_phone) == 0:
        fill_dict_phone()

    res_search = {}

    for kontakt, num_tel in dict_phone.items():
        if name_contact in kontakt.lower():
            res_search.update({kontakt: num_tel})

    return res_search


#Реакція на ввод користувача у головному меню
def input_output(text_user):

    if text_user == 'hello':
        return True
    else:        
        print('=== GoobBye ! ===')



def add_record(data_contact):     
    
    dict_phone[data_contact[0]] = data_contact[1]
    phonebook = open('phonebook.msf', 'a+')
    phonebook.write(str(data_contact[0]) + ' , ' + '+'+data_contact[1])
    phonebook.write('\n')
    phonebook.close() 
    return True       



def change_record(name_search, new_number):

    if len(dict_phone) == 0:
        fill_dict_phone()
    
    for name_book, number_book in dict_phone.items():
        if name_search == name_book:           
            dict_phone.update({name_book: new_number})
            os.system('CLS')
            
            phonebook = open('phonebook.msf', 'w')
            for i, y in dict_phone.items():
                phonebook.write(i + ' , ' + y)
                phonebook.write('\n')
            phonebook.close()
    
    return True



def show_all_record():

    if len(dict_phone) == 0:
        fill_dict_phone()

    os.system('CLS')

    if len(dict_phone) == 0:
        print('Phone book is empty')
    else:
        for name_book, number_book in dict_phone.items():
            print(name_book, ' ', number_book)


def delete_record(name_contact):
    if len(dict_phone) == 0:
        fill_dict_phone()
    for name_search in dict_phone:
        if name_contact == name_search:
            dict_phone.pop(name_search)
            break
    phonebook = open('phonebook.msf', 'w+')
    for key, data in dict_phone.items():
        phonebook.write(key + ' , ' + data)
        phonebook.write('\n')
    phonebook.close()


def operation_calendar():
    os.system('CLS')
    print('==== calendar ====')
    calendar.TextCalendar().pryear(2023)



