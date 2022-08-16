## pre-scriptum: в Стилях Notepad++ настройте цвет STRINGEOL, чтобы отличать мои комментарии ##, в PyCharm для этого надо редактировать файл цветовой схемы

## ==========  1  ========== ##

class Tetrader:
    def __init__(self, line: float):
        if not self.validation(line):
            ## здесь лучше использовать TypeError
            raise Exception('Это не может быть тетрайдером')
        
        self.line = line
    
    @staticmethod
    # Тут выяснилось, что isinstance(True, (int, float)) вернет True. В каких случаях имеет смысл использовать
    # isinstance() или type() in (кортеж объектов)?
        ## это связано с наследованием: класс bool унаследован от класса int
        ## функция isinstance() проверяет не только указанный(-ые) класс(ы), но и его(их) наследников, а функция type() – только указанный(-ые) класс(ы)
    def validation(line: float) -> bool:
        ## если допускаете float, то допустите и 0 < line <= 1
        return line >= 1 and type(line) in (int, float)
    
    def square(self) -> float:
        return round(3**0.5 * self.line**2, 2)
    
    def volume(self) -> float:
        return round((self.line**3 * 2**0.5) / 12, 2)


tet = Tetrader(100)
print(tet.square())
print(tet.volume())

# 17320.51
# 95724.86



## ==========  2  ========== ##

from datetime import datetime, timedelta

class Moment:
    def __init__(self):
        self.date = datetime.now()

    # Предположу, что у нас 0 часовой пояс и находимся мы в Лондоне
    def moment_in_tz(self, tz: int) -> datetime:
        if tz in range(-12, 13, 1):
            return self.date + timedelta(hours=tz)
        raise ValueError('Часовые пояса от -12, до 12 включительно')

    def time_of_day(self, tz) -> None:
        hours = self.moment_in_tz(tz).hour

        if 0 <= hours < 6:
            print('Ночь')
        elif 6 <= hours < 12:
            print('Утро')
        elif 12 <= hours < 18:
            print('День')
        elif 18 <= hours < 24:
            print('Вечер')
        else:
            ## ValueError
            raise Exception('Случилось невероятное')

    def upd(self) -> None:
        self.date = datetime.now()


happy_moment = Moment()
happy_moment.upd()
happy_moment.time_of_day(2)
# happy_moment.time_of_day(122)

## хорошо!
