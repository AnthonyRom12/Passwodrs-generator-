import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
quantity = int(input('Enter quantity of passwords: '))
len_pass = int(input('Enter the length of password: '))
stroka_upp = input('Do you want to include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? (yes/no) ')
stroka_low = input('Do you want to include lowercase letters abcdefghijklmnopqrstuvwxyz? (yes/no) ')
stroka_sym = input('Do you want to include symbols !#$%&*+-=?@^_? (yes/no) ')
del_sym = input('Whether to exclude ambiguous characters il1Lo0O? (yes/no) ')
if stroka_upp == 'yes':
    chars += uppercase_letters
if stroka_low == 'yes':
    chars += lowercase_letters
if stroka_sym == 'yes':
    chars += punctuation
if del_sym == 'yes':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(len,chars):
    pswrd = ''
    for _ in range(quantity):
        for _ in range(len_pass):
            pswrd += random.choice(chars)
        pswrd += ' '
    return pswrd

print(generate_password(len, chars))

