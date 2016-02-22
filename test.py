class Player:

    
    #   add new player
    def __init__(self,name,color,cur_balance,cur_position):     
        self.name = name
        self.color = color.upper()
        self.cur_balance = cur_balance
        self.cur_position = cur_position
        self.next_position = cur_position
        self.property_owned = []
        self.property_mortgaged = []
        self.jail_card = False


    def temp(self):
        self.jail_card = True




player = Player(name = "nitesh",color = "Red",cur_balance = 1000,cur_position = (0,0))
print(player.name)
print(player.color)
print(player.cur_balance)
print(player.cur_position)
player.temp()
print(player.jail_card)
