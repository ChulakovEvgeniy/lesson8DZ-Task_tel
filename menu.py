from base_function import input_data, print_data, put_data, delete_data, input_num

def interface():
    command = -1
    while command != 5:
        print('Добро пожаловать в телефоный справочник! Что вы хотите сделать?\n'
              '1. Записать данные(в 2-х форматах)\n'
              '2. Удалить данные\n'
              '3. Изменить данные\n' 
              '4. Вывести данные\n'
              '5. Выход')
        command = input_num('Введите номер операции: ')

        while command < 1 or command > 5:
            print('Нет такого в меню, еще раз')
            command = input_num('Введите номер операции: ')

        match command:
            case 1:
                input_data()
            case 2:
                delete_data()
            case 3:
                put_data()
            case 4:
                print_data()
            case 5:
                print('Приятно было поработать вместе, возвращайся)))')