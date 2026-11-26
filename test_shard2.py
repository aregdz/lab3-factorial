import math
import time
import pytest
from main import factorial


@pytest.mark.parametrize("n", range(110, 220))
def test_factorial_shard2(n):
    time.sleep(0.15)
    assert factorial(n) == math.factorial(n)
