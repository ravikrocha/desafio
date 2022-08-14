import itertools
from heuristica_gulosa import *


def test_if_max_cost_is_zero_then_no_investiment():
    max_cost = 0
    chosen_items = greedy_knapsack(max_cost, available_items)
    assert chosen_items == []


def test_when_one_single_investiment_is_choosen():
    max_cost = 1
    available_items = [
        ValuableItem(name='Item 0', profit=20, cost=1),
        ValuableItem(name='Item 1', profit=10, cost=1),
        ValuableItem(name='Item 2', profit=30, cost=1),
        ValuableItem(name='Item 3', profit=5, cost=1),
        ValuableItem(name='Item 4', profit=15, cost=1),
        ValuableItem(name='Item 5', profit=10, cost=1),
        ValuableItem(name='Item 6', profit=8, cost=1),
        ValuableItem(name='Item 7', profit=4, cost=1)
    ]
    expected_solutions = list(itertools.permutations(
        [ValuableItem(name='Item 2', profit=30, cost=1)]))

    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_investiment_1_is_greater_than_5_drop_5():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=20, cost=1),
        ValuableItem(name='Item 1', profit=10, cost=1),
        ValuableItem(name='Item 2', profit=30, cost=1),
        ValuableItem(name='Item 3', profit=5, cost=1),
        ValuableItem(name='Item 4', profit=15, cost=1),
        ValuableItem(name='Item 5', profit=10, cost=1),
        ValuableItem(name='Item 6', profit=8, cost=1),
        ValuableItem(name='Item 7', profit=4, cost=1)
    ]
    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 3', profit=5, cost=1),
        ValuableItem(name='Item 2', profit=30, cost=1),
        ValuableItem(name='Item 0', profit=20, cost=1),
        ValuableItem(name='Item 1', profit=10, cost=1),
        ValuableItem(name='Item 5', profit=10, cost=1)
    ]))
    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_investiment_5_is_greater_than_1_drop_1():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=30, cost=1),
        ValuableItem(name='Item 1', profit=3, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 3', profit=5, cost=1),
        ValuableItem(name='Item 4', profit=40, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]
    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 4', profit=40, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]))
    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_investiment_2_is_chosen_then_choose_4():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=8, cost=1),
        ValuableItem(name='Item 1', profit=24, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 3', profit=5, cost=1),
        ValuableItem(name='Item 4', profit=7, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]

    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 3', profit=5, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 1', profit=24, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1)
    ]))

    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_investiment_4_is_chosen_and_investiment_2_is_not_chosen():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=8, cost=1),
        ValuableItem(name='Item 1', profit=4, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 3', profit=20, cost=1),
        ValuableItem(name='Item 4', profit=7, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]
    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 3', profit=20, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]))
    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_neither_investiment_2_and_4_are_chosen():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=8, cost=1),
        ValuableItem(name='Item 1', profit=6, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 3', profit=5, cost=1),
        ValuableItem(name='Item 4', profit=7, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]
    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1),
        ValuableItem(name='Item 0', profit=8, cost=1)
    ]))
    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_investiment_2_cant_be_taken_bcs_4_is_too_expensive():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=8, cost=1),
        ValuableItem(name='Item 1', profit=24, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 3', profit=5, cost=10),
        ValuableItem(name='Item 4', profit=7, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]
    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1),
        ValuableItem(name='Item 0', profit=8, cost=1)]))
    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_investiment_2_is_high_but_4_is_not_worthy():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=8, cost=1),
        ValuableItem(name='Item 1', profit=24, cost=1),
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 3', profit=5, cost=2),
        ValuableItem(name='Item 4', profit=7, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1)
    ]
    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 2', profit=25, cost=1),
        ValuableItem(name='Item 5', profit=15, cost=1),
        ValuableItem(name='Item 6', profit=12, cost=1),
        ValuableItem(name='Item 7', profit=10, cost=1),
        ValuableItem(name='Item 0', profit=8, cost=1)]))
    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions


def test_when_itens_2_and_4_is_not_worthy_to_keep_even_though_2_is_one_of_the_best():
    max_cost = 5
    available_items = [
        ValuableItem(name='Item 0', profit=16, cost=1),
        ValuableItem(name='Item 1', profit=9, cost=1),
        ValuableItem(name='Item 2', profit=15, cost=1),
        ValuableItem(name='Item 3', profit=1, cost=2),
        ValuableItem(name='Item 4', profit=6, cost=1),
        ValuableItem(name='Item 5', profit=14, cost=1),
        ValuableItem(name='Item 6', profit=8, cost=1),
        ValuableItem(name='Item 7', profit=7, cost=1)
    ]
    expected_solutions = list(itertools.permutations([
        ValuableItem(name='Item 0', profit=16, cost=1),
        ValuableItem(name='Item 2', profit=15, cost=1),
        ValuableItem(name='Item 5', profit=14, cost=1),
        ValuableItem(name='Item 6', profit=8, cost=1),
        ValuableItem(name='Item 7', profit=7, cost=1)]))
    assert tuple(greedy_knapsack(max_cost, available_items)
                 ) in expected_solutions
