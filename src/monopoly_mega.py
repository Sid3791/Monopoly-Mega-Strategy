from ast import List
from decimal import InvalidContext
import math
import random

# track number of times landed on space
class MonopolyMega():
    BOARD = [
        {"index": 0, "name": "GO", "type": "corner" },
        {"index": 1, "name": "Mediterranean Avenue", "type": "property", "group": "Brown", "cost": 60, "baseRent": 2, "rent1Houses": 10, "rent2Houses": 30, "rent3Houses": 90, "rent4Houses": 160, "rentHotel": 250, "rentSkyscraper": 400 },
        {"index": 2, "name": "Community Chest", "type": "draw" },
        {"index": 3, "name": "Baltic Avenue", "type": "property", "group": "Brown", "cost": 60, "baseRent": 4, "rent1Houses": 20, "rent2Houses": 60, "rent3Houses": 180, "rent4Houses": 320, "rentHotel": 450, "rentSkyscraper": 600 },
        {"index": 4, "name": "Arctic Avenue", "type": "property", "group": "Brown", "cost": 80, "baseRent": 5, "rent1Houses": 25, "rent2Houses": 75, "rent3Houses": 225, "rent4Houses": 375, "rentHotel": 550, "rentSkyscraper": 700 },
        {"index": 5, "name": "Income Tax", "type": "tax", "amount": 200 },
        {"index": 6, "name": "Reading Railroad", "type": "railroad", "cost": 200, "baseRent": 25, "rentDepot": 50 },
        {"index": 7, "name": "Massachusetts Avenue", "type": "property", "group": "Light Blue", "cost": 100, "baseRent": 6, "rent1Houses": 30, "rent2Houses": 90, "rent3Houses": 270, "rent4Houses": 400, "rentHotel": 550, "rentSkyscraper": 700 },
        {"index": 8, "name": "Oriental Avenue", "type": "property", "group": "Light Blue", "cost": 100, "baseRent": 6, "rent1Houses": 30, "rent2Houses": 90, "rent3Houses": 270, "rent4Houses": 400, "rentHotel": 550, "rentSkyscraper": 700 },
        {"index": 9, "name": "Chance", "type": "draw" },
        {"index": 10, "name": "Gas Company", "type": "utility", "cost": 150 },
        {"index": 11, "name": "Vermont Avenue", "type": "property", "group": "Light Blue", "cost": 100, "baseRent": 6, "rent1Houses": 30, "rent2Houses": 90, "rent3Houses": 270, "rent4Houses": 400, "rentHotel": 550, "rentSkyscraper": 700 },
        {"index": 12, "name": "Connecticut Avenue", "type": "property", "group": "Light Blue", "cost": 120, "baseRent": 8, "rent1Houses": 40, "rent2Houses": 100, "rent3Houses": 300, "rent4Houses": 450, "rentHotel": 600, "rentSkyscraper": 750 },
        {"index": 13, "name": "Jail/Just Visiting", "type": "corner" },
        {"index": 14, "name": "Auction", "type": "special" },
        {"index": 15, "name": "Maryland Avenue", "type": "property", "group": "Pink", "cost": 140, "baseRent": 10, "rent1Houses": 50, "rent2Houses": 150, "rent3Houses": 450, "rent4Houses": 625, "rentHotel": 750, "rentSkyscraper": 950 },
        {"index": 16, "name": "St. Charles Place", "type": "property", "group": "Pink", "cost": 140, "baseRent": 10, "rent1Houses": 50, "rent2Houses": 150, "rent3Houses": 450, "rent4Houses": 625, "rentHotel": 750, "rentSkyscraper": 950 },
        {"index": 17, "name": "Electric Company", "type": "utility", "cost": 150 },
        {"index": 18, "name": "States Avenue", "type": "property", "group": "Pink", "cost": 140, "baseRent": 10, "rent1Houses": 50, "rent2Houses": 150, "rent3Houses": 450, "rent4Houses": 625, "rentHotel": 750, "rentSkyscraper": 950 },
        {"index": 19, "name": "Virginia Avenue", "type": "property", "group": "Pink", "cost": 160, "baseRent": 12, "rent1Houses": 60, "rent2Houses": 180, "rent3Houses": 500, "rent4Houses": 700, "rentHotel": 900, "rentSkyscraper": 1100 },
        {"index": 20, "name": "Pennsylvania Railroad", "type": "railroad", "cost": 200, "baseRent": 25, "rentDepot": 50 },
        {"index": 21, "name": "St. James Place", "type": "property", "group": "Orange", "cost": 180, "baseRent": 14, "rent1Houses": 70, "rent2Houses": 200, "rent3Houses": 550, "rent4Houses": 750, "rentHotel": 950, "rentSkyscraper": 1200 },
        {"index": 22, "name": "Community Chest", "type": "draw" },
        {"index": 23, "name": "Tennessee Avenue", "type": "property", "group": "Orange", "cost": 180, "baseRent": 14, "rent1Houses": 70, "rent2Houses": 200, "rent3Houses": 550, "rent4Houses": 750, "rentHotel": 950, "rentSkyscraper": 1200 },
        {"index": 24, "name": "New York Avenue", "type": "property", "group": "Orange", "cost": 200, "baseRent": 16, "rent1Houses": 80, "rent2Houses": 220, "rent3Houses": 600, "rent4Houses": 800, "rentHotel": 1000, "rentSkyscraper": 1300 },
        {"index": 25, "name": "New Jersey Avenue", "type": "property", "group": "Orange", "cost": 200, "baseRent": 16, "rent1Houses": 80, "rent2Houses": 220, "rent3Houses": 600, "rent4Houses": 800, "rentHotel": 1000, "rentSkyscraper": 1300 },
        {"index": 26, "name": "Free Parking", "type": "corner" },
        {"index": 27, "name": "Kentucky Avenue", "type": "property", "group": "Red", "cost": 220, "baseRent": 18, "rent1Houses": 90, "rent2Houses": 250, "rent3Houses": 700, "rent4Houses": 875, "rentHotel": 1050, "rentSkyscraper": 1250 },
        {"index": 28, "name": "Chance", "type": "draw" },
        {"index": 29, "name": "Indiana Avenue", "type": "property", "group": "Red", "cost": 220, "baseRent": 18, "rent1Houses": 90, "rent2Houses": 250, "rent3Houses": 700, "rent4Houses": 875, "rentHotel": 1050, "rentSkyscraper": 1250 },
        {"index": 30, "name": "Illinois Avenue", "type": "property", "group": "Red", "cost": 240, "baseRent": 20, "rent1Houses": 100, "rent2Houses": 300, "rent3Houses": 750, "rent4Houses": 925, "rentHotel": 1100, "rentSkyscraper": 1275 },
        {"index": 31, "name": "Michigan Avenue", "type": "property", "group": "Red", "cost": 240, "baseRent": 20, "rent1Houses": 100, "rent2Houses": 300, "rent3Houses": 750, "rent4Houses": 925, "rentHotel": 1100, "rentSkyscraper": 1275 },
        {"index": 32, "name": "Bus Ticket", "type": "special" },
        {"index": 33, "name": "B. & O. Railroad", "type": "railroad", "cost": 200, "baseRent": 25, "rentDepot": 50 },
        {"index": 34, "name": "Atlantic Avenue", "type": "property", "group": "Yellow", "cost": 260, "baseRent": 22, "rent1Houses": 110, "rent2Houses": 330, "rent3Houses": 800, "rent4Houses": 975, "rentHotel": 1150, "rentSkyscraper": 1400 },
        {"index": 35, "name": "Ventnor Avenue", "type": "property", "group": "Yellow", "cost": 260, "baseRent": 22, "rent1Houses": 110, "rent2Houses": 330, "rent3Houses": 800, "rent4Houses": 975, "rentHotel": 1150, "rentSkyscraper": 1400 },
        {"index": 36, "name": "Water Works", "type": "utility", "cost": 150 },
        {"index": 37, "name": "Marvin Gardens", "type": "property", "group": "Yellow", "cost": 280, "baseRent": 24, "rent1Houses": 120, "rent2Houses": 360, "rent3Houses": 850, "rent4Houses": 1025, "rentHotel": 1200, "rentSkyscraper": 1500 },
        {"index": 38, "name": "California Avenue", "type": "property", "group": "Yellow", "cost": 280, "baseRent": 24, "rent1Houses": 120, "rent2Houses": 360, "rent3Houses": 850, "rent4Houses": 1025, "rentHotel": 1200, "rentSkyscraper": 1500 },
        {"index": 39, "name": "Go To Jail", "type": "corner" },
        {"index": 40, "name": "South Carolina Avenue", "type": "property", "group": "Green", "cost": 300, "baseRent": 26, "rent1Houses": 130, "rent2Houses": 390, "rent3Houses": 900, "rent4Houses": 1100, "rentHotel": 1275, "rentSkyscraper": 1550 },
        {"index": 41, "name": "North Carolina Avenue", "type": "property", "group": "Green", "cost": 300, "baseRent": 26, "rent1Houses": 130, "rent2Houses": 390, "rent3Houses": 900, "rent4Houses": 1100, "rentHotel": 1275, "rentSkyscraper": 1550 },
        {"index": 42, "name": "Community Chest", "type": "draw" },
        {"index": 43, "name": "Pennsylvania Avenue", "type": "property", "group": "Green", "cost": 320, "baseRent": 28, "rent1Houses": 150, "rent2Houses": 450, "rent3Houses": 1000, "rent4Houses": 1200, "rentHotel": 1400, "rentSkyscraper": 1600 },
        {"index": 44, "name": "Short Line", "type": "railroad", "cost": 200, "baseRent": 25, "rentDepot": 50 },
        {"index": 45, "name": "Chance", "type": "draw" },
        {"index": 46, "name": "Birthday Gift", "type": "special" },
        {"index": 47, "name": "Florida Avenue", "type": "property", "group": "Green", "cost": 350, "baseRent": 35, "rent1Houses": 175, "rent2Houses": 500, "rent3Houses": 1100, "rent4Houses": 1300, "rentHotel": 1500, "rentSkyscraper": 2000 },
        {"index": 48, "name": "Park Place", "type": "property", "group": "Dark Blue", "cost": 350, "baseRent": 35, "rent1Houses": 175, "rent2Houses": 500, "rent3Houses": 1100, "rent4Houses": 1300, "rentHotel": 1500, "rentSkyscraper": 2000 },
        {"index": 49, "name": "Luxury Tax", "type": "tax", "amount": 100 },
        {"index": 50, "name": "Boardwalk", "type": "property", "group": "Dark Blue", "cost": 400, "baseRent": 50, "rent1Houses": 200, "rent2Houses": 600, "rent3Houses": 1400, "rent4Houses": 1700, "rentHotel": 2000, "rentSkyscraper": 2500 }
    ]
    
    def __init__(self):
        self.players = List[MonopolyMegaPlayer]
        self.current_player = 0
        self.turn_number = 0
        self.bank_cash = 1e10 
        self.property_owner = {}      
        self.property_state = {}     
        self.chance_deck = []
        self.community_deck = []
        self.game_over = False
        
    def agent_actions(self, agent):
        pass
    
