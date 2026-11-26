import math
import time
import pytest
from main import factorial


@pytest.mark.parametrize("n", range(0, 110))
def test_factorial_shard1(n):
    time.sleep(0.15)
    assert factorial(n) == math.factorial(n)
