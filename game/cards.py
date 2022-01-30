import random

class Cards():
    total_score=300
    def __init__(self):
        #The player starts the game with 300 points.( -Augusto-)
        #This is the magic Score: )        
        self.isDisplayedNextNumber=True
        #self.next_number=0
        self.lose_points= 75
        self.earn_points=100
        self.previous_number = 0
        self.current_number = 0
        #self.prev_number=0
        self.num=0
        self.f=0
        self.j=0
    
    def get_card_num(self):       
        self.number = random.randint(1, 13)
        return self.number 
    
    def player_choice(self):
        #change the state of isDisplayedNextNumber once when self.current_number
        # is outputed, this block occurs only the firs time.
        if self.isDisplayedNextNumber:
            self.previous_number=self.get_card_num()
            self.num=self.current_number=self.get_card_num()
            print("The card is: ", self.previous_number)
            opt = input("Higher/Lower [h / l] :")
            print("Next Card is :", self.current_number)
            self.isDisplayedNextNumber = False
            if  self.current_number > self.previous_number and opt == "h":
                self.total_score += self.earn_points
                print("You win!")
                print("Your Score is: ", self.total_score)
            elif  self.current_number > self.previous_number and opt == "l":
                self.total_score -= self.lose_points
                print("You lose!")
                print("Your Score is: ", self.total_score) 
            elif  self.current_number < self.previous_number and opt == "l":
                self.total_score += self.earn_points
                self.total_score=self.total_score
                print("You win!")
                print("Your Score is: ", self.total_score)
            elif  self.current_number < self.previous_number and opt == "h":
                self.total_score -= self.lose_points
                print("You lose!")
                print("Your Score is: ", self.total_score)
            else:
                print("Your Score is: ", self.total_score)               
        else:
            self.j = self.num
            print("The card is: ", self.num)
            opt = input("Higher/Lower [h / l] :")
            self.num = self.get_card_num()
            self.f  = self.num
            print("Next Card is :", self.num)
            if  self.num > self.j and opt == "l":
                self.total_score -= self.lose_points
                print("You loose!")
                print("Your Score is: ", self.total_score)
            elif  self.num < self.j and opt == "h":
                self.total_score -= self.lose_points
                print("You lose!")
                print("Your Score is: ", self.total_score)
            elif  self.num > self.j and opt == "h":
                self.total_score += self.earn_points
                self.total_score=self.total_score
                print("You win!")
                print("Your Score is: ", self.total_score)
            elif  self.num < self.j and opt == "l":
                self.total_score += self.earn_points
                print("You win!")
                print("Your Score is: ", self.total_score)    
            else:
                print("Your Score is: ", self.total_score)      
            
           
    def recursion(self):
        print("---------------------------------------")
        self.player_choice()
        if self.total_score <= 0:
            print("The game is over.")
            print("Thank you and came back soon!")
            print("---------------------------------------")
            exit()
        else:
            p = input("Do want to play? [y/n] ")          
            if p.lower() != "n":
                #loop gaming if the user select any key#
                print("---------------------------------------")
                self.recursion()
                print("Despues de recursion por las porcias.")
            else:
                #game ends if user selected n key.#
                print("The game is over.")
                print("Thank you and came back soon!")
                print("---------------------------------------")
                exit()

card = Cards()
