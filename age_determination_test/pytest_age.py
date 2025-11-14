import pytest
from age import categorize_by_age as determine_age_group
def test_determine_child_age_group():
    assert determine_age_group(5) == "Child"
    assert determine_age_group(0) == "Child"
    assert determine_age_group(9) == "Child"

def test_determine_teenager_age_group():
    assert determine_age_group(10) == "Teenager"
    assert determine_age_group(15) == "Teenager"
    assert determine_age_group(18) == "Teenager"

def test_determine_adult_age_group():
    assert determine_age_group(19) == "Adult"
    assert determine_age_group(30) == "Adult"
    assert determine_age_group(64) == "Adult"

def test_determine_golden_age_group():
    assert determine_age_group(65) == "Golden age"
    assert determine_age_group(80) == "Golden age"
    assert determine_age_group(120) == "Golden age"

def test_determine_invalid_age_group():
    assert determine_age_group(-1) == "Invalid age: -1"
    assert determine_age_group(121) == "Invalid age: 121"
    assert determine_age_group(150) == "Invalid age: 150"

# python -m pytest age_determination_test/pytest_age.py -v