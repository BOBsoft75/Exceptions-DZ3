import re


class IncorrectDataFormatException(Exception):
    pass


class IncorrectDataAmountException(Exception):
    pass


def parse_input_data(input_string):
    input_data = input_string.strip().split(' ')
    if len(input_data) != 6:
        raise IncorrectDataAmountException('Введено некоректное количество данных!')

    last_name, first_name, middle_name, birth_date, phone_number, gender = input_data

    # Проверяем формат введенных фамилии, имени, отчества
    if not all(re.match(r'^[a-zA-Zа-яА-Я]+$', name) for name in (last_name, first_name, middle_name)):
        raise IncorrectDataFormatException('Некорректный формат ФИО (должно быть например: Иванов Иван Иванович)')

    # Проверяем формат введенной даты рождения
    if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', birth_date):
        raise IncorrectDataFormatException('Некорректный формат даты рождения (должно быть в формате: 01.12.1980)')

    # Проверяем формат введенного телефонного номера
    if not re.match(r'^\d+$', phone_number):
        raise IncorrectDataFormatException('Некорректный формат телефонного номера (должно быть 11 цифр например: 89119876655)')

    # Проверяем формат введенного пола
    if not gender in ('f', 'm'):
        raise IncorrectDataFormatException('Некорректный формат пола (должно быть m для мужского и f для женского)')

    return last_name, first_name, middle_name, birth_date, phone_number, gender
   

def save_to_file(data):
    last_name, _, _, _, _, _ = data
    with open(f'{last_name}.txt', 'a') as f:
        f.write(' '.join(data) + '\n')


def main():
    input_string = input('Введите данные в формате: Фамилия Имя Отчество, дата рождения, номер телефона, пол\n(Пример: Ivanov Ivan Ivanovich 05.12.1977 89117778899 m): ')
    try:
        data = parse_input_data(input_string)
    except (IncorrectDataFormatException, IncorrectDataAmountException) as e:
        print(f'Error: {e}')
        return

    try:
        save_to_file(data)
    except Exception as e:
        print(f'Ошибка записи данных в файл: {e}')


if __name__ == '__main__':
    main()
