from times import compute_overlap_time
from times import time_range
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short)
    expected = short
    assert result == expected 


test_given_input()

#1 two time ranges that do not overlap
def test_non_overlapping():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2011-01-12 10:30:00", "2011-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected 

#2 two time ranges that both contain several intervals each

def test_several_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short)
    expected = short
    assert result == expected 

#3 two time ranges that end exactly at the same time when the other starts

def test_back_to_back():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")
    print(compute_overlap_time(first, second))
    result = compute_overlap_time(first, second)
    expected = []
    assert result == expected 

#Negative Testing

def test_negative():

    with pytest.raises(ValueError):
            second = time_range( "2010-01-12 14:00:00", "2010-01-12 12:00:00")
            