class MonopolyMegaPlayer():
    def __init__(self):
        self.money = 2500
        self.bus_tickets = 0
        # property arrays will be with 
        self.properties = []
        self.current_pos = 0
        self.numJailTurns = -1
        self.getOutOfJailFree = False
        self.isBankrupt = False
        self.totalNetWorth = 0
        self.turnOrder = -1
        
    def get_property_data(self, idx):
        return MonopolyMega.BOARD[idx]
    
    def get_index_prop_data(self, idx):
        for i in range(self.properties):
            if idx == self.properties[i][0]["index"]:
                return i
    
    # two dice rolls to simulate landing odds
    def move_action(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        full_roll = die1 + die2
        
        self.current_pos += full_roll % 52
        
        return self.current_pos
        
    def buy_prop(self, idx):
        self.properties.append([self.get_property_data(idx), 0, False])
        self.money -= self.get_property_data(idx)["cost"]
        
    def mortgage_prop(self, idx):
        self.properties[self.get_index_prop_data(idx)][2] = True
        self.money += self.properties[self.get_index_prop_data(idx)][0]["cost"] // 2
                
    def add_buildings(self, idx, num_buildings):
        self.properties[self.get_index_prop_data(idx)][1] += num_buildings
        self.money -= ((idx // 13) + 1) * 50
                
    def use_jail_card(self):
        if self.getOutOfJailFree:
            self.getOutOfJailFree = False
        else:
            return -1
            
        self.numJailTurns = -1
        return 1
        
    def pay_rent(self, player, idx):
        property_data = self.properties[self.get_index_prop_data(idx)]
        payment = self.properties[self.get_index_prop_data(idx)][0][f"rent{property_data[1]}houses"]
        
        if property_data[2]:
            return 0
                
        if self.money - payment < 0:
            return -1
        
        self.money -= payment
        player.money += payment
        
        return 1
    
    def pay_tax(self):
        if self.money - 100 < 0:
            return -1
        
        self.money -= 100
        
    def declare_bankruptcy(self):
        self.isBankrupt = True
        
    def sell_buildings(self, idx, num_of_buildings):
        self.properties[self.get_index_prop_data(idx)][1] -= num_of_buildings
        self.money += ((idx // 13) + 1) * 50
        
    def unmortgage_prop(self, idx):
        property_data = self.properties[self.get_index_prop_data(idx)]
        price = property_data[0]["cost"] + 0.1 * property_data[0]["cost"] 
        
        if self.money - price < 0:
            return -1
        
        self.money -= price
        self.properties[self.get_index_prop_data(idx)][2] = False
        
    def propose_trade(
        self, 
        player, 
        properties_offered, 
        cash_offered, 
        properties_return, 
        cash_retrun
    ):
        pass
        
    def respond_trade(self, playerf, properties_offered, cash_offered, properties_return, cash_return):
        pass
    
    def determine_num_moves_with_bus_ticket(self):
        return (52 - self.current_pos) % 13
    
    def move_bus_ticket_action(self, num_moves):
        self.current_pos += num_moves
        
#! check if money available for transactions