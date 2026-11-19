# py-mini

A small inventory library used as a software-factory fixture target: stock levels, API tokens, reports and snapshots.

```bash
uv sync --frozen
uv run --frozen mypy
uv run --frozen ruff check
uv run --frozen pytest -q
```
Drift drill.

Usage example (run from the repository root):

```python
>>> import sys
>>> sys.path.insert(0, "src")  # run from the repository root
>>> from inventory.report import low_stock
>>> from inventory.stock import Stock
>>> stock = Stock()
>>> _ = stock.add("widget", 3, reorder_level=5)
>>> _ = stock.add("bolt", 100, reorder_level=10)
>>> _ = stock.add("gadget", 5, reorder_level=5)
>>> low_stock(stock)
['gadget', 'widget']

```
