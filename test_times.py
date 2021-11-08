from times import *
import pytest
from pytest import raises
import yaml

with open('fixture.yaml') as yaml_file:
    fixture = yaml.load(yaml_file)

@pytest.mark.parametrize("time_range_1,time_range_2,expected", [(fixture["generic"]["time_range_1"],fixture["generic"]["time_range_2"], fixture["generic"]["expected"]),\
     (fixture["no_overlap"]["time_range_1"], fixture["no_overlap"]["time_range_2"], fixture["no_overlap"]["expected"]),\
         (fixture["several_intervals"]["time_range_1"], fixture["several_intervals"]["time_range_2"], fixture["several_intervals"]["expected"]),\
             (fixture["same_time"]["time_range_1"], fixture["same_time"]["time_range_2"], fixture["same_time"]["expected"])])

def test_overlap(time_range_1, time_range_2, expected):
    assert compute_overlap_time(time_range_1, time_range_2) == expected

def test_negative():
    with raises(ValueError, match ="Start time must be before end time."):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")