try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tic Tac Toe',
    'author': 'Hamish Rickerby',
    'url': 'https://github.com/rickerbh/tictactoe_py',
    'author_email': 'hamish@simplemachines.com.au',
    'version': '0.1',
    'install_requires': ['nose', 'nosy'],
    'packages': ['tictactoe'],
    'scripts': [],
    'name': 'tictactoe',
    'test_suite': 'nose.collector'
}

setup(**config)
