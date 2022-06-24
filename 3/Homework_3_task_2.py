# Вести з консолі строку зі слів (або скористайтеся константою).
# Напишіть код, який визначить кількість кількість слів, в цих даних.
import string

users_text = input("Введіть, будь ласка, декілька слів:\n")

words_number = sum([i.strip(string.punctuation).isalpha() for i in users_text.split()])

print(f'Кількість введених вами слів є {words_number}')