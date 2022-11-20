from src.ASCII import ascii_dictionary
import string

def is_bin(num):
    for letter in num: 
        if(letter != '1' and letter != '0'):
            return False
    return True

def is_hex(num):
    if(num.isdigit() and int(num) > 9): return False
    hex_digits = set(string.hexdigits)
    return all(c in hex_digits for c in num)

def get_dec_from_bin(num):
    arr = []
    dec = ''
    print(len(num))
    for i in range(1, len(num)+1):
        dec += num[i-1]
        if(i % 8 == 0 and i != 0):
            print("Двоичная: ", dec)
            print("Длина: ", len(dec))
            dec = int(dec, 2)
            arr.append(dec)
            dec = ''
    print(arr)
    return arr

def get_dec_from_hex(num):
    arr = []
    dec = ''
    print(len(num))
    for i in range(1, len(num)+1):
        dec += num[i-1]
        if(i % 2 == 0 and i != 0):
            print("Шестнадцетеричная: ", dec)
            print("Длина: ", len(dec))
            dec = int(dec, 16)
            arr.append(dec)
            dec = ''
    print(arr)
    return arr

def get_descipted_binary_code(num, base):
    arr = []
    if(base == 16):
        arr = get_dec_from_hex(num)
    else:
        arr = get_dec_from_bin(num)


    word = ''
    for i in range(len(arr)):
        try:
            word+=ascii_dictionary.get(str(arr[i]))
        except:
            word+=f"\nОшибка! Не обнаружено буквы в словаре!\nНенайденное значение: {arr[i]}\n"
    word += f"\nПолученные числа: {arr}"
    return word