from data_create import name_data, surname_data, phone_data, address_data

def input_num(message: str) -> int:
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)

def change_request(message: str,data):
    print('Что вы знаете о контакте:\n'
          '1. Фамилию\n'
          '2. Имя\n'
          '3. Номер телефона\n'
          '4. Номер записи')
    var = input_num('Введите номер варианта:')

    match var:
        case 1 | 2:
            second_name = input('Введите фамилию или Имя: ').title()
            for i in range(len(data)):
                if second_name in data[i]:
                    return i
        case 3:
            phone = input('Введите телефон: ')
            for i in range(len(data)):
                if phone in data[i]:
                    return i
        case 4:
            print(message)
            number_journal = input_num('Введите номер записи: ')
            number_journal -= 1

            while number_journal < 0 or number_journal > len(data):
                print('\nтакого пункта нет, попробуй еще раз')
                number_journal = input_num('Выберите номер записи: ')
                number_journal -= 1
            return number_journal

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = input_num(f'В каком формате Вы хотите записать данные?\n\n'
                    f'1 Вариант:\n\n'
                    f'{surname}\n'
                    f'{name}\n'
                    f'{phone}\n'
                    f'{address}\n\n'
                    f'2 вариант\n\n'
                    f'{surname};{name};{phone};{address}\n\n'
                    'Выберите номер варианта: ')
    while var != 1 and var != 2:
        print('такого пункта нет, попробуй еще раз')
        var = input_num('Выберите номер варианта: ')

    match var:
        case 1:
            with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
                file.write(f'{surname}\n{name}\n{phone}\n{address}\n\n')
        case 2:
            with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
                file.write(f'{surname};{name};{phone};{address}\n\n')


def print_data(arg = 3):
    match arg:
        case 1:
            print('Вывожу данные для Вас данные из 1 файла\n')
            with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
                data_first = file.readlines()
                data_first_version_second = []
                j = 0
                for i in range(len(data_first)):
                    if data_first[i] == '\n' or i == len(data_first) - 1:
                        data_first_version_second.append(''.join(data_first[j:i + 1]))
                        j = i
                data_first = data_first_version_second
                print(''.join(data_first))
                return data_first
        case 2:
            print('Вывожу данные для Вас данные из 2 файла\n')
            with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
                data_second = list(file.readlines())
                print(*data_second)
            return data_second
        case 3:
            print('Вывожу данные для Вас данные из 1 файла\n')
            with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
                data_first = file.readlines()
                data_first_version_second = []
                j = 0
                for i in range(len(data_first)):
                    if data_first[i] == '\n' or i == len(data_first)-1:
                        data_first_version_second.append(''.join(data_first[j:i + 1]))
                        j = i
                data_first = data_first_version_second
                print(''.join(data_first))

            print('Вывожу данные для Вас данные из 2 файла\n')
            with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
                data_second = list(file.readlines())
                print(*data_second)
            return data_first, data_second

def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data(3)
    number_file = input_num('Введите номер файла: ')

    while number_file != 1 and number_file != 2:
        print('такого пункта нет, попробуй еще раз')
        number_file = input_num('Выберите номер варианта: ')

    match number_file:
        case 1:
            number_journal = change_request('Какую запись Вы хотите изменить?', data_first)

            print(f'Изменить данную запись\n{data_first[number_journal]}')
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            data_first = data_first[:number_journal] + [f'{surname}\n{name}\n{phone}\n{address}\n'] + \
                data_first[number_journal + 1:]
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(''.join(data_first))
            print_data(1)
            print('Изменения успешно сохранены!')


        case 2:
            number_journal = change_request('Какую запись Вы хотите изменить?', data_second)

            print(f'Изменить данную запись\n{data_second[number_journal]}')
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            data_second = data_second[:number_journal]+[f'{surname};{name};{phone};{address}\n'] + \
                data_second[number_journal + 1:]
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(''.join(data_second))
            print_data(2)
            print('Изменения успешно сохранены!')

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data(3)
    number_file = input_num('Введите номер файла: ')

    while number_file != 1 and number_file != 2:
        print('такого пункта нет, попробуй еще раз')
        number_file = input_num('Выберите номер варианта: ')

    match number_file:
        case 1:
            number_journal = change_request('Какую запись Вы хотите удалить?', data_first)

            print(f'Удалить данную запись\n{data_first[number_journal]}')
            data_first = data_first[:number_journal] + data_first[number_journal + 1:]
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(''.join(data_first))
            print_data(1)
            print('Изменения успешно сохранены))')

        case 2:
            number_journal = change_request('Какую запись Вы хотите удалить?', data_second)

            print(f'Удалить данную запись?\n{data_second[number_journal]}'
                  '1.Да\n'
                  '2.Нет')
            answer = input_num('Выберите номер варианта: ')

            while answer != 1 and number_file != 2:
                print('такого пункта нет, попробуй еще раз')
                answer = input_num('Выберите номер варианта: ')

            match answer:
                case 1:
                    data_second = data_second[:number_journal] + data_second[number_journal + 1:]
                    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                        file.write(''.join(data_second))
                    print_data(2)
                    print('Изменения успешно сохранены))')
                case 2:
                    print('думай лучше\n')