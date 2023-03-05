import random
import sys

print("""
     **************************************************    
    ***       ***  **********   ******       **  ***  ***  
    ***   **   **  *********  *  *****  *******  **  ****  
    ***       ***  ********  ***  ****  *******   *******  
    ***   **   **  *******         ***  *******  **  ****  
    ***       ***      **  *******  **       **   ***  **  
     ***************************************************   
        *********************************************
       ****          ***  ********        ***  **  ***
       ********  ******  *  ******  *********  *  ****
       ********  *****  ***  *****  *********    *****
       **  ****  ****         ****  *********  **  ***
       *****   *****  *******  ***        ***  ***  **
        *********************************************
         """)

class Player:
    def __init__(self, name = "", wallet=500):
        self.name = name
        self.wallet = wallet

    def __repr__(self):
        return print(("Welcome to Black Jack ") + self.name + (
                    " You are at table No.1, \n your dealers name is Frank. You have " + str(
                self.wallet) + " chips. Goodluck!"))
    def update_wallet(self,bet = 0,game_results = 0):
        self.wallet = self.wallet - int(bet) + int(game_results)
        if self.wallet <= 0:
            print("Sorry you're all out of chips, please come again.")
            sys.exit()
        print("You have " + str(self.wallet) + " chips remaining.")
    def balance(self):
        return self.wallet


class Cards:
    def __init__(self,player, ready = ""):
        self.player = player
        self.ready = ready
        self.value = []
        self.suits = []
        self.card_total = 0
        self.card_convert = []

    def __repr__(self):
        if len(self.value) == 5:
            print(str(self.player) + " card is a " + str(self.card_convert[4]) + " of " + str(self.suits[4]))
        if len(self.value) == 4:
            print(str(self.player) + " card is a " + str(self.card_convert[3]) + " of " + str(self.suits[3]))
        if len(self.value) == 3:
            print(str(self.player) + " card is a " + str(self.card_convert[2]) + " of " + str(self.suits[2]))
        if len(self.value) == 2:
            print(str(self.player) + " cards are " + str(self.card_convert[0]) + " of "
                  + str(self.suits[0]) + " and " + str(self.card_convert[1]) + " of " + str(self.suits[1]))

    def card_select(self):
        card_dict = {"Hearts":[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11],
                 "Diamonds":[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11],
                 "Spades":[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11],
                 "Clubs":[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]}
        face_cards = [10,"King", "Queen", "Jack"]
        card_set = random.choice(list(card_dict.items()))
        cards = card_set[1]
        card = cards[random.randint(0, 11)]
        suit = card_set[0]

        self.value.append(card)
        self.suits.append(suit)
        if card == 10:
            self.card_convert.append(face_cards[random.randint(0,3)])
        elif card == 11:
            self.card_convert.append("Ace")
        else:
            self.card_convert.append(card)
    def card_sum(self):
        return sum(self.value)

    def card_list(self):
        return self.value

    def restart(self):
        self.value = []
        self.suits = []
        self.card_convert = []





player1 = Player(input("Who is playing today? "))
print(Player.__repr__(player1))
dealer_cards = Cards("The Dealer's")
player_cards = Cards("Your")

def double_down(card_sum):
    if card_sum == 9 or 10 or 11 and input("Would you like to double down? y/n ") == "y":
        bet * 2
    else:
        pass



def game_results(bet):
    game_net = 0
    if player_cards.card_sum() > 21:
        print("You lost....")
        return player1.update_wallet(bet,game_net)
    elif dealer_cards.card_sum() > 21:
        game_net = int(bet) * 1.5
        print("You won!! You collected " + str(int(game_net)) + " chips.")
        return player1.update_wallet(bet, game_net)

    elif dealer_cards.card_sum() - 21 == player_cards.card_sum() - 21:
        print("Its a tie! The Dealer returns the chips you bet")
        return player1.update_wallet(bet,bet)
    elif dealer_cards.card_sum() - 21 > player_cards.card_sum() - 21:
        print("You lost....")
        return player1.update_wallet(bet,game_net)
    elif dealer_cards.card_sum() - 21 < player_cards.card_sum() - 21:
        game_net = int(bet) * 1.5
        print("You won!! You collected " + str(int(game_net)) + " chips.")
        return player1.update_wallet(bet, game_net)
    else:
        pass



for game in range(0, 999):
    init = input("***** Dealer Shuffling ***** \n Would you like to continue? y/n ")
    bet = 0
    game_end = ""
    player_cards.restart()
    dealer_cards.restart()

    if init == "y":
        bet = input("Place your bet: ")
    else:
        print("We hope you enjoyed your time here!")
        break
    for i in range(0,10):
        try:
            int(bet)
            break
        except:
            print("Sorry not a valid bet please input integer")
            bet = input("Place your bet: ")

    for i in range(0,10):
        if int(bet) > player1.balance():
            print("Sorry you only have " + str(player1.balance()) + " chips.")
            bet = input("Please input valid bet. ")

        else:
            player_cards.card_select()
            player_cards.card_select()
            dealer_cards.card_select()
            dealer_cards.card_select()
            Cards.__repr__(player_cards)
            Cards.__repr__(dealer_cards)
            break

    double_down(player_cards.card_sum())

    for i in range(0, 4):
        if player_cards.card_sum() > 21:
            print("You busted....")
            break
        elif dealer_cards.card_sum() > 21:
            print("The dealer busted!")
            break

        draw = input("Would you like to draw another card? y/n ")

        while dealer_cards.card_sum() < 17:
            dealer_cards.card_select()
            Cards.__repr__(dealer_cards)
        if draw == "y":
            player_cards.card_select()
            Cards.__repr__(player_cards)
        elif draw == "n":
            print("***** Stand *****")
            break
        else:
            break
    if player1.balance() <= 0:
        print("Sorry you ran out of chips, please come again!")
        break
    game_results(bet)



# Blackjack parameters for consideration
# player wins are paid out 1.5x the bet
# dealer must hit until value above 17
# splitting: player may play two separate hands if initial cards are the same denomination
# double down: if card value = 9,10,11 they may double their bet but only get one card
# when a player hits a total of 5 times they automatically win with a payout equal to bet
# consider house payout limit to win game
