""" 
            Project: Texas Hold'Em Algorithm
Team Members:                   Course: Intro To Algorithms S25
    Amiya White                 
    Jayla Henry                 
    Joanna Lopez                 Date: April 29, 2025
"""
import random
played = [False, False]

class TexasHoldEm:
    #money starts at 100 and resets and 
    # should not exceed 7! this is what we are examining and making comparisons in everything 

    def __init__(self):
        self.current_deal = []
        self.current_phase = ""
        self.opponent_action = ""
        self.opponent_bet = 0
        self.total = 100
        self.pot = 0
        self.moves = 0


        # ordered in order of winning ranks
        self.hand_ranking = {
            'Royal Flush': 10,
            'Straight Flush' : 9,
            'Four of a Kind': 8,
            'Full House': 7,
            'Flush': 6,
            'Straight': 5,
            'Three of a Kind': 4,
            'Two Pairs': 3,
            'Pair': 2,
            'High Card': 1
        }
        self.number = ['A', 'Q', 'K', 'J', '10', '9', '8','7','6','5','4','3','2']
        self.symbol = ['s', 'c','h','d']

    def bet(self):
        #all in never!
        # get the betting phase from input
        # if we are in the hole cards phase we just add the hole cards to our current_deal array
        # and call 0 unless first better is not us then we match

        # key is number & value is symbol
        nums = [card[0] for card in self.current_deal]
        high_cards = {"A", "K", "Q", "J", "10"}

        # counts how many cards in our current deal
        high_card_count = sum(1 for number in nums if number in high_cards)

        # checks if there's a pair in current deal 
        # set function picks out the duplicates in a list
        pair_found = len(nums) != len(set(nums))

        if self.current_phase == '1':
            if (self.moves == 0 and not played[1]):
                # bet_amount = intself.raise_act(self.current_deal, self.opponent_bet, self.total)
                # self.pot += bet_amount
                self.raise_act(self.current_deal, self.opponent_bet)
                #print(f"Remaining Amount: {self.total}.\n Pot is now {self.pot}.\n")
            else:
                self.pot += self.call()

        elif self.current_phase == '3':
            if (not pair_found and high_card_count == 0):
                self.fold()
            elif pair_found and high_card_count > 0:
                self.raise_act(self.current_deal, self.opponent_bet)
                #print(f"Remaining Amount: {self.total}.\n Pot is now {self.pot}.\n")
            else:
                self.pot += self.call()
                print(f"Remaining Amount: {self.total}.\n Pot is now {self.pot}.\n")
        else:
            self.pot += self.call()
            
    
        # increment the moves after the player has acted
        self.moves += 1

    def call(self):
        #all operations will be called within call
        #call everytime until first 3 cards come out!
        # if we don't have enough to match we fold
        if self.opponent_bet > self.total:
            print(f"Not enough to call. We fold.\n")
            self.fold()
        else:
            # if we do have enough --> we subtract what they bet from our total to match
            # and we add it to the pot
            # print out our bet
            self.total -= self.opponent_bet
            self.pot += self.opponent_bet
            print(f"We call {self.opponent_bet}. \n Remaining Amount: {self.total}.\n Pot is now {self.pot}.\n")
            # since we are matching we just return what they bet
            return self.opponent_bet
    
    # helper function
    def classify_rank(self):
        pass

    def fold(self):
        #never fold? unless 4th card down/ turn 
        #example: if in turn phase, and if no hand_ranking matched by now, FOLD
        print("Fold. Game Over.")
        exit()


    def raise_act(self, current_deal, opponent_bet):
        #creates array to compare with high rank cards
        #creates array to compare with high rank cards
        high_rank_cards = ["A", "K", "Q", "J", "10", "9", "8"]
        high_rank_count = sum(1 for card in current_deal if card in high_rank_cards)
        #pair
        if high_rank_count == 2:
            total_raise = opponent_bet + 7
            if total_raise <= self.total:
                self.total -= total_raise
                self.pot += total_raise
                print("We Raise The Bet BY", total_raise)
                print(f"Remaining Amount: {self.total}.\n Pot is now {self.pot}.\n")
                return total_raise

        #three of a kind & four of a kind
        elif high_rank_count >= 3:
            total_raise = opponent_bet + 10
            if total_raise <= self.total:
                self.total -= total_raise
                self.pot += total_raise
                print("We Raise The Bet BY", total_raise)
                print(f"Remaining Amount: {self.total}.\n Pot is now {self.pot}.\n")
                return total_raise

        #bluff
        bluff_probability = 0.1
        total_bluff_raise = 0
        if random.random() < bluff_probability:
            total_bluff_raise = opponent_bet + 3
            if total_bluff_raise <= self.total:
                self.pot += total_bluff_raise
                self.total -= total_bluff_raise
        else:
            total_bluff_raise += 5
            self.pot += total_bluff_raise
            self.total -= total_bluff_raise           
        #print("Raising The Bet To", total_bluff_raise)
        print(f"Remaining Amount: {self.total}.\n Pot is now {self.pot}.\n")
        return total_bluff_raise
                
        #raise 10 only if 
        #raise anytime we have 2 of same faces (Q, K, A, J, 10)
        #minimum, for first hand until house shows cards then rraise
        #raise if two pairs of high cards. so 9< ?

    def set_betting_phases(self, phase):
        self.current_phase = phase
    
    def get_betting_phases(self):
        return self.current_phase

    def set_opponent_action(self, action):
        self.opponent_action = action

