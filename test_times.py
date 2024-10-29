import pytest
import yaml
from times import time_range, compute_overlap_time, iss_passes
from unittest.mock import patch

"""
# Answers UCL-COMP0233-24-25/RSE-Classwork#16
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


def load_fixture_data():
    with open("fixture.yaml", "r") as file:
        return yaml.safe_load(file)

fixture_data = load_fixture_data()
parametrize_data = [
    (
        time_range(
            case[list(case.keys())[0]]["time_range_1"]["start"],
            case[list(case.keys())[0]]["time_range_1"]["end"],
            number_of_intervals=case[list(case.keys())[0]]["time_range_1"]["number_of_intervals"],
            gap_between_intervals_s=case[list(case.keys())[0]]["time_range_1"]["gap_between_intervals_s"]
        ),
        time_range(
            case[list(case.keys())[0]]["time_range_2"]["start"],
            case[list(case.keys())[0]]["time_range_2"]["end"],
            number_of_intervals=case[list(case.keys())[0]]["time_range_2"]["number_of_intervals"],
            gap_between_intervals_s=case[list(case.keys())[0]]["time_range_2"]["gap_between_intervals_s"]
        ),
        case[list(case.keys())[0]]["expected"]
    )
    for case in fixture_data
]

@pytest.mark.parametrize("range1, range2, expected", parametrize_data)
def test_compute_overlap_time(range1, range2, expected):
    result = [f'("{start}", "{end}")' for start, end in compute_overlap_time(range1, range2)]
    assert result == expected, f"Expected: {expected}, but got: {result}"

def test_iss_passes():
    mock_response = {
        "passes": [
            {"startUTC": 1263292200, "endUTC": 1263292620},  # 2010-01-12 10:30:00 to 2010-01-12 10:37:00
            {"startUTC": 1263292680, "endUTC": 1263293100}   # 2010-01-12 10:38:00 to 2010-01-12 10:45:00
        ]
    }
    with patch("times.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = iss_passes(56, 0, api_key="33Q884-HFUV8K-SCS3LG-55CU")
        expected = [
            ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
            ("2010-01-12 10:38:00", "2010-01-12 10:45:00")
        ]
        assert result == expected, f"Expected: {expected}, but got: {result}"

def test_wrong_input():
    start_time = "2010-01-12 08:00:00"
    end_time = "2010-01-11 08:00:00"
    with pytest.raises(ValueError, match="Wrong Input!"):
        time_range(start_time, end_time)