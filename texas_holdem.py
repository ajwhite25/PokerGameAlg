""" 
            Project: Texas Hold'Em Algorithm
Team Members:                   Course: Intro To Algorithms S25
    Amiya White                 
    Jayla Henry                 
    Joanna Lopez                 Date: April 29, 2025
"""
from collections import OrderedDict
import math

max_size = 7
current_deal =OrderedDict(max_size=max_size)
amount = 100
pot=0

class TexasHoldEm:
    #money starts at 100 and resets and 
    current_phase = ""
    opponent_action=""
    
    hand_ranking = []
    suite = []
    faces = []
    current_deal =[] # should not exceed 7! this is what we are examining and making comparisons in everything 

    def __init__(self):
        self.current_phase = ""
        self.opponent_action=""
        
        #Ordered in order of winning ranks!
        self.hand_ranking = {'Royal Flush','Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pairs', 'Pair', 'High Card'}
        self.number = ['A', 'Q', 'K', 'J', '10', '9', '8','7', '6', '5', '4', '3', '2', '1']
        self.symbol = ['s','c','h','d']

    def bet(self):
        #all in never !
        # DO joanna
        #all in never !  
        # get the betting phase from input
        # if we are in the hole cards phase we just add the hole cards to our current_deal array
        # and call 0 unless first better is not us then we match
        # if current_phase == "Hole Cards":
        #     return call_check()

        # elif current_phase == "Flop":

        # elif current_phase == "Turn":

        # else: 
        pass

    def call(self):
        #all operations will be called within call
        #call everytime until first 3 cards come out!
        # if low two pairs just call
        # DO joanna
        pass

    def fold(self):
        #never fold? unless 4th card down/ turn 
        #example: if in turn phase, and if no hand_ranking matched by now, FOLD
        print("Fold. We Lose.")
        exit()
        pass

    def raise_act(self, highest_bid, amount):
        high_rank_cards = ["A", "K", "Q", "J", "10", "9"]
        #creates array to compare with high rank cards
        rank = []
        for card in faces:
            if card == True:
                rank.append(card)
        #rank duplicate counter
        #source
        #https://www.geeksforgeeks.org/find-duplicates-given-array-elements-not-limited-range/?ref=rp
        def findDups(arr):
            res = []
            for i in range(len(arr) - 1):
                for j in range(i + 1, len(arr)):
                    if arr[i] == arr[j]:
                        if arr[i] not in  res:
                            res.append(arr[i])
                        break
            return res
            #checks if face is high rank
        if rank in high_rank_cards:
                #check if faces are the same
            common_elements = findDups(rank)
            if common_elements in high_rank_cards:
                #minimum raise
                total_raise = highest_bid + 10
                if (total_raise <= amount):
                    print("We Raise The Bet To", total_raise)
                else:
                    print("Cant Raise. Not Enough Money")
            else:
                    print("Faces Are Not The Same")
        else:
                print("Cards Are Not High Cards")
        #raise 10 only if 
        #raise anytime we have 2 of same faces (Q, K, A, J, 10)
        #minimum, for first hand until house shows cards then rraise
        #raise if two pairs of high cards. so 9< ?

    def set_betting_phases(self, phase):
        self.current_phase = phase

    def set_opponent_action(self, action):
        self.opponent_action = action
         

#all in if suites match! can get flush (this is a hand ranking)
     

def main():
    #continuous while and conditionals that check each of our class methods. following the rules
    print("Welcome to Texas Hold 'Em!")
    start = input("Are you ready to begin the game?(y/n) ")
    
    if(start== 'n'):
        print("Exiting Games")
        exit()

    if(start=='y'):
        print("Enter starting cards: ")
        
        for c in range (0,2):
            number = input(f"{c}: Number on card: (A,Q,J,K,10-2) ")
            symbol = input(f"{c}: Symbol on card: (s,d,h,c) ")
            current_deal[number] = symbol

        game = TexasHoldEm()
        game.get_betting_phases = 1
        turn= input("Who is going first? (i/u)")

        while True:
            # Played 0: i, PLayed 1: u
            played = [False, False]

            while not (played[0] and played[1]):
                if(turn =='u') and not played[1]:
                    oppponent_action = input("What did the opponent do? ") 
                    game.set_opponent_action(oppponent_action)
                    played[1] = True

                    if(oppponent_action=='raised'):
                        pot = int(input("How much? "))
                    #if they fold we automatically win.\
                    elif(oppponent_action =='fold'):
                        print(f"I WIN!\n Money Remaining: {amount}. \n\n")
                        exit()
                    
                    # My game is taken next.
                    turn = 'i'

                elif(turn =='i') and not played[0]:
                    action = game.bet()
                    print(action)
                    played[0]= True
                    turn='u'

            new_phase=input("Next Phase? (2,3,4, 0-skip) ")

            match new_phase:
                case '0':
                    break
                case '2':
                    # The Flop
                    game.set_betting_phases(new_phase)
                    for c in range (0,3):
                        number = input(f"{c}: Number on card: (A,Q,J,K,10-2) ")
                        symbol = input(f"{c}: Symbol on card: (s,d,h,c) ")
                        current_deal[number] = symbol
                    break
                
                case '3':
                    game.set_betting_phases(new_phase)
                    # The Turn
                    #fold on turn phase IF we don't see anything we can handle (in array in the phase class)
                    current_deal[input(f"{c}: Number on card: (A,Q,J,K,10-2) ")] = input(f"{c}: Symbol on card: (s,d,h,c) ")
                    break

                case '4':
                    game.set_betting_phases(new_phase)
                    #The River
                    #Closing!
                    current_deal[input(f"{c}: Number on card: (A,Q,J,K,10-2) ")] = input(f"{c}: Symbol on card: (s,d,h,c) ")
                    #outputs--  tell them what action and by how much. 
        
            # reminder, call everytime until house puts card down
            # raise if and anytime we get two high cards
if __name__ == "__main__":
            main()