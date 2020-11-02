

def one_time_pad_code(key_file_name, encryption_file_name, encrypted_file_name, process_show):
    key_file_txt = open(key_file_name, encoding='utf-8')
    encryption_file_txt = open(encryption_file_name, encoding='utf-8')
    encrypted_file_txt = open(encrypted_file_name, 'w', encoding='utf-8')
    key_text = key_file_txt.read().upper()
    encryption_text = encryption_file_txt.read().upper()
    punctuation = ',.-=+_!&?><@#$/*"%^ '
    for char in punctuation:
        while char in key_text:
            key_text = key_text.replace(char, '')
        while char in encryption_text:
            encryption_text = encryption_text.replace(char, '')

    print('Текст для шифрування: {0}'.format(encryption_text))
    print('Ключовий текст: {0}'.format(key_text))
    permitted_symbol = len(key_text) - len(encryption_text)
    selected_symbol = 0
    if permitted_symbol < 0:
        print('Текст для шифрування занадто великий.')
        return 0
    else:
        print('Максимальний номер символу, з якого можна обрати початок ключа: {0}'.format(permitted_symbol))
        while True:
            selected_symbol = int(input('Введіть номер символу, з якого починатиметься ключ.\n:'))
            if selected_symbol <= permitted_symbol and selected_symbol >= 0:
                break


    alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    encryption_code = []

    for i in range(len(encryption_text)):
        new_char = alphabet.find(encryption_text[i]) + alphabet.find(key_text[i + permitted_symbol]) + 2
        if process_show:
            print('{0} + {1} = {2}'.format(alphabet.find(encryption_text[i]) + 1,
                                       alphabet.find(key_text[i + permitted_symbol]) + 1, new_char))
        if new_char > 33:
            new_char -= 33
            if process_show:
                print('---> {0}'.format(new_char))
        encryption_code.append(new_char)


    encrypted_text = ''
    for char_code in encryption_code:
        encrypted_text += alphabet[char_code - 1]

    print('Зашифроване повідомлення: {0}'.format(encrypted_text))
    encrypted_file_txt.write(encrypted_text)

    encrypted_file_txt.close()
    encryption_file_txt.close()
    key_file_txt.close()


def one_time_pad_decode(key_file_name, message_file_name, encrypted_file_name, process_show):
    key_file = open(key_file_name, encoding='utf-8')
    encrypted_file = open(encrypted_file_name, encoding='utf-8')
    message_file = open(message_file_name, 'w', encoding='utf-8')
    key_text = key_file.read().upper()
    encrypted_text = encrypted_file.read().upper()
    punctuation = ',.-=+_!&?><@#$/*"%^ '
    for char in punctuation:
        while char in key_text:
            key_text = key_text.replace(char, '')
        while char in encrypted_text:
            encrypted_text = encrypted_text.replace(char, '')

    print('Текст для дешифрування: {0}'.format(encrypted_text))
    print('Ключовий текст: {0}'.format(key_text))
    permitted_symbol = len(key_text) - len(encrypted_text)
    selected_symbol = 0
    if permitted_symbol < 0:
        print('Текст для дешифрування занадто великий.')
        return 0
    else:
        print('Максимальний номер символу, з якого можна обрати початок ключа: {0}'.format(permitted_symbol))
        while True:
            selected_symbol = int(input('Введіть номер символу, з якого починатиметься ключ.\n:'))
            if selected_symbol <= permitted_symbol and selected_symbol >= 0:
                break

    alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    message_code = []

    for i in range(len(encrypted_text)):
        new_char = alphabet.find(encrypted_text[i]) - alphabet.find(key_text[i + permitted_symbol])
        if process_show:
            print('{0} - {1} = {2}'.format(alphabet.find(encrypted_text[i]) + 1,
                                       alphabet.find(key_text[i + permitted_symbol]) + 1, new_char))
        if new_char < 1:
            new_char += 33
            if process_show:
                print('---> {0}'.format(new_char))
        message_code.append(new_char)


    message_text = ''
    for char_code in message_code:
        message_text += alphabet[char_code - 1]

    print('Розшифроване повідомлення: {0}'.format(message_text))
    message_file.write(message_text)

    encrypted_file.close()
    message_file.close()
    key_file.close()


if __name__ == '__main__':
    one_time_pad_code('key_file.txt', 'message_0.txt', 'encrypted_file.txt', False)
    print('=====================================================')
    one_time_pad_decode('key_file.txt', 'message_1.txt', 'encrypted_file.txt', False)