# 1. Зформуйте строку, яка містить певну інформацію про символ в відомому слові. Наприклад "The [номер символу]
# symbol in [тут слово] is '[символ з відповідним порядковим номером]'". Слово та номер отримайте за допомогою input(
# ) або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't'
# ".


while True:
    word = input("Введіть, будь ласка, слово:\n")
    if word.isalpha():
        break
    else:
        print("Слово мусить містити лише букви")

while True:
    try:
        symbol_number = int(input("Введіть порядковий номер символу:\n"))
        if symbol_number > len(word) or symbol_number <= 0:
            print('Введений порядковий номер є поза межами слова')
        else:
            break
    except ValueError:
        print('Введіть, будь ласка, порядковий номер цифрою')

searched_symbol = word[symbol_number - 1]

print(f'The {symbol_number} symbol in "{word}" is "{searched_symbol}"')

