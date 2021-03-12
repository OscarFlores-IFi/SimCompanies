# -*- coding: utf-8 -*-
"""
Spyder Editor

Simulation of production of aerospace BFRs and SORs 
"""

import numpy as np

class Resources(object):
    
    



    bfr
    
    rocket_engine
    
    cockpit
    attitude_control
    
    fuselage
    propellant_tank
    heat_shield
    orbital_booster
    starship

  
    cash = 0 
    water = 0
    seeds = 0 
    grain = 0
    eggs = 0
    buildings = 0 

    water_price = 0.295 
    seeds_price = 0.19
    
    # Considering excess/deficit production as a market price (for buy or sell)
    grain_price = 0.55 if grain < 0 else (0.55 - 0.1*0.358)*0.97
    eggs_price = 1.1 if eggs < 0 else (1.1 - 0.1*0.358)*0.97
    
    
    # Considering excess production as priceless, but deficit as market price: 
    # grain_price = 0.53 if grain < 0 else 0
    # eggs_price = 1.1 if eggs < 0 else 0
    
    
    
    @staticmethod
    def info():
        # resources hourly balance
        print('Cash: {}'.format(Resources.cash))
        print('Water: {}'.format(Resources.water))
        print('Seeds: {}'.format(Resources.seeds)) 
        print('Grain: {}'.format(Resources.grain))
        print('eggs: {}'.format(Resources.eggs))
        print('Buildings value: {}'.format(Resources.buildings))
    
    @staticmethod
    def info_daily():
        # resources daily balance
        print('Cash: {}'.format(Resources.cash * 24))
        print('Water: {}'.format(Resources.water * 24))
        print('Seeds: {}'.format(Resources.seeds * 24)) 
        print('Grain: {}'.format(Resources.grain * 24))
        print('eggs: {}'.format(Resources.eggs * 24))
        print('Buildings value: {}'.format(Resources.buildings))
        
    @classmethod
    def daily_revenue(cls):
        # Total hourly revenue (considering a monetary price for excess in production)
        rev =   cls.cash + \
            cls.water_price*cls.water + \
            cls.seeds_price*cls.seeds + \
            cls.grain_price*cls.grain + \
            cls.eggs_price*cls.eggs
        
        print('Total revenue: ' + str(rev*24 ))
        return(rev*24)
    
    @classmethod
    def daily_Revenue_per_Building_value(cls):
        print('Daily yield revenue: ' + str(cls.daily_revenue()/cls.buildings))


    
aerospace factory 

aerospace electronics

propulsion factory

vertical integration facility

    
class Plantation(object):
    # The plantation produces seeds, grain, apples, ... 
    # For our business model we buy the seeds and produce grain from it. 
    def __init__(self, lvl):
        self.lvl = lvl
        self.grain_production = 825 * lvl
        self.grain_input_resources = [0.5, 1] # [water, seeds]
        self.wages = 104 * admin_overhead * lvl
        self.cost_per_level = 6900
        self.upgrading_cost = self.cost_per_level * lvl
        self.building_value = (np.arange(lvl) * self.cost_per_level).sum()+ \
            self.cost_per_level     
            
        Resources.cash -= self.wages
        Resources.water -= self.grain_input_resources[0] * self.grain_production
        Resources.seeds -= self.grain_input_resources[1] * self.grain_production
        Resources.grain += self.grain_production
        Resources.buildings += self.building_value
        
    
    def info(self):
        print('Plantation lvl: ' + str(self.lvl))
        print('Grain production: ' + str(self.grain_production))
        print('Grain input resources per hour: {} water, {} seeds '.format(
            self.grain_input_resources[0] * self.grain_production,
            self.grain_input_resources[1] * self.grain_production))
        print('Wages: ' + str(self.wages))
        print('Upgrading Cost: ' + str(self.upgrading_cost))   
        print('Building value: '+ str(self.building_value))


