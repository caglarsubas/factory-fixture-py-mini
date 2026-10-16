# Using py-mini

## Stock

`Stock.add(sku, quantity)` and `Stock.remove(sku, quantity)` change stock levels.

## Tokens

`issue_token` and `verify_token` sign API tokens with an HMAC key the caller provides.

## Reports

`summary(stock)` summarises the stock. It returns a dict with two keys:

- `skus`: the number of distinct SKUs (entries) held in the stock.
- `units`: the total (sum) of item quantities across all SKUs.

`low_stock(stock)` lists the SKUs that need reordering. It returns a `list[str]`
of every SKU whose quantity is at or below its reorder level
(`quantity <= reorder_level`), so a SKU exactly at its level is included and
SKUs above their level are left out. The list is ordered ascending by SKU
(plain string order). It does not change the stock.

## Snapshots

`save_snapshot` and `load_snapshot` write and read stock levels as JSON.
