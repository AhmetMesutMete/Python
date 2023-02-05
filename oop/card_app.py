### Card Class

# Each object derived from the card class will represent a card type.
# Card class will have 2 instance properties named type and value
# The instance method of the card class named fetch_card() will print the card information
# __repr__ method will be used to print card information
import random
class Card:
    '''
        Instance Attributes
            -type, value
        Instance Methods
            -fetch_card()
    '''
    def __init__(self, card_type, card_value):
        self.card_type = card_type
        self.card_value = card_value

    # def fetch_card(self):
    #     '''Displays card information'''
    #     print(f'Card Type: {self.card_type}, Card Value: {self.card_value}')

    def __repr__(self):
        return f'{self.card_value} of {self.card_type}'

# c1 = Card('diamonds', 5)
# c1.fetch_card()
# print(c1)

### Deck Class

class Deck:
    '''
        Instance Methods
            -remaining_cards()
            -shuffle_cards()
            -deal_card()
            -throw_card()
    '''
    card_types = ['clubs (♣)','diamonds (♦)','hearts (♥)','spades (♠)']
    card_values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    def __init__(self):
        self.card_list = [Card(t, v) for t in Deck.card_types for v in Deck.card_values]
        # print(self.card_list)

    def remaining_cards(self):
        '''Returns the number of remaining cards'''
        return len(self.card_list)

    def shuffle_cards(self):
        '''Shuffles cards'''
        if self.remaining_cards() < 52:
            raise ValueError('You can only shuffle the cards at the beginning.')
        random.shuffle(self.card_list)
        # print(self.card_list)

    def deal_card(self, num):
        '''deals the number of requested cards'''
        rem_cards = self.remaining_cards()
        if rem_cards == 0:
            raise ValueError('All cards dealt.')
        num = min(rem_cards, int(num))
        cards = random.sample(self.card_list, num)
        for i in cards:
            self.card_list.remove(i)
        return cards

    def throw_card(self):
        '''throws one card from the hand'''
        return self.deal_card(1)[0]


d1 = Deck()
d1.shuffle_cards()
d1.deal_card(52)
print(d1.throw_card())

# d2 = Deck()
# d2.shuffle_cards()
