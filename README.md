# bingx-python
Python SDK (sync and async) for Bingx with Rest and WS capabilities.

You can check Bingx's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/bingx)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install bingx
```

## Usage

### Async

```Python
from bingx import BingxAsync

async def main():
    instance = BingxAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from bingx import BingxSync

def main():
    instance = BingxSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from bingx import BingxWs

async def main():
    instance = BingxWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

