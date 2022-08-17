from random import shuffle


class Card:
    SUIT_NAMES = ['Трефы', 'Бубны', 'Червы', 'Пики']
    RANK_NAMES = [None, 'Туз', '2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'Валет', 'Дама', 'Король']

    def __init__(self, suil: int, rank: int) -> None:
        self.suit = suil
        self.rank = rank
    
    def __str__(self):
        return f'{Card.RANK_NAMES[self.rank]} масти {Card.SUIT_NAMES[self.suit]}'


class Deck:
    '''Да, я знаю, что можно было относледоваться от листа. Но мне почему-то
    захотелось сделать именно так'''
    def __init__(self):
        self.cards = list()
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        res = list()
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def do_shuffle(self) -> None:
        shuffle(self.cards)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def pop_card(self) -> Card:
        return self.cards.pop()

    def move_cards(self, hand, num: int) -> None:
        for _ in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    def __init__(self, name=''):
        self.cards = list()
        self.name = name
    
    def how_points(self) -> int:
        score = 0
        for card in self.cards:
            score += card.rank
        return score

    def is_lose(self) -> bool:
        return self.how_points() > 21



if __name__ == '__main__':
    flag = True
    while flag:
        deck = Deck()
        deck.do_shuffle()
        hand = Hand()
        while not hand.is_lose():
            deck.move_cards(hand, 1)
            if hand.is_lose():
                print('Вы проиграли', 'Ваши очки', hand.how_points(), sep='\n\n')
                break
            print('Ваши карты:', str(hand), 'Ваши очки:', hand.how_points(), sep='\n',)
            choice = int(input('Хотите взять еще карту? 0 - да, 1 -нет _> '))
            if choice:
                print('Ваше кол-во очков:', hand.how_points(), sep='  ')
                break
        else:
            print('Вы проиграли', 'Ваши очки', hand.how_points(), sep='\n')
        flag = bool(int(input('Хотите сыграть еще? 1 - да, 0 - нет _>')))


