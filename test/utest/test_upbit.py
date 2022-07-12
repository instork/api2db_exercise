"""test script for python-project-template."""
import sys

sys.path.insert(0, "../../")
# import pytest
from api import upbit


def test_pyubit() -> None:
    """Test pyupbit ohlcv."""
    data = upbit.get_ohlcv("KRW-ETH", "minute1", 3)
    keys = ["open", "high", "low", "close", "volume", "value"]
    for key in keys:
        assert key in data.keys()
