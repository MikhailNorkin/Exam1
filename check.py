import re
from typing import Optional
from colorama import *
init()


def check_number_operation(input_string: Optional[str]) -> Optional[int]:
    '''
    Функция проверки на целое число от 1 до 6.
    '''
    while type:
        print(Fore.BLUE + Back.WHITE)
        number_oper = input(input_string)
        try:
            number_oper = int(number_oper)
            if 0 < number_oper < 7:
                return number_oper
            else:
                print(Fore.GREEN + Back.RED +
                      '\nНеверный ввод данных! Должно быть целое число от 1 до 6 включительно!')
                print(Fore.BLUE + Back.WHITE)
                number_oper = input(input_string)
                continue
        except ValueError:
            print(Fore.GREEN + Back.RED +
                  '\nНеверный ввод данных! Должно быть целое число от 1 до 6 включительно!')


def check_confirm_operation(input_string: Optional[str]) -> Optional[int]:
    '''
    Функция проверки на целое число от 1 до 6.
    '''
    while type:
        print(Fore.BLUE + Back.WHITE)
        number_oper = input(input_string)
        try:
            number_oper = int(number_oper)
            if 0 < number_oper < 3:
                return number_oper
            else:
                print(Fore.GREEN + Back.RED +
                      '\nНеверный ввод данных! Должно быть целое число: 1 или 2!')
                print(Fore.BLUE + Back.WHITE)
                number_oper = input(input_string)
                continue
        except ValueError:
            print(Fore.GREEN + Back.RED +
                  '\nНеверный ввод данных! Должно быть целое число: 1 или 2!')


def check_double_surname(text):
    while len(text) > 40:
        print(Fore.GREEN + Back.RED)
        text = input(
            'Слишком много символов! Допустимо не более 40. Повторите ввод:\n')
    else:
        if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) != None:
            text_list = text.split('-')
        for i in range(0, len(text_list)):
            text_list[i] = text_list[i].capitalize()
        text = '-'.join(text_list)
        return text


def check_textfield(text, optional=1):
    '''
    Функция проверяет ввод текстового поля (обязательного: optional = 1 (по умолчанию), необязательного: optional = 0).
    '''
    flag = False
    while flag == False:
        if optional == 0:
            while len(text) > 40:
                print(Fore.GREEN + Back.RED)
                text = input(
                    'Слишком много символов! Допустимо не более 40. Повторите ввод:\n')
            else:
                if re.match('^[а-яёА-ЯЁ]{2,40}$', text) != None or text == '-':
                    flag = True
                    return text
                elif re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) != None:
                    flag = True
                    return text
                else:
                    print(Fore.GREEN + Back.RED)
                    text = input(
                        'Некорректный ввод, повторите:\n')
        if optional == 1:
            while len(text) > 40:
                print(Fore.GREEN + Back.RED)
                text = input(
                    'Слишком много символов! Допустимо не более 40. Повторите ввод:\n')
            else:
                if re.match('^[а-яёА-ЯЁ]{2,40}$', text) != None:
                    flag = True
                    return text
                elif re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) != None:
                    flag = True
                    return text
                else:
                    print(Fore.GREEN + Back.RED)
                    text = input(
                        'Неверный ввод данных! Должны быть только буквы русского алфавита. Не менее 2 и не более 40 символов. Повторите ввод:\n')


def check_free_textfield(text):
    '''
    Функция проверяет ввод текстового поля свободного содержания.
    '''
    flag = False
    while flag == False:
        if len(text) > 40:
            print(Fore.GREEN + Back.RED)
            text = input(
                'Слишком много символов! Допустимо не более 40. Повторите ввод:\n')
        else:
            flag = True
            return text


def check_mobile(text):
    '''
    Функция проверяет корректность ввода мобильного телефона.
    '''
    flag = False
    while flag == False:
        if text[0] == '0':
            print(Fore.GREEN + Back.RED)
            text = input(
                'Некорректный ввод данных! Как минимум первая цифра "0" невозможна:\n')
        elif text == '-':
            flag = True
            return text
        elif len(text) != 12:
            if len(text) != 11:
                print(Fore.GREEN + Back.RED)
                text = input(
                    'Некорректный ввод! Слишком мало или слишком много символов, либо введены буквы / неверные цифры вначале. Номер телефона заполняйте только из цифр (допустимо указать "+7" в начале). Наберите заново:\n')
        elif len(text) == 12 and text[:2] != '+7':
            print(Fore.GREEN + Back.RED)
            text = input(
                'Некорректный ввод! Слишком мало или слишком много символов, либо введены буквы / неверные цифры вначале. Номер телефона заполняйте только из цифр (допустимо указать "+7" в начале). Наберите заново:\n')
        try:
            int(text)
            flag = True
            return text
        except ValueError:
            print(Fore.GREEN + Back.RED)
            text = input(
                'Некорректный ввод данных (встречаются нецифры)! Наберите заново:\n')
            continue


def check_homephone(text):
    '''
    Функция проверяет корректность ввода домашнего телефона.
    '''
    flag = False
    while flag == False:
        if text[0] == '0':
            print(Fore.GREEN + Back.RED)
            text = input(
                'Некорректный ввод данных! Как минимум первая цифра "0" невозможна:\n')
        elif text == '-':
            flag = True
            return text
        elif len(text) < 5 or len(text) > 7:
            print(Fore.GREEN + Back.RED)
            text = input(
                'Некорректный ввод! Слишком мало или слишком много символов. Наберите заново:\n')
        else:
            try:
                int(text)
                flag = True
                return text
            except ValueError:
                print(Fore.GREEN + Back.RED)
                text = input(
                    'Некорректный ввод данных! В номере присутствуют не только цифры! Наберите заново:\n')
                continue


def remove_spaces_in_string(text: Optional[str]) -> Optional[str]:
    '''
    Чистит строку - удаляет все пробелы.
    '''
    text = text.replace(' ', '')
    return text
