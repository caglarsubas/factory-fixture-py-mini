import copy

from inventory.report import low_stock, summary
from inventory.stock import Stock


def test_summary_counts_skus_and_units() -> None:
    stock = Stock()
    stock.add("apple", 3)
    stock.add("pear", 4)
    assert summary(stock) == {"skus": 2, "units": 7}


def test_low_stock_includes_equal_and_below_excludes_above() -> None:
    stock = Stock()
    stock.add("eq", 5, 5)
    stock.add("below", 2, 5)
    stock.add("above", 6, 5)
    assert low_stock(stock) == ["below", "eq"]


def test_low_stock_sorted_regardless_of_insertion_order() -> None:
    stock = Stock()
    for sku in ["pear", "Apple", "banana", "apple"]:
        stock.add(sku, 0, 1)
    assert low_stock(stock) == ["Apple", "apple", "banana", "pear"]


def test_low_stock_empty_cases() -> None:
    assert low_stock(Stock()) == []
    stock = Stock()
    stock.add("a", 3, 1)
    assert low_stock(stock) == []


def test_low_stock_default_reorder_level_zero_and_negative() -> None:
    stock = Stock()
    stock.add("zero", 0)
    stock.add("neg", 1)
    stock.remove("neg", 3)
    stock.add("pos", 1)
    assert low_stock(stock) == ["neg", "zero"]


def test_low_stock_does_not_modify_stock() -> None:
    stock = Stock()
    stock.add("a", 1, 2)
    stock.add("b", 9, 2)
    before = copy.deepcopy(stock)
    low_stock(stock)
    assert stock == before
