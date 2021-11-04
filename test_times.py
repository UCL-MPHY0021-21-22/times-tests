from times import *
import pytest
from pytest import raises

test_range_0 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
test_range_1 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
test_range_2 = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
test_range_3 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
test_range_4 = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")

expected_0 = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
expected_1 = []

@pytest.mark.parametrize("time_range_1,time_range_2,expected", [(test_range_0,test_range_1, expected_0), (test_range_0, test_range_2, expected_1), \
    (test_range_3, test_range_1, expected_0), (test_range_0, test_range_4, expected_1)])
def test_overlap(time_range_1, time_range_2, expected):
    assert compute_overlap_time(time_range_1, time_range_2) == expected

def test_negative():
    with raises(ValueError, match ="Start time must be before end time."):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
