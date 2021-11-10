from datetime import time
from times import time_range, compute_overlap_time
from pytest import raises

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_not_overlap():
    '''two time ranges that do not overlap'''
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:01:00", "2010-01-12 13:00:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_several_intervals():
    '''two time ranges that both contain several intervals each'''
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected 

def test_start_end_same():
    '''two time ranges that end exactly at the same time when the other starts'''
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected 

def test_backwards_date_error():
    '''Negative testing - start date always before end date'''
    with raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

    
