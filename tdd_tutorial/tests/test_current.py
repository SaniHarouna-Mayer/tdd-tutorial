import pytest
from datetime import datetime
from tdd_tutorial.tdd_tut import is_current


@pytest.mark.parametrize("input, expected",[
	({"begin_year": 2018, "end_year": 2019}, False),
	({"begin_year": 2017}, True),
	({"begin_year": 2019, "begin_month": 8, "begin_day": 11, "end_year": 2020, "end_month": 7, "end_day": 11}, True),
	({"begin_year": 2019, "begin_month": 8, "begin_day": 11}, True),
	])
def test_current(input, expected):
	assert is_current(input) == expected