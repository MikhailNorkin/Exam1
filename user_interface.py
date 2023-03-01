import check as ch
from colorama import *
init()


def confirm_operation():
    '''
    Функция получает номер опреации и проверяет его на корректность.
    '''
    operation = ch.check_confirm_operation(
        'Подтверждаете выполнение операции? \n 1 - Да (Подтверждаю) \n 2 - Нет (Отклоняю) \n')
    return operation


def input_data(data):
    print(Fore.GREEN + Back.YELLOW)
    f = input(
        f'\n Добавьте заметку:\n')
    return f


def input_text():
    print(Fore.BLACK + Back.MAGENTA)
    text = input(
        #'Кого будем искать? Напишите Имя или Фамилию (регистр непринципиален): ')
        '\nКакую строчку будем удалять? Введите номер строки:  ')
    return text

def rename_text():
    print(Fore.BLACK + Back.MAGENTA)
    text = input(
        #'Кого будем искать? Напишите Имя или Фамилию (регистр непринципиален): ')
        '\nКакую строчку будем редактировать? Введите номер строки:  ')
    return text


def print_instructions_for_input():
    print(Fore.BLACK + Back.MAGENTA + 'При добавлении новой записи необходимо учесть следующее^\n Поле  должно состоять только из букв русского алфавита. Не менее 2 и не более 40 символов.\n')


def get_operation():
    '''
    Функция получает номер операции и проверяет его на корректность.
    '''
    operation = ch.check_number_operation(
        'Какую операцию вы хотите выполнить? \n 1 - Открыть текущий справочник (вывод в консоль) \n 2 - Добавить новую запись \n 3 - Удалить запись \n 4 - Редактировать запись\n')
    return operation
