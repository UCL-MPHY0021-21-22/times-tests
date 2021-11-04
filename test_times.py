from times import *
import pytest

def test_given_input():
    large0 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short0 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result0 = compute_overlap_time(large0, short0)
    expected0 = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result0 == expected0
    #Two time ranges that do not overlap
def test_not_overlapping():
    large_not_overlapping = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short_not_overlapping = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60)
    result_not_overlapping = compute_overlap_time(large_not_overlapping, short_not_overlapping)
    expected_not_overlapping = [('2010-01-12 12:00:00', '2010-01-12 11:00:00'), ('2010-01-12 12:23:00', '2010-01-12 11:00:00')]
    assert result_not_overlapping == expected_not_overlapping
    #Two time ranges that both contain several intervals each
def test_several_intervals():
    large3 = time_range("2010-01-12 07:00:00", "2010-01-12 08:00:00",6,120)
    short3 = time_range("2010-01-12 08:00:00", "2010-01-12 12:45:00", 7, 60)
    result3 = compute_overlap_time(large3, short3)
    expected3 = [('2010-01-12 08:00:00', '2010-01-12 07:08:20'), ('2010-01-12 10:23:00', '2010-01-12 08:00:00')]
    assert result3 == expected3
    #Two time ranges that end exactly when the other one starts
def test_adjacent_time_range():
    large5 = time_range("2010-01-12 07:00:00", "2010-01-12 08:00:00")
    short5 = time_range("2010-01-12 08:00:00", "2010-01-12 12:45:00")
    result5 = compute_overlap_time(large5, short5)
    expected5 = [('2010-01-12 08:00:00', '2010-01-12 08:00:00')]
    assert result5 == expected5
    #Test for going backwards
def test_backwards_time():
    with pytest.raises(ValueError):
        time_range("2010-01-12 11:00:00", "2010-01-12 08:00:00")