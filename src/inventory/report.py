from inventory.stock import Stock


def summary(stock: Stock) -> dict[str, int]:
    return {
        "skus": len(stock.items),
        "units": sum(item.quantity for item in stock.items.values()),
    }


def low_stock(stock: Stock) -> list[str]:
    """Return SKUs with quantity at or below reorder level, sorted ascending."""
    return sorted(
        sku for sku, item in stock.items.items() if item.quantity <= item.reorder_level
    )
