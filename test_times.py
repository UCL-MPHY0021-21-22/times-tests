from times import compute_overlap_time, time_range

def test_small_within_large():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_small_on_boundary_still_within():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:00:00", "2010-01-12 10:15:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:00:00', '2010-01-12 10:07:00'), ('2010-01-12 10:08:00', '2010-01-12 10:15:00')]
    assert result == expected

def test_small_outside_large():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_half_of_small_within_large():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 09:54:30", "2010-01-12 10:05:30", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:00:30', '2010-01-12 10:05:30')]
    assert result == expected

