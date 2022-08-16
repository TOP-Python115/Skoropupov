number_1 = float(input('Введите первое число '))


def age(age):
    if age >= 0 and 13 >= age:
        print('Детство')
    elif 24 >= age and age >= 14:
        print('Молодость')
    elif 59 >= age and age >= 25:
        print('Зрелость')
    elif age >= 60:
        print('Старость')
    else:
        print('Некорректный возраст')

age(number)