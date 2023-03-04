import export_func as basic
import modul_classes as mc


def main_menu():

    basic.os.system('CLS')
    print('==== main menu ====')
    print('How can I help you?')
    print('1. - Phonebook\n2. - Calendar\n3. - Exit\nYour chois:')

    chois = input('>>>>  ')
    if chois == '1':
        phone_menu()
    elif chois == '2':
        calendar_menu()
    else:
        basic.input_output('end')


def phone_menu():

    basic.os.system('CLS')
    print('==== phonebook menu ====')
    print('add - adding a contact to the phonebook\nchange - change an existing contact'
          '\nphone - contact information by name\nshow all - list of all contacts\n'
          'del - deleting a contact from the phonebook\nexit - exit to main menu'
          '\nYour chois:')

    
    chois = input('>>>>  ').lower()
    if chois == 'add':
        basic.os.system('CLS')
        print('==== adding contact ===')
        check_data = False
        while check_data == False:
            print('Enter phone number and contact name(Name Surname +380672972960)')
            data_contact = input('>>>> ')
            data_contact = data_contact.split('+')
            try:
                for r in data_contact[0]:
                    int(r)
                    print('Тame must not start with a number') 
                    break                 
            except ValueError:
                try:
                    check_number =basic.check_number(data_contact[1])
                    if check_number == True:
                        response = basic.add_record(data_contact)
                        if response == True:
                            print(f'Successfully added contact {data_contact[0]} {data_contact[1]}')
                            basic.time.sleep(2)
                            phone_menu()
                except IndexError:
                    print('Incomplete information entered, please re-enter')
                    continue
            check_data = True


    elif chois == 'change':

        basic.os.system('CLS')
        print('==== contact change ====')
        print('Enter contact name')
        name_contact = input('>>>>  ')
        list_result = basic.search_kontakts(name_contact)
        list_name = list()
        count = 1
        for name, number in list_result.items():
            print(str(count) ,'. ',name,' , ' ,number)
            list_name.append(name)
            count +=1

        if count > 2:
            print('Enter the number of the contact you want to change')
            name_change = input('>>>>  ')
        else:
            name_change = name 

        checking = False
        while checking == False:
            print(f'Enter a new phone number for contact {list_name[int(name_change)-1]} (specimen - +380672972960)')        
            new_number = input('>>>>  ')
            result = basic.check_number(new_number)
            if result == True:
                checking = True

        result_change = basic.change_record(list_name[int(name_change)-1], new_number)
        if result_change == True:
            print(f'Contact {name} changed, old number {number} - new number set as {new_number}') 
            basic.time.sleep(3)       
            phone_menu()
        

    elif chois == 'phone':

        basic.os.system('CLS')

        if len(basic.dict_phone) == 0:
            basic.fill_dict_phone()

        search = True
        while search == True:
            print('==== contact information ====')
            print('enter contact name')
            name_contact = input ('>>>>  ')
            result_names = basic.search_kontakts(name_contact)

            if len(result_names) == 0:
                print('Contacts with such data were not found. Repeat search? (yes/no)')
                response = input('>>>>  ')
                if response.lower() == 'no':
                    search = False
            else:
                for key, value in result_names.items():
                    print(f'{key}  {value}')
                    search = False

        print('Return in menu phonebook ?(yes/no)')
        if input('>>>>  ').lower() == 'yes':
            phone_menu()
        else:
            main_menu()

    elif chois == 'show all':
        basic.show_all_record()
        print('Return in menu phonebook ?(yes/no)')
        if input('>>>>  ').lower() == 'yes':
            phone_menu()
        else:
            main_menu()

    elif chois == 'del':

        basic.os.system('CLS')
        print('==== delete change ====')
        print('Enter contact name')
        name_contact = input('>>>>  ')
        list_result = basic.search_kontakts(name_contact)
        list_name = list()
        count = 1
        for name, number in list_result.items():
            print(str(count), '. ', name, ' , ', number)
            list_name.append(name)
            count += 1
        if count >2:
            print('Enter the number of the contact you want to delete')
            name_change = input('>>>>  ')
        else:
            name_change = name
        print(f'{name} entry will be deleted from the phonebook.(yes/no)\nYour choise')
        result = input('>>>>  ')
        if result.lower() == 'yes':
            basic.delete_record(name)
        print(f'Record {name} deleted from phone book')
        print('Return in menu phonebook ?(yes/no)')
        if input('>>>>  ').lower() == 'yes':
            phone_menu()
        else:
            main_menu()

    elif chois == 'exit':
        main_menu()

    else:
        print('Incorrect chois...')
        basic.time.sleep(3)
        phone_menu() 
        

def calendar_menu():
    basic.operation_calendar()
    print('Return in main menu ?(yes/no)')
    if input('>>>>  ').lower() == 'yes':
            main_menu()
    else:
        calendar_menu()


def __main__():
    print('Hello! I am a bot.\n Enter "hello" to get started or any other word to exit.')
    chois = input('>>>>  ').lower()
    chois = basic.input_output(chois)
    if chois == True:
        main_menu()

__main__()
