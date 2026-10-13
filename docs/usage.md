# Using py-mini

## Stock

`Stock.add(sku, quantity)` and `Stock.remove(sku, quantity)` change stock levels.

## Tokens

`issue_token` and `verify_token` sign API tokens with an HMAC key the caller provides.

## Reports

`summary(stock)` summarises the stock.

`low_stock(stock)` returns the SKUs whose quantity is less than or equal to their reorder level, sorted by SKU (Python's default string ordering), so buyers know what to reorder.

## Snapshots

`save_snapshot` and `load_snapshot` write and read stock levels as JSON.
