# this file will run tests on the times.py file

from times import compute_overlap_time, time_range

def test_given_input():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short) 
    h = time_range("2010-01-14 10:30:00", "2010-01-15 10:45:00")
    expected = compute_overlap_time(short, h)
    assert result == expected

