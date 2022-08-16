number_1 = float(input('Введите первое число '))
number_2 = float(input('Введите второе число '))
number_3 = float(input('Введите третье число '))

def neg(number):
    if number <= 0:
        return 0
    else:
        return number


def sum_pos(number_1, number_2, number_3):
    return neg(number_1) + neg(number_2) + neg(number_3)


print(sum_pos(number_1, number_2, number_3))