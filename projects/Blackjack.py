import random, os

deck = []
player_cards = []
dealer_cards =[]

def create_deck():
    '''Creates Dec of 52 Playing Cards'''
    cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    suites = ['♠','♥','♦','♣']
    for card in cards:
        for suite in range(len(suites)):
            deck.append((card, suites[suite]))


def first_deal(player):
    while len(player) < 2:
        card = random.choice(deck)
        player.append(card)
    
    if player == dealer_cards:
        print(f'Dealer Cards:\n{player[0][0]}{player[0][1]}\n')
    else:
        print(f'\nYour Cards:')
        for card in player:
            print(f'{card[0]}{card[1]}')
        print('\n')
    
    

def deal_card(player):
        card = random.choice(deck)
        player.append(card)
        for card in player:
            print(f'{card[0]}{card[1]}')
        print('\n')

def play_game():

    os.system('clear')
    player_score = 0
    dealer_score = 0
    play = True

    def calc_total(player):
        total = 0

        for card in player:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                total += 10
            elif card[0] == 'A':
                if total <= 10:
                    total += 11
                else:
                    total += 1
            else:
                total += card[0]
        return total


    create_deck()
    first_deal(player_cards)
    first_deal(dealer_cards)
    player_score += calc_total(player_cards)
    dealer_score += calc_total(dealer_cards)
        
    #Debug Player Score
    # print(f'Dealer Score: {dealer_score}')

    while play:
        player_score = calc_total(player_cards)
        print(f'Player Score: {player_score}')
        action = input('hit | hold\n> ').upper()
        if player_score == 21:
            print('Blackjack!')
        else:
            if action == 'HIT':
                deal_card(player_cards)
                player_score = calc_total(player_cards)
                if player_score == 21:
                    print('Blackjack!')
                    play = False
                elif player_score > 21:
                    print(f'Bust! {player_score}')
                    print('The dealer wims!')
                    play = False
            elif action == 'HOLD':
                play = False
                print(f'Player Score: {player_score}')


                if dealer_score < 17:
                    deal_card(dealer_cards)
                    dealer_score = calc_total(dealer_cards)
                    print(f'Dealer Score: {dealer_score}')
                
                if dealer_score == player_score:
                    print('It\'s a Draw!')
                elif dealer_score > player_score:

                    if dealer_score <= 21:
                        
                        print('The Dealer Won!')
                    else:
                        print('You Won!')
                else:
                    print(f'Dealer Score: {dealer_score}')
                    print('You Won!')

    
play_game()