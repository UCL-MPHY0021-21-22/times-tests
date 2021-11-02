# this file will run tests on the times.py file

from times import compute_overlap_time, time_range

def test_given_input():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    
    assert result == expected

def test_no_overlap():
    test1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    test2 = time_range("2010-01-12 13:00:00", "2010-01-12 15:00:00")

    result1 = compute_overlap_time(test1, test2) 
    expected = []

    assert result1 == expected


