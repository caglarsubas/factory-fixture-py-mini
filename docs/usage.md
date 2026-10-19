# Using py-mini

## Stock

`Stock.add(sku, quantity)` and `Stock.remove(sku, quantity)` change stock levels.

## Tokens

`issue_token` and `verify_token` sign API tokens with an HMAC key the caller provides.

## Reports

`summary(stock)` summarises the stock. It returns a dict with two keys, and both values are integers (`dict[str, int]`):

- `skus` is the number of distinct SKUs held in the stock. A SKU whose quantity has dropped to zero is still counted.
- `units` is the sum of the quantities across all SKUs.

`low_stock(stock)` returns the SKUs whose quantity is at or below their reorder level, sorted by SKU in ascending order. It does not change the stock.

## Snapshots

`save_snapshot` and `load_snapshot` write and read stock levels as JSON.
