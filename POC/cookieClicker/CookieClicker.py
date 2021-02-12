"""
Cookie Clicker Simulator
"""

#import simpleplot

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)
import math
import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._cookies = float(0)
        self._total_cookies = float(0)
        self._cps = float(1)
        self._time = float(0)
        self._history=[(0.0,None,0.0,0.0)]

        
    def __str__(self):
        """
        Return human readable state
        """
        result = ('\n Time: ' + str(self._time) + 
        '\n Current Cookies: ' + str(self._cookies) + 
        '\n CPS: ' + str(self._cps) + 
        '\n Total Cookies: ' + str(self._total_cookies))
        return result
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """

        return float(self._cookies)
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return float(self._cps)
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return float(self._time)
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies <= self._cookies:
            result = 0.0
        else:
            cookies_to_earn = cookies - self._cookies
            result = cookies_to_earn / self._cps
        return float(math.ceil(result))
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._cookies += self._cps * time
            self._total_cookies += self._cps * time
            self._time += time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self._cookies:
            self._cookies -= cost
            self._cps += additional_cps
            self._history.append((self._time,item_name,cost,self._total_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    shop = build_info.clone()
    game = ClickerState()
    while game.get_time()<= duration:
        purchase_next = strategy(game.get_cookies(),game.get_cps(),game.get_history(),duration-game.get_time(),shop.clone())
        if purchase_next == None:
            break
        if game.get_cookies() < shop.get_cost(purchase_next):
            if game.time_until(shop.get_cost(purchase_next)) > duration - game.get_time():
                break
            game.wait(game.time_until(shop.get_cost(purchase_next)))
        game.buy_item(purchase_next,shop.get_cost(purchase_next),shop.get_cps(purchase_next))
        shop.update_item(purchase_next)
    if game.get_time() < duration:
        game.wait(duration - game.get_time())
    return game


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """

    return "Cursor"
def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None
        

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    shop = build_info.clone()
    #find the smallest number for build
    lowest_price_list = []
    for item in shop.build_items():
        lowest_price_list.append(shop.get_cost(item))
    lowest_price_list = sorted(lowest_price_list)
    # return the item that matches that price
    for item in shop.build_items():
        if shop.get_cost(item) == lowest_price_list[0]:
            return item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    shop = build_info.clone()
    #find the smallest number for build
    lowest_price_list = []
    for item in shop.build_items():
        lowest_price_list.append(shop.get_cost(item))
    lowest_price_list = sorted(lowest_price_list)
    # return the item that matches that price
    for item in shop.build_items():
        if shop.get_cost(item) == lowest_price_list[-1]:
            return item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    shop = build_info.clone()
    #find the smallest number for build
    lowest_price_list = []
    for item in shop.build_items():
        lowest_price_list.append(shop.get_cost(item))
    lowest_price_list = sorted(lowest_price_list)
    # return the item that matches that price
    for item in shop.build_items():
        if shop.get_cost(item) == lowest_price_list[0]:
            return item
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print (strategy_name, ":", state)

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    #print(history[0][1])
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    """
    Run the simulator.
    """    
    #run_strategy("None/MyStrat", SIM_TIME, strategy_none)

    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    
