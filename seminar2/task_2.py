#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
#строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))
result: str = ''
BASE_HEX = 16

temp_num = num
while temp_num:
    remainder_division = temp_num % BASE_HEX
    match remainder_division:
        case 10:
            result = 'a' + result
        case 11:
            result = 'b' + result
        case 12:
            result = 'c' + result
        case 13:
            result = 'd' + result
        case 14:
            result = 'e' + result
        case 15:
            result = 'f' + result
        case _:
            result = str(remainder_division) + result
    temp_num = temp_num // BASE_HEX

print(f'число {num} в {BASE_HEX} системе исчисления: 0x{result}')
print(f'Проверка: {hex(num)}')