#all in if suites match! can get flush (this is a hand ranking)

def main():
    #continuous while and conditionals that check each of our class methods. following the rules
    print("Welcome to Texas Hold 'Em!")
    start = input("Are you ready to begin the game?(y/n) ").lower()
    state = True
    if(start== 'n'):
        print("Exiting Game")
        exit()

    
    game = TexasHoldEm()
    game.set_betting_phases('1')
    print("Enter starting cards: ")
    
    for c in range (0,2):
        number = input(f"{c}: Number on card: (A,Q,J,K,10-2) ").upper()
        symbol = input(f"{c}: Symbol on card: (s,d,h,c) ").lower()
        game.current_deal.append((number, symbol))

    turn = input("Who is going first? (i/u)").lower()
    
    # initial betting round
    #turn = play_betting_round(game, turn)

    while (state):
        # Played 0: i, PLayed 1: u

        while not (played[0] and played[1]):

            if (turn == 'u' and not played[1]):
                opponent_action = input("What did the opponent do? (fold, call, raise) ").lower()
                game.set_opponent_action(opponent_action)
                played[1] = True

                if opponent_action == 'raise':
                    game.opponent_bet = int(input("How much? "))
                    game.pot += game.opponent_bet
                    game.bet()
                    if game.opponent_action == 'fold':
                        return 'i'
                elif opponent_action == 'fold':
                    game.total += game.pot
                    print(f"I WIN!\n Money Earned: {game.total}. \n\n")
                    exit()
                
                elif opponent_action == 'call':
                    game.opponent_bet = int(input("How much?"))
                    game.pot += game.opponent_bet
                    game.bet()
                    turn = 'i'

                turn = 'i'
            

            elif turn =='i' and not played[0]:
                game.bet()
                played[0]= True
                turn='u'

        played[0]= False
        played[1] = False
        new_phase = input("Next Phase? (2-Flop, 3-Turn, 4-River, 0-Skips) ").lower()

        match new_phase:
            case '0':
                continue
            case '2':
                # The Flop
                game.set_betting_phases(new_phase)
                print("\nFlop:")
                for c in range (0,3):
                    number = input(f"{c}: Number on card: (A,Q,J,K,10-2) ").upper()
                    symbol = input(f"{c}: Symbol on card: (s,d,h,c) ").lower()
                    game.current_deal.append((number, symbol))
                continue
            case '3':
                game.set_betting_phases(new_phase)
                # The Turn
                #fold on turn phase IF we don't see anything we can handle (in array in the phase class)
                number = input(f"{c}: Number on card: (A,Q,J,K,10-2) ").upper()
                symbol = input(f"{c}: Symbol on card: (s,d,h,c) ").lower()
                game.current_deal.append((number, symbol))
                continue

            case '4':
                game.set_betting_phases(new_phase)
                #The River
                print("\nRiver:")
                number = input(f"{c}: Number on card: (A,Q,J,K,10-2) ").upper()
                symbol = input(f"{c}: Symbol on card: (s,d,h,c) ").lower()
                #outputs--  tell them what action and by how much. 
                game.current_deal.append((number, symbol))
                print(game.current_deal)
                print("We call zero! NO more money added as we finish")
                print(f"GAME OVER! (you decide who wins) ;)")
                state = False

            
                # reminder, call everytime until house puts card down
                # raise if and anytime we get two high cards

if __name__ == "__main__":
    main()