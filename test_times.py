# this file will run tests on the times.py file

from times import compute_overlap_time, time_range
import pytest

def test_given_input():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    
    assert result == expected

def test_no_overlap():
    test1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    test2 = time_range("2010-01-12 13:00:00", "2010-01-12 15:00:00")

    result = compute_overlap_time(test1, test2) 
    expected = []

    assert result == expected

def test_time_backwards():

    with pytest.raises(ValueError):
        test1 = time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
        test2 = time_range("2010-01-12 11:00:00", "2010-01-12 10:30:00")


def test_multiple_intervals():
    large = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 3, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 120)

    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:34:00'), ('2010-01-12 10:37:30', '2010-01-12 10:39:00'), ('2010-01-12 10:43:00', '2010-01-12 10:44:00')]

    assert result == expected

def test_full_overlap():

    high = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    low = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")

    result = compute_overlap_time(high,low)
    expected = [("2010-01-12 10:00:00", "2010-01-12 12:00:00)")]

    assert result == expected
