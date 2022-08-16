number_1 = float(input('Введите первое число '))
number_2 = float(input('Введите второе число '))


def number_magic(number_1, number_2):
    if number_1 % number_2 == 0:
        print(f"{number_1} делится на {number_2} нацело\nЧастное: {int(number_1 / number_2)}")
    else:
        print(f"{number_1} не делится на {number_2} нацело\nЧастное: {int(number_1 / number_2)}\nОстаток: {number_1 % number_2}")


number_magic(number_1, number_2)