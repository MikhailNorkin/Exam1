import csv
from io import UnsupportedOperation
import user_interface as ui
from dictionaries import dict_field as d1
from dictionaries import dict_translate as d2
import os
import re
import check as ch
import pandas as pd
from colorama import *
init()


def add_contact():
    '''
    Добавление контакта в новую строку.
    Первая строка - строка заголовков столбцов.
    Предусмотрены случаи:
    отсутствия файла, пустого файла, уже заполненного файла.
    '''
    ui.print_instructions_for_input()
    string_in_file, header = [], []
    # for i in range(1, 1):
    i = 1
    header.append(d2[d1[i]])

        # if i == 1:
            
        # if i == 2:    
        #     text = ui.input_data(d2[d1[i]])
        #     if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) != None:
        #         f = ch.check_double_surname(text)
        #     if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) == None:
        #         f = ch.check_textfield(text)
        #         f = str(f).capitalize()

        # if i == 1:
    text = ui.input_data(d2[d1[i]])
    # if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) != None:
    f = ch.check_double_surname(text)
    # if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) == None:
    #     f = ch.check_textfield(text)
    f = str(f).capitalize()
    string_in_file.append(f)
    try:
        results = pd.read_csv('contacts.csv')
        # print(results)
        open('contacts.csv')
        with open('contacts.csv', 'a', encoding='utf-8') as phonebook:
            file_writer = csv.writer(
                phonebook, delimiter='|', lineterminator="\r")
            if os.stat('contacts.csv').st_size != 0:
                file_writer.writerow(string_in_file)
            elif os.stat('contacts.csv').st_size == 0:
                file_writer.writerow(header)
                file_writer.writerow(string_in_file)
    except (FileNotFoundError, UnsupportedOperation):
        with open('contacts.csv', 'a', encoding='utf-8') as phonebook:
            file_writer = csv.writer(
                phonebook, delimiter='|', lineterminator="\r")
            file_writer.writerow(header)
            file_writer.writerow(string_in_file)


def rename(nuber_str):
    '''
    Поиск контакта по имени / фамилии.
    '''


    flag = False
    while flag == False:
        try:
            open('contacts.csv')
            try:
                nuber_str_int = int(nuber_str)
            except ValueError:
                print(Fore.GREEN + Back.RED +
                        '\nНужно ввести число! Введите еще раз')
                print(Fore.BLUE + Back.WHITE)
                nuber_str = input()
                continue
            with open('contacts.csv', 'r', encoding='utf-8') as fr:
                lines = fr.readlines()
                if (len(lines) < nuber_str_int+1) or (nuber_str_int < 1):
                    print(Fore.GREEN + Back.RED +
                         '\nВы ввели неправильный номер строки. Введите номер еще раз')
                    print(Fore.BLUE + Back.WHITE)
                    nuber_str = input()
                    continue
                else:
                    flag = True 
                    open('contacts.csv')
                    with open('contacts.csv', 'r', encoding='utf-8') as f:
                        data_str = f.read()
                        line11 = data_str.split('\n', 11)[nuber_str_int]
                        print(f"Строка "+ nuber_str + " выглядит следующим образом:")
                        print(line11)
                        print("Введите строку ее заменющую:")
                        nuber_str = input()
                    with open('contacts.csv', 'r', encoding='utf-8') as f:    
                        lines = f.readlines()
                    with open('contacts.csv', 'w', encoding='utf-8') as fw:
                        ptr = 0
                        for line in lines:
                            if ptr != nuber_str_int:
                                fw.write(line)
                            else:
                                fw.write(nuber_str+"\n")    
                            ptr += 1     
        except FileNotFoundError:
            print(Fore.GREEN + Back.RED +
                'Телефонная книга пуста, поэтому Вы не можете ее открыть!')
    # return line


def open_phonebook():
    '''
    Функция открывает файл с контактами (если он есть) и выводит список в консоль.
    '''
    try:
        open('contacts.csv')
        with open('contacts.csv', encoding='utf-8') as phonebook:
            file_reader = csv.reader(phonebook, delimiter='|')
            i = 0
            for row in file_reader:
                if len(row) > 0:
                    if i > 0:
                        print(f"{i} - {str(row)[2:-2]}")  
                    else: 
                        print(row) 
                    i = i + 1          

    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонной книги нет - Вы не можете ее открыть!')

def del_contact(nuber_str):

    flag = False
    while flag == False:
        try:
            open('contacts.csv')
            try:
                nuber_str_int = int(nuber_str)
            except ValueError:
                print(Fore.GREEN + Back.RED +
                        '\nНужно ввести число! Введите еще раз')
                print(Fore.BLUE + Back.WHITE)
                nuber_str = input()
                continue
            with open('contacts.csv', 'r', encoding='utf-8') as fr:
                lines = fr.readlines()
                if (len(lines) < nuber_str_int+1) or (nuber_str_int < 1):
                    print(Fore.GREEN + Back.RED +
                         '\nВы ввели неправильный номер строки. Введите номер еще раз')
                    print(Fore.BLUE + Back.WHITE)
                    nuber_str = input()
                    continue
                else:
                    flag = True    
                    ptr = 0        
                    with open('contacts.csv', 'w', encoding='utf-8') as fw:
                        for line in lines:
                            if ptr != nuber_str_int:
                                fw.write(line)
                            ptr += 1     

        except FileNotFoundError:
            print(Fore.GREEN + Back.RED +
                    'Телефонной книги нет - Вы не можете ее открыть!')

def delete_contact(data):
    '''
    Фунция удаляет найденный контакт. НЕ ДОРАБОТАНА!!!
    '''
    try:
        open('contacts.csv')
        search_line = find_contact(data)
        if len(search_line) == 1:
            print(Fore.BLACK + Back.MAGENTA +
                  f'Найдено 1 совпадение:\n{search_line}\n')
            operation = ui.confirm_operation()
            if operation == '1':
                print(1)
            if operation == '2':
                print(Fore.BLACK + Back.MAGENTA +
                      'Вы отказались от удаления записи. Переходим в основное меню.')
        if len(search_line) > 1:
            for i in range(0, len(search_line)):
                print(Fore.BLACK + Back.MAGENTA + 'Больше одной строки')
                print(f'№ {i+1} - {search_line[i]}')
            line_del = input(
                'Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
            flag = False
            while flag == False:
                try:
                    int(line_del)
                    if int(line_del) > 0:
                        if int(line_del) < len(search_line):
                            print(1)
                            flag = True
                    else:
                        print(Fore.GREEN + Back.RED)
                        line_del = input(
                            'Неверно указан номер строки! Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
                except ValueError:
                    print(Fore.GREEN + Back.RED)
                    line_del = input(
                        'Неверно указан номер строки! Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонная книга пуста, поэтому удалять нечего!')


# delete_contact('Дарья')
