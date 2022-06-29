# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.


import re


user_string = input("Введіть, будь ласка, строку на ваш вибір:\n")

words_with_many_vowels = [x for x in user_string.split() if re.search(r'[aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ]{2}', x)]

print(f"Кількість слів з двома голосними літерами підряд у введеній вами строці: {len(words_with_many_vowels)}")
