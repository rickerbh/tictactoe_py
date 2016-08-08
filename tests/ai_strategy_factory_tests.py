from nose.tools import *
from tictactoe.ai_strategy_factory import AIStrategyFactory
from tictactoe.ai_strategies.hard import Hard
from tictactoe.ai_strategies.easy import Easy

def factory_returns_hard_strategy_test():
    factory = AIStrategyFactory()
    strategy = factory.strategy("Hard", "X", "O")
    assert isinstance(strategy, Hard)

def factory_returns_easy_strategy_test():
    factory = AIStrategyFactory()
    strategy = factory.strategy("Easy", "X", "O")
    assert isinstance(strategy, Easy)
    
