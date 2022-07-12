"""Get data using pyubit.

- Author: NamSahng
- Email: namskygreen@naver.com
"""
from typing import Dict

import pyupbit


def get_ohlcv(ticker: str, interval: str, count: int) -> Dict:
    """Get ohlcv."""
    ohlcv = pyupbit.get_ohlcv(ticker, interval, count)
    ohlcv = ohlcv.to_dict()
    return ohlcv
