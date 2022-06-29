# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: {
# "cilpio": 47.999, "a_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.ua": 38.324, "my-store": 37.166,
# "the_partner": 38.988, "sto": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви
# магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною


while True:
    try:
        min_price, max_price = float(input("Введіть мінімальну ціну\n")), float(input("Введіть максимальну ціну\n"))
        if min_price <= 0 or max_price <= 0:
            print('Обидві ціни мусять бути більші нуля, спробуйте ще раз')
        elif max_price <= min_price:
            print('Максимальна ціна мусить бути вищою ніж мінімальна')
        else:
            break
    except ValueError:
        print('Введіть, будь ласка, ціни цифрами')
#
stores_w_prices = {"cilpio": 47.999, "a_studio": 42.999, "momo": 49.999,
                   "main-service": 37.245, "buy.ua": 38.324, "my-store": 37.166,
                   "the_partner": 38.988, "sto": 37.720, "rozetka": 38.003}

suitable_stores = {k: v for k, v in stores_w_prices.items() if min_price <= v <= max_price}

stores_name_list = list(suitable_stores.keys())

stores_name_string = ', '.join(map(str, stores_name_list))

print(f'Магазини з цінами в діапазоні між мінімальною і максимальною вартістю: {stores_name_string}')
