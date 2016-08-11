test:
	python3 setup.py test

watch:
	nosy

test_game:
	nosetests tests/ai_hard_strategy_tests.py:play_all_games
