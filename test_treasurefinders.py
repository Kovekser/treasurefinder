import mock
import pytest

from treasurefinder import treasure_finder
from treasurefinder_class import TreasureFinder


TEST_CASE_SUCCESS = (('55', '14', '25', '52', '21'),
                     ('44', '31', '11', '53', '43'),
                     ('24', '13', '45', '12', '34'),
                     ('42', '22', '43', '32', '41'),
                     ('51', '23', '33', '54', '15'))

TEST_CASE_FAILURE = (('55', '14', '25', '52', '21'),
                     ('44', '31', '11', '53', '43'),
                     ('24', '13', '45', '12', '34'),
                     ('42', '22', '44', '32', '41'),
                     ('51', '23', '33', '54', '15'))


def test_treasurefinder_func_success():
    expected = "You've found treasure in the cell 43"
    result = treasure_finder(TEST_CASE_SUCCESS)
    assert result == expected


def test_treasurefinder_func_failure():
    expected = 'Unfortunately there is no treasure here'
    result = treasure_finder(TEST_CASE_FAILURE)
    assert result == expected


@mock.patch('treasurefinder_class.TreasureFinder._csv_to_array', mock.MagicMock(return_value=TEST_CASE_SUCCESS))
def test_treasurefinder_class_success():
    expected = "You've found treasure in the cell 43"
    result = TreasureFinder('some.csv').finder()
    assert result == expected


@mock.patch('treasurefinder_class.TreasureFinder._csv_to_array', mock.MagicMock(return_value=TEST_CASE_FAILURE))
def test_treasurefinder_class_failure():
    expected = 'Unfortunately there is no treasure here'
    result = TreasureFinder('some.csv').finder()
    assert result == expected