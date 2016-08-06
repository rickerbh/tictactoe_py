test:
	python3 setup.py test

watch:
	nosy

test_game:
	nosetests tests/ai_strategy_tests.py:ai_strategy_play_all_games
