import sys 
import os
from times import compute_overlap_time, time_range
import pytest


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short)
    expected = compute_overlap_time(large, short)
    assert result == expected

test_given_input()


