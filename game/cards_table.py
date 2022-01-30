from game.cards import Cards


class Cards_table:    

    def __init__(self):
        self.is_playing=True
        
        #startgame module Initialize the game.
        while self.is_playing:
                                            
            #card.player_choice look for the choice of the player.
            card = Cards()    
            card.recursion()