class Farm(object):
    # Once we have enough grain (if we do not, we buy it) we produce eggs
    def __init__(self, lvl):
        self.lvl = lvl
        self.eggs_production = 326.26 * lvl
        self.eggs_input_resources = [0.4, 0.5] # [water, grain]
        self.wages = 138  * admin_overhead * lvl
        self.cost_per_level = 10350
        self.upgrading_cost = self.cost_per_level * lvl
        self.building_value = (np.arange(lvl) * self.cost_per_level).sum()+ \
            self.cost_per_level        
        
        Resources.cash -= self.wages
        Resources.water -= self.eggs_input_resources[0] * self.eggs_production
        Resources.grain -= self.eggs_input_resources[1] * self.eggs_production
        Resources.eggs += self.eggs_production
        Resources.buildings += self.building_value
        

    def info(self):
        print('Farm lvl: ' + str(self.lvl))
        print('eggs_production: ' + str(self.eggs_production))
        print('eggs input resources per hour: {} water, {} grain '.format(
            self.eggs_input_resources[0] * self.eggs_production,
            self.eggs_input_resources[1] * self.eggs_production))        
        print('Wages: ' + str(self.wages))
        print('Upgrading Cost: ' + str(self.upgrading_cost))
        print('Building value: '+ str(self.building_value))
        

class Grocery(object):
    # And at last we sell the eggs. 
    def __init__(self, lvl, retail_price, units_sold_per_hour):
        self.eggs_retail_price = retail_price 
        self.lvl = lvl
        self.sales = units_sold_per_hour * lvl
        self.wages = 138 * admin_overhead * lvl
        self.cost_per_level = 10350
        self.upgrading_cost = self.cost_per_level * lvl
        self.building_value = (np.arange(lvl) * self.cost_per_level).sum()+ \
            self.cost_per_level

        Resources.cash += self.sales * self.eggs_retail_price - self.wages
        Resources.eggs -= self.sales
        Resources.buildings += self.building_value
        
        
    def info(self):
        print('Grocery lvl: ' + str(self.lvl))
        print('Sold eggs per hour: ' + str(self.sales))
        print('Wages: ' + str(self.wages))
        print('Sales - wages, per hour: ' + str(self.sales * self.eggs_retail_price - self.wages))
        print('Upgrading Cost: ' + str(self.upgrading_cost))
        print('Building value: '+ str(self.building_value))
     
def print_required_resources():
    print('Daily cash required: ' + str(Resources.cash * 24 +\
    Resources.seeds * Resources.seeds_price * 24 + \
    Resources.water * Resources.water_price * 24))
    

##### 
##### Simulations!
#####

# COO = 0.025 aprox. So it compensates with the admin overhead. the most, the better. 
COO = 0.01
# CMO = 0.03
CMO = 0.01

admin_overhead = 1.295 - COO
        
P1 = Plantation(10)
# P1.info()

F1 = Farm(5)
F2 = Farm(5)
F3 = Farm(5)
F4 = Farm(5)
# F1.info()

### Paso intermedio
print_required_resources()
###

rp, usph = 1.6, 429.08*(1+CMO)
# rp, usph = 6.1, 80 # 

G1 = Grocery(4, rp, usph) # lvl, retail price, units sold per hour (at lvl 1)
G2 = Grocery(4, rp, usph)
G3 = Grocery(4, rp, usph)
G4 = Grocery(4, rp, usph)
G5 = Grocery(4, rp, usph)
# G6 = Grocery(5, rp, usph)
# G1.info()



Resources.info_daily()
Resources.daily_Revenue_per_Building_value()

#####
##### Second simulation!
#####
        


# admin_overhead = 1.17
        
# P1 = Plantation(5)
# # P1.info()

# F1 = Farm(7)
# F2 = Farm(7)
# F3 = Farm(7)
# # F4 = Farm(5)
# # F1.info()

# rp, usph = 6.1, 80 

# G1 = Grocery(6, rp, usph) # lvl, retail price, units sold per hour (at lvl 1)
# G2 = Grocery(6, rp, usph)
# G3 = Grocery(6 ,rp, usph)
# G4 = Grocery(6, rp, usph)
# G5 = Grocery(6, rp, usph)
# G6 = Grocery(5, rp, usph)
# # G1.info()

