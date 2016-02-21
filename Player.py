class Player:

    
    #   add new player
    def __init__(self,name,color,cur_balance):     
        self.name = name
        self.color = color.upper()
        self.cur_balance = cur_balance
        if self.color == "BLUE":
            cur_position = (1020,720)
        elif self.color == "RED":
            cur_position = (1060,720)
        elif self.color == "GREEN":
            cur_position = (1020,750)
        elif self.color == "YELLOW":
            cur_position = (1060,750)
        else:
            cur_position = ()

        self.cur_position = cur_position
        self.next_position = self.cur_position
        self.property_owned = []
        self.property_mortgaged = []
        total_rails_owned = 0
        total_utilities_owned = 0,
        self.jail_card = False



    #   move player
    #   update balance
    #   add property
    #   remove property
    #   mortgage property
    #   unmortgage property
    #   set jail card
    #   update position
    #   remove player
    
