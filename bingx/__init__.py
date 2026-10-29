import sys
import bingx.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from bingx.ccxt import bingx as BingxSync
from bingx.ccxt.async_support.bingx import bingx as BingxAsync
from bingx.ccxt.pro.bingx import bingx as BingxWs
