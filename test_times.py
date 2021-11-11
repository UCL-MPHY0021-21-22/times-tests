from datetime import time
from times import time_range, compute_overlap_time
import pytest

# def test_given_input():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_not_overlap():
#     '''two time ranges that do not overlap'''
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
#     result = compute_overlap_time(large, short)
#     expected = []
#     assert result == expected

# def test_several_intervals():
#     '''two time ranges that both contain several intervals each'''
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected 

# def test_start_end_same():
#     '''two time ranges that end exactly at the same time when the other starts'''
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")
#     result = compute_overlap_time(large, short)
#     expected = []
#     assert result == expected 

# Parametrizing fixtures and test functions

test_range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
test_range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
expected1 = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
test_range3 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
test_range4 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
expected2 = []

def test_backwards_date_error():
    '''Negative testing - start date always before end date'''
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

@pytest.mark.parametrize("time_range1, time_range2, expected",
[(test_range1, test_range2, expected1),
(test_range1, test_range3, expected2),
(test_range4, test_range2, expected1),
(test_range1, test_range3, expected2)])

def test_eval(time_range1, time_range2, expected):
    assert compute_overlap_time(time_range1, time_range2) == expected

    