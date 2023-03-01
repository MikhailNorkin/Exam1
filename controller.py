import user_interface as ui
import contact_actions as ca
import os
os.system("cls")


def button_click():
    '''
    Запуск и отработка приложения.
    '''
    operation = ui.get_operation()
    if operation == 1:
        result = ca.open_phonebook()
    elif operation == 2:
        result = ca.add_contact()
    elif operation == 3:
        data = ui.input_text()
        result = ca.del_contact(data)
        # print('Функция в стадии разработки.')
    elif operation == 4:
        data = ui.rename_text()
        result = ca.find_contact(data)
    elif operation == 5:
        print('Функция в стадии разработки.')
    elif operation == 6:
        print('Функция в стадии разработки.')
    # ui.view_result(result)
