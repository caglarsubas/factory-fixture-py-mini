from inventory.report import low_stock, summary
from inventory.stock import Stock


def test_summary_counts_skus_and_units() -> None:
    stock = Stock()
    stock.add("apple", 3)
    stock.add("pear", 4)
    assert summary(stock) == {"skus": 2, "units": 7}


def test_low_stock_includes_item_at_level() -> None:
    stock = Stock()
    stock.add("pear", 5, 5)
    assert low_stock(stock) == ["pear"]


def test_low_stock_includes_item_below_level() -> None:
    stock = Stock()
    stock.add("apple", 2, 3)
    assert low_stock(stock) == ["apple"]


def test_low_stock_excludes_item_above_level() -> None:
    stock = Stock()
    stock.add("kiwi", 10, 4)
    assert low_stock(stock) == []


def test_low_stock_sorted_by_sku() -> None:
    stock = Stock()
    stock.add("pear", 5, 5)
    stock.add("kiwi", 10, 4)
    stock.add("apple", 2, 3)
    stock.add("Zed", 1, 1)
    result = low_stock(stock)
    assert isinstance(result, list)
    assert result == ["Zed", "apple", "pear"]


def test_low_stock_empty_stock() -> None:
    assert low_stock(Stock()) == []


def test_low_stock_default_level_zero_quantity() -> None:
    stock = Stock()
    stock.add("a", 0)
    stock.add("b", 1)
    assert low_stock(stock) == ["a"]


def test_low_stock_negative_quantity_after_remove() -> None:
    stock = Stock()
    stock.add("a", 1, 0)
    stock.remove("a", 3)
    assert low_stock(stock) == ["a"]


def test_low_stock_does_not_modify_stock() -> None:
    stock = Stock()
    stock.add("b", 1, 2)
    stock.add("a", 9, 2)
    before = {k: (v.quantity, v.reorder_level) for k, v in stock.items.items()}
    low_stock(stock)
    after = {k: (v.quantity, v.reorder_level) for k, v in stock.items.items()}
    assert before == after
    assert list(stock.items) == ["b", "a"]
