# bingx-python
Python SDK (sync and async) for Bingx cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bingx)
- You can check Bingx's docs here: [Docs](https://www.google.com/search?q=google+bingx+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/bingx-python
- Pypi package: https://pypi.org/project/bingx


## Installation

```
pip install bingx
```

## Usage

### Sync

```Python
from bingx import BingxSync

def main():
    instance = BingxSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from bingx import BingxAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BingxAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from bingx import BingxWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = BingxWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_market_order_with_cost(self, symbol: str, side: OrderSide, cost: float, params={})`
- `create_market_sell_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_balance(self, params={})`
- `fetch_canceled_and_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_canceled_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_addresses_by_network(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_inverse_swap_markets(self, params)`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_margin_mode(self, symbol: str, params={})`
- `fetch_mark_price(self, symbol: str, params={})`
- `fetch_mark_prices(self, symbols: Strings = None, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_liquidations(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest(self, symbol: str, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position_history(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_position_mode(self, symbol: Str = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_spot_markets(self, params)`
- `fetch_swap_markets(self, params)`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_transfers(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `add_margin(self, symbol: str, amount: float, params={})`
- `cancel_all_orders_after(self, timeout: Int, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids: List[str], symbol: Str = None, params={})`
- `close_all_positions(self, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `custom_encode(self, params)`
- `describe(self)`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `nonce(self)`
- `reduce_margin(self, symbol: str, amount: float, params={})`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params={})`
- `set_margin(self, symbol: str, amount: float, params={})`
- `set_position_mode(self, hedged: bool, symbol: Str = None, params={})`
- `set_sandbox_mode(self, enable: bool)`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `spot_v1_public_get_server_time(request)`
- `spot_v1_public_get_common_symbols(request)`
- `spot_v1_public_get_market_trades(request)`
- `spot_v1_public_get_market_depth(request)`
- `spot_v1_public_get_market_kline(request)`
- `spot_v1_public_get_ticker_24hr(request)`
- `spot_v1_public_get_ticker_price(request)`
- `spot_v1_public_get_ticker_bookticker(request)`
- `spot_v1_private_get_trade_query(request)`
- `spot_v1_private_get_trade_openorders(request)`
- `spot_v1_private_get_trade_historyorders(request)`
- `spot_v1_private_get_trade_mytrades(request)`
- `spot_v1_private_get_user_commissionrate(request)`
- `spot_v1_private_get_account_balance(request)`
- `spot_v1_private_post_trade_order(request)`
- `spot_v1_private_post_trade_cancel(request)`
- `spot_v1_private_post_trade_batchorders(request)`
- `spot_v1_private_post_trade_order_cancelreplace(request)`
- `spot_v1_private_post_trade_cancelorders(request)`
- `spot_v1_private_post_trade_cancelopenorders(request)`
- `spot_v1_private_post_trade_cancelallafter(request)`
- `spot_v2_public_get_market_depth(request)`
- `spot_v2_public_get_market_kline(request)`
- `spot_v3_private_get_get_asset_transfer(request)`
- `spot_v3_private_get_asset_transfer(request)`
- `spot_v3_private_get_capital_deposit_hisrec(request)`
- `spot_v3_private_get_capital_withdraw_history(request)`
- `spot_v3_private_post_post_asset_transfer(request)`
- `swap_v1_public_get_ticker_price(request)`
- `swap_v1_public_get_market_historicaltrades(request)`
- `swap_v1_public_get_market_markpriceklines(request)`
- `swap_v1_public_get_trade_multiassetsrules(request)`
- `swap_v1_private_get_positionside_dual(request)`
- `swap_v1_private_get_trade_batchcancelreplace(request)`
- `swap_v1_private_get_trade_fullorder(request)`
- `swap_v1_private_get_maintmarginratio(request)`
- `swap_v1_private_get_trade_positionhistory(request)`
- `swap_v1_private_get_positionmargin_history(request)`
- `swap_v1_private_get_twap_openorders(request)`
- `swap_v1_private_get_twap_historyorders(request)`
- `swap_v1_private_get_twap_orderdetail(request)`
- `swap_v1_private_get_trade_assetmode(request)`
- `swap_v1_private_get_user_marginassets(request)`
- `swap_v1_private_post_trade_cancelreplace(request)`
- `swap_v1_private_post_positionside_dual(request)`
- `swap_v1_private_post_trade_batchcancelreplace(request)`
- `swap_v1_private_post_trade_closeposition(request)`
- `swap_v1_private_post_trade_getvst(request)`
- `swap_v1_private_post_twap_order(request)`
- `swap_v1_private_post_twap_cancelorder(request)`
- `swap_v1_private_post_trade_assetmode(request)`
- `swap_v2_public_get_server_time(request)`
- `swap_v2_public_get_quote_contracts(request)`
- `swap_v2_public_get_quote_price(request)`
- `swap_v2_public_get_quote_depth(request)`
- `swap_v2_public_get_quote_trades(request)`
- `swap_v2_public_get_quote_premiumindex(request)`
- `swap_v2_public_get_quote_fundingrate(request)`
- `swap_v2_public_get_quote_klines(request)`
- `swap_v2_public_get_quote_openinterest(request)`
- `swap_v2_public_get_quote_ticker(request)`
- `swap_v2_public_get_quote_bookticker(request)`
- `swap_v2_private_get_user_balance(request)`
- `swap_v2_private_get_user_positions(request)`
- `swap_v2_private_get_user_income(request)`
- `swap_v2_private_get_trade_openorders(request)`
- `swap_v2_private_get_trade_openorder(request)`
- `swap_v2_private_get_trade_order(request)`
- `swap_v2_private_get_trade_margintype(request)`
- `swap_v2_private_get_trade_leverage(request)`
- `swap_v2_private_get_trade_forceorders(request)`
- `swap_v2_private_get_trade_allorders(request)`
- `swap_v2_private_get_trade_allfillorders(request)`
- `swap_v2_private_get_trade_fillhistory(request)`
- `swap_v2_private_get_user_income_export(request)`
- `swap_v2_private_get_user_commissionrate(request)`
- `swap_v2_private_get_quote_bookticker(request)`
- `swap_v2_private_post_trade_order(request)`
- `swap_v2_private_post_trade_batchorders(request)`
- `swap_v2_private_post_trade_closeallpositions(request)`
- `swap_v2_private_post_trade_cancelallafter(request)`
- `swap_v2_private_post_trade_margintype(request)`
- `swap_v2_private_post_trade_leverage(request)`
- `swap_v2_private_post_trade_positionmargin(request)`
- `swap_v2_private_post_trade_order_test(request)`
- `swap_v2_private_delete_trade_order(request)`
- `swap_v2_private_delete_trade_batchorders(request)`
- `swap_v2_private_delete_trade_allopenorders(request)`
- `swap_v3_public_get_quote_klines(request)`
- `cswap_v1_public_get_market_contracts(request)`
- `cswap_v1_public_get_market_premiumindex(request)`
- `cswap_v1_public_get_market_openinterest(request)`
- `cswap_v1_public_get_market_klines(request)`
- `cswap_v1_public_get_market_depth(request)`
- `cswap_v1_public_get_market_ticker(request)`
- `cswap_v1_private_get_trade_leverage(request)`
- `cswap_v1_private_get_trade_forceorders(request)`
- `cswap_v1_private_get_trade_allfillorders(request)`
- `cswap_v1_private_get_trade_openorders(request)`
- `cswap_v1_private_get_trade_orderdetail(request)`
- `cswap_v1_private_get_trade_orderhistory(request)`
- `cswap_v1_private_get_trade_margintype(request)`
- `cswap_v1_private_get_user_commissionrate(request)`
- `cswap_v1_private_get_user_positions(request)`
- `cswap_v1_private_get_user_balance(request)`
- `cswap_v1_private_post_trade_order(request)`
- `cswap_v1_private_post_trade_leverage(request)`
- `cswap_v1_private_post_trade_allopenorders(request)`
- `cswap_v1_private_post_trade_closeallpositions(request)`
- `cswap_v1_private_post_trade_margintype(request)`
- `cswap_v1_private_post_trade_positionmargin(request)`
- `cswap_v1_private_delete_trade_allopenorders(request)`
- `cswap_v1_private_delete_trade_cancelorder(request)`
- `contract_v1_private_get_allposition(request)`
- `contract_v1_private_get_allorders(request)`
- `contract_v1_private_get_balance(request)`
- `wallets_v1_private_get_capital_config_getall(request)`
- `wallets_v1_private_get_capital_deposit_address(request)`
- `wallets_v1_private_get_capital_innertransfer_records(request)`
- `wallets_v1_private_get_capital_subaccount_deposit_address(request)`
- `wallets_v1_private_get_capital_deposit_subhisrec(request)`
- `wallets_v1_private_get_capital_subaccount_innertransfer_records(request)`
- `wallets_v1_private_get_capital_deposit_riskrecords(request)`
- `wallets_v1_private_post_capital_withdraw_apply(request)`
- `wallets_v1_private_post_capital_innertransfer_apply(request)`
- `wallets_v1_private_post_capital_subaccountinnertransfer_apply(request)`
- `wallets_v1_private_post_capital_deposit_createsubaddress(request)`
- `subaccount_v1_private_get_list(request)`
- `subaccount_v1_private_get_assets(request)`
- `subaccount_v1_private_get_allaccountbalance(request)`
- `subaccount_v1_private_post_create(request)`
- `subaccount_v1_private_post_apikey_create(request)`
- `subaccount_v1_private_post_apikey_edit(request)`
- `subaccount_v1_private_post_apikey_del(request)`
- `subaccount_v1_private_post_updatestatus(request)`
- `account_v1_private_get_uid(request)`
- `account_v1_private_get_apikey_query(request)`
- `account_v1_private_get_account_apipermissions(request)`
- `account_v1_private_get_allaccountbalance(request)`
- `account_v1_private_post_innertransfer_authorizesubaccount(request)`
- `account_transfer_v1_private_get_subaccount_asset_transferhistory(request)`
- `account_transfer_v1_private_post_subaccount_transferasset_supportcoins(request)`
- `account_transfer_v1_private_post_subaccount_transferasset(request)`
- `user_auth_private_post_userdatastream(request)`
- `user_auth_private_put_userdatastream(request)`
- `user_auth_private_delete_userdatastream(request)`
- `copytrading_v1_private_get_swap_trace_currenttrack(request)`
- `copytrading_v1_private_post_swap_trace_closetrackorder(request)`
- `copytrading_v1_private_post_swap_trace_settpsl(request)`
- `copytrading_v1_private_post_spot_trader_sellorder(request)`
- `api_v3_private_get_asset_transfer(request)`
- `api_v3_private_get_asset_transferrecord(request)`
- `api_v3_private_get_capital_deposit_hisrec(request)`
- `api_v3_private_get_capital_withdraw_history(request)`
- `api_v3_private_post_post_asset_transfer(request)`
- `api_asset_v1_private_post_transfer(request)`
- `api_asset_v1_public_get_transfer_supportcoins(request)`

### WS Unified

- `describe(self)`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `watch_ohlcv_for_symbols(self, symbolsAndTimeframes: List[List[str]], since: Int = None, limit: Int = None, params={})`
- `get_order_book_limit_by_market_type(self, marketType: str, limit: Int = None)`
- `get_message_hash(self, unifiedChannel: str, symbol: Str = None, extra: Str = None)`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `set_balance_cache(self, client: Client, type, subType, subscriptionHash, params)`
- `load_balance_snapshot(self, client, messageHash, type, subType)`
- `keep_alive_listen_key(self, params={})`
- `authenticate(self, params={})`
- `pong(self, client, message)`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.