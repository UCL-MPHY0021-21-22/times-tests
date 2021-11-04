from typing import Match
from times import compute_overlap_time,time_range
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_backwards_range():
    with pytest.raises(ValueError,Match='m'):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

#def test_dont_overlap():
 #   large2 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
  #  short2 = time_range("2011-01-12 10:00:00", "2011-01-12 12:00:00")
   # result = compute_overlap_time(large2,short2)
    #expected = []
    #print(result)
    #assert (result == expected),'Overlap does not exist'