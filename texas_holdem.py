import random
import math

class TexasHoldEm:
    #money starts at 100 and resets and 
    current_phase = ""
    opponent_action=""
    
    hand_ranking = []
    suits = []
    faces = []
    current_deal =[] # should not exceed 7! this is what we are examining and making comparisons in everything 

    def bet():
<<<<<<< HEAD
        #all in never !  
=======
        #all in never !
        # DO joanna
>>>>>>> refs/remotes/origin/main
        pass

    def call_check():
        #all operations will be called within call
        #call everytime until first 3 cards come out!
        # if low two pairs just call
        # DO joanna
        pass

    def fold():
        #never fold? unless 4th card down/ turn 
        #example: if in turn phase, and if no hand_ranking matched by now, FOLD
        print("Fold. We Lose.")
        exit()
        pass

    def raise_act(faces, highest_bid, amount):
        high_rank_cards = ["A", "K", "Q", "J", "10", "9"]
        rank = []
        for card in faces:
            if card = True:
                rank.append(card)
            #checks if face is high rank
            if rank in high_rank_cards:
                #check if faces are the same
                if :
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

        pass

    def get_betting_phases():
         pass
    def set_betting_phases():
         pass
    
    def get_opponent_action():
         pass
    def set_opponent_action():
         pass

#all in if suites match! can get flush (this is a hand ranking)
     

def main():
    #continuous while and conditionals that check each of our class methods. following the rules
    print("Welcome to Texas Hold 'Em!")
    suite = input("Card Suite: ")
    faces = input("Faces: ")
<<<<<<< HEAD
    amount = 100
=======
    current_phase = input("Enter current phase. ")
    oppponent_action = input("What did the opponent do? ") #if they fold we automatically win.

    #outputs--  tell them what action and by how much. 
>>>>>>> refs/remotes/origin/main

    ## take phases as input with suite and number. 


    # reminder, call everytime until house puts call down
    # raise if and anytime we get two high cards
    #fold on turn phase IF we don't see anything we can handle (in array in the phase class)

    #array size does not exceed 7

if __name__ == "__main__":
        main()