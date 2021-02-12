"""
Cookie Clicker Simulator
"""

#import simpleplot
import math

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._current_cookies = float(0)
        self._total_cookies = float(0)
        self._current_cps = float(1)
        self._current_time = float(0)
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        result = ('Current time: ' + str(self._current_time) + 
        '\nCurrent cookies: ' + str(self._current_cookies) + 
        '\nCurrent CPS: ' + str(self._current_cps) + 
        '\nTotal cookies: ' + str(self._total_cookies))
        return result
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return float(self._current_cookies)
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return float(self._current_cps)
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return float(self._current_time)
    
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
        if cookies <= self._current_cookies:
            result = 0.0
        else:
            cookies_to_earn = cookies - self._current_cookies
            result = cookies_to_earn / self._current_cps
        return float(math.ceil(result))
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0:
            self._current_cookies += self._current_cps * time
            self._total_cookies += self._current_cps * time
            self._current_time += time
                
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self._current_cookies:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, cost, self._total_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    shop = build_info.clone()
    game = ClickerState()
    while game.get_time() <= duration:
        next_item_to_purchase = strategy(game.get_cookies(), game.get_cps(), game.get_history(), duration - game.get_time(), shop.clone())
        if next_item_to_purchase == None:
            break
        if game.get_cookies() < shop.get_cost(next_item_to_purchase):
            if game.time_until(shop.get_cost(next_item_to_purchase)) > duration - game.get_time():
                break
            game.wait(game.time_until(shop.get_cost(next_item_to_purchase)))
        game.buy_item(next_item_to_purchase, shop.get_cost(next_item_to_purchase), shop.get_cps(next_item_to_purchase))
        shop.update_item(next_item_to_purchase)
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
    result = None
    shop = build_info.clone()
    cheapest = [shop.build_items()[0], shop.get_cost(shop.build_items()[0])]
    for item in shop.build_items():
        if shop.get_cost(item) < cheapest[1]:
            cheapest[0] = item
            cheapest[1] = shop.get_cost(item)
    if cheapest[1] <= cookies + time_left * cps:
        result = cheapest[0]
    return result


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    result = None
    shop = build_info.clone()
    most_expensive = [shop.build_items()[0], shop.get_cost(shop.build_items()[0])]
    for item in shop.build_items():
        if shop.get_cost(item) > most_expensive[1] and shop.get_cost(item) <= cookies + time_left * cps:
            most_expensive[0] = item
            most_expensive[1] = shop.get_cost(item)
    if most_expensive[1] <= cookies + time_left * cps:
        result = most_expensive[0]
    return result


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    result = None
    shop = build_info.clone()
    history_summary = {}
    for item in history:
        if item[1] != None:
            if item[1] not in history_summary:
                history_summary[item[1]] = 1
            else:
                history_summary[item[1]] += 1
    for item in shop.build_items():
        if item not in history_summary:
            history_summary[item] = 0
    for item in history_summary:
        history_summary[item] = [history_summary[item], shop.get_cost(item)]
    candidate = ['dummy', float('inf'), float('inf')]
    for item in history_summary:
        if history_summary[item][0] < candidate[1] and history_summary[item][1] <= cookies + time_left * cps:
            candidate = [item, history_summary[item][0], history_summary[item][1]]
    if candidate[2] <= cookies + time_left * cps:
        result = candidate[0]
    return result


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print (strategy_name, ":", state)

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    """
    Run the simulator.
    """    
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()