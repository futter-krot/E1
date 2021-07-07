import pytest, pytest_cov
from .. import gallows

class TestClass:

    def test_round(self):
        game = gallows.Gallow()
        assert game.round() == None

    def test_input(self):
        gallows.input = lambda _: 'ans'
        output = gallows.Gallow.round
        assert output == gallows.Gallow.round

    def teardown_method(self, method):
        gallows.input = input

    def test_choose_word(self):
        random_word = gallows.choose_word(gallows.choices)
        assert random_word in gallows.choices

    def test_calcualte_score_positive(self):
        score = gallows.calculate_score(1)
        assert score == 3

    def test_calcualte_score_negative(self):
        score = gallows.calculate_score(5)
        assert score == 0

    def test_create_game(self):
        game = gallows.create_game()
        assert game.word in gallows.choices
        assert game.attempts == 4
        assert game.cypher == '-' * len(game.word)
