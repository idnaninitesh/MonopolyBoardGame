class Card:

    #add a card
    def __init__(self,id_no,name,color,cost,rent,mortgage_value,house_cost,hotel_cost,house_rent,hotel_rent,board_pos,info_pos):
        self.id_no = id_no
        self.name = name
        self.color = color
        self.cost = cost
        self.rent = rent
        self.mortgage_value = mortgage_value
        self.house_cost = house_cost
        self.hotel_cost = hotel_cost
        self.house_rent = house_rent
        self.hotel_rent = hotel_rent
        self.board_pos = board_pos
        self.info_pos = info_pos
        self.status = 0
        self.houses_built = 0
        self.hotel_built = 0



    # update card status
    # add house
    # add hotel
    # remove house
    # remove hotel
