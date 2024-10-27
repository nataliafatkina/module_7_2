def custom_write(file_name, strings):
    strings_positions = {}
    number_str = 0

    file = open(file_name, 'a', encoding='utf-8')

    for string in strings:
        start_str = file.tell()
        file.write(string + '\n')
        strings_positions.update({(strings.index(string) + 1, start_str): string})
    file.close()
    return print(strings_positions)


info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

custom_write('test.txt', info)