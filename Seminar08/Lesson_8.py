# 1. Открыть файл телефонной книги.
# 2. Сохранить файл телефонной книги.
# 3. Показать все контакты.
# 4. Найти контакт.
# 5. Добавить контакт.
# 6. Изменить контакт.
# 7. Удалить контакт.
# 8. Выход.

def menu():
    while True:
        title = int(input("""Введите запрос:
                                             1. Сохранить файл телефонной книги.
                                             2. Показать все контакты.
                                             3. Найти контакт.
                                             4. Добавить контакт.
                                             5. Изменить контакт.
                                             6. Удалить контакт.
                                             7. Выход."""))
        
        if title == 1:
            save_dir(dict_phnbk)
            print("Сохранено")
        elif title == 2:
            if len(dict_phnbk) == 0:
                dict_phnbk = open_read_dir()
            if len(dict_phnbk) == 0:
                print("Справочник пуст")
            else:
                print(dict_phnbk)
        elif title == 3:
            find_contact(dict_phnbk)
        elif title == 4:
           dict_phnbk = add_contact(dict_phnbk)
           print("Сохраните контакт!")
        elif title == 5:
            new_contact = find_contact(dict_phnbk)
            add_contact(dict_phnbk, new_contact)
        elif title == 6:
            pass
        elif title == 7:
            print('End')
            break
        else:
            print("Введите корректное значение:")
       
def open_read_dir():
    dict_phnbk = {}
    with open('phonebook.txt', 'r') as f:
        for line_contact in f.readlines():
            key, value = line_contact.split(':')
            dict_phnbk[key] = value
        return dict_phnbk
        
def save_dir(dict_phnbk):
    str_phnbk = ''
    for k, v in dict_phnbk.items():
        str_phnbk += f'{k} : {v} \n' 
    with open('phonebook.txt', 'w') as f:
        f.write(str_phnbk)
        
def add_contact(dict_phnbk, new_contact_in = [0]):
    if len(new_contact_in) < 2:
        name_contact = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        comment_contact = input("Добавить комментарий: ")
        contact_list = [phone_number,  comment_contact]
    else:
        name_contact, contact_list = tuple(new_contact_in)
    #dict_phnbk[name_contact] = dict_phnbk.setdefault(name_contact, contact_list)
    dict_phnbk.setdefault(name_contact, contact_list)
    print(dict_phnbk[name_contact])
    return dict_phnbk

def find_contact(dict_phnbk):
    name_contact = input("Введите ФИО: ")
    if name_contact in dict_phnbk:
        print(f" {name_contact} : {dict_phnbk[name_contact]}")
        return [name_contact, dict_phnbk[name_contact]]
    else:
        print("Проверьте корректность введеных данных!")
    
    
    