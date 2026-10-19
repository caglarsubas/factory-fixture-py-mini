from inventory.report import low_stock, summary
from inventory.stock import Stock


def test_summary_counts_skus_and_units() -> None:
    stock = Stock()
    stock.add("apple", 3)
    stock.add("pear", 4)
    assert summary(stock) == {"skus": 2, "units": 7}


def test_low_stock_includes_skus_at_or_below_reorder_level() -> None:
    stock = Stock()
    stock.add("below", 2, reorder_level=5)
    stock.add("equal", 5, reorder_level=5)
    stock.add("above", 6, reorder_level=5)
    assert low_stock(stock) == ["below", "equal"]


def test_low_stock_is_sorted_by_sku() -> None:
    stock = Stock()
    for sku in ("pear", "apple", "fig"):
        stock.add(sku, 1, reorder_level=3)
    assert low_stock(stock) == ["apple", "fig", "pear"]


def test_low_stock_empty_when_nothing_is_low() -> None:
    assert low_stock(Stock()) == []
    stock = Stock()
    stock.add("apple", 10, reorder_level=5)
    stock.add("pear", 1)  # default reorder level 0, quantity above it
    assert low_stock(stock) == []


def test_low_stock_does_not_mutate_stock() -> None:
    stock = Stock()
    stock.add("pear", 1, reorder_level=3)
    stock.add("apple", 9, reorder_level=3)
    stock.add("fig", 0)
    before = {s: (i.quantity, i.reorder_level) for s, i in stock.items.items()}
    low_stock(stock)
    after = {s: (i.quantity, i.reorder_level) for s, i in stock.items.items()}
    assert before == after
    assert set(stock.items) == {"pear", "apple", "fig"}
