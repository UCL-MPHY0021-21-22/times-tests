from times import compute_overlap_time, time_range

# def test_generic_case():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
#     assert compute_overlap_time(large, short) == expected

# work collaboratively!
# create a test each in test_times.py for
# two time ranges that do not overlap
# two time ranges that both contain several intervals each
# two time ranges that end exactly at the same time when the other starts
# run pytest and see whether all tests are picked up by pytest and whether they pass.
# fix any bugs in times.py the tests may have helped you find.
# Add the new and modified files to the repository, commit them (with a meaningful comment that also includes
# https://github.com/UCL-MPHY0021-21-22/RSE-Classwork/issues/17) and push it to your fork.

def several_intervals():
    multi_interval_1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",4)
    multi_interval_2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00",4)
    expected = [("2010-01-12 11:00:00", "2010-01-12 11:30:00"),("2010-01-12 11:30:00", "2010-01-12 12:00:00")]
    print("expected is:", expected)
    print("calculated is:", compute_overlap_time(multi_interval_1,multi_interval_2))
    #assert expected == compute_overlap_time(multi_interval_1,multi_interval_2)

several_intervals()