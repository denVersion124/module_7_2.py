def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'wb') as file:
        for index, string in enumerate(strings, start=1):
            # Получаем текущую позицию байта перед записью
            byte_position = file.tell()
            # Кодируем строку в байты и записываем в файл
            file.write(string.encode('utf-8') + b'\n')
            # Добавляем кортеж (номер строки, позиция начала) в словарь
            strings_positions[(index, byte_position)] = string

    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)