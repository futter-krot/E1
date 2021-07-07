  import pytest, pytest_cov
from gallows import Gallow, choose_word, calculate_score, create_game, choices, attempts
import gallows

class TestClass:

    def test_round(self):
        game = Gallow()
        assert game.round() == None

    def test_input(self):
        gallows.input = lambda _: 'ans'
        output = Gallow.round
        assert output == Gallow.round

    def teardown_method(self, method):
        gallows.input = input

    def test_choose_word(self):
        random_word = choose_word(choices)
        assert random_word in choices

    def test_calcualte_score_positive(self):
        score = calculate_score(1)
        assert score == 3

    def test_calcualte_score_negative(self):
        score = calculate_score(5)
        assert score == 0

    def test_create_game(self):
        game = create_game()
        assert game.word in choices
        assert game.attempts == 4
        assert game.cypher == '-' * len(game.word)
