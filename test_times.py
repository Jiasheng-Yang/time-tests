import pytest
from times import time_range, compute_overlap_time

@pytest.mark.parametrize(
    "range1, range2, expected",
    [
        # test_given_input
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", number_of_intervals=1, gap_between_intervals_s=0),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", number_of_intervals=2, gap_between_intervals_s=60),
            [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        ),
        # test_time_no_overlap
        (
            time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00", number_of_intervals=1, gap_between_intervals_s=0),
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", number_of_intervals=1, gap_between_intervals_s=0),
            []
        ),
        # test_time_multi_intervals
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", number_of_intervals=2, gap_between_intervals_s=60),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", number_of_intervals=2, gap_between_intervals_s=60),
            [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        ),
        # test_time_adjacent
        (
            time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00", number_of_intervals=1, gap_between_intervals_s=0),
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", number_of_intervals=1, gap_between_intervals_s=0),
            []
        ),
    ]
)
def test_compute_overlap_time(range1, range2, expected):
    result = compute_overlap_time(range1, range2)
    assert result == expected, f"Expected: {expected}, but got: {result}"

"""
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", number_of_intervals=1, gap_between_intervals_s=0)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", number_of_intervals=2, gap_between_intervals_s=60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    # judge that the result matches the expected value
    assert result == expected, f"Expected: {expected}, but Result: {result}, doesn't match!"

def test_time_no_overlap():
    range1 = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00", number_of_intervals=1, gap_between_intervals_s=0)
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", number_of_intervals=1, gap_between_intervals_s=0)
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected, f"Expected: {expected}, but got: {result}"

def test_time_multi_intervals():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", number_of_intervals=2, gap_between_intervals_s=60)
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", number_of_intervals=2, gap_between_intervals_s=60)
    result = compute_overlap_time(range1, range2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected, f"Expected: {expected}, but got: {result}"

def test_time_adjacent():
    range1 = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00", number_of_intervals=1, gap_between_intervals_s=0)
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", number_of_intervals=1, gap_between_intervals_s=0)
    result = compute_overlap_time(range1, range2)
    expected = []
    assert result == expected, f"Expected: {expected}, but got: {result}"
"""

def test_wrong_input():
    start_time = "2010-01-12 08:00:00"
    end_time = "2010-01-11 08:00:00"
    with pytest.raises(ValueError, match="Wrong Input!"):
        time_range(start_time, end_time)