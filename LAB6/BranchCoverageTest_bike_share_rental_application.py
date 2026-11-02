import pytest
from bike_share_rental import ride_cost, dock_status, can_unlock

#Example test cases:
def test_standard_ride():
    assert ride_cost("standard", 45, False, False) == 40

def test_dock_available():
    assert dock_status(5, 10) == "available"

#Added test cases for code (line) coverage:
def test_unknown_bike_type():
    with pytest.raises(ValueError):
        ride_cost("tandem", 30, False, False)

def test_invalid_duration():
    with pytest.raises(ValueError):
        ride_cost("standard", 0, False, False)

def test_subscriber_free_ride():
    assert ride_cost("standard", 30, True, False) == 0

def test_subscriber_paid_ride():
    assert ride_cost("electric", 90, True, False) == 70

def test_peak_surcharge():
    assert ride_cost("standard", 30, False, True) == 35

def test_long_ride_surcharge():
    assert ride_cost("standard", 200, False, False) == 240

def test_dock_empty():
    assert dock_status(0, 10) == "empty"

def test_dock_full():
    assert dock_status(10, 10) == "full"

def test_dock_few_bikes():
    assert dock_status(2, 10) == "few bikes"

def test_dock_few_slots():
    assert dock_status(9, 10) == "few slots"

def test_invalid_capacity():
    with pytest.raises(ValueError):
        dock_status(5, 0)

def test_negative_bike_count():
    with pytest.raises(ValueError):
        dock_status(-1, 10)

def test_unlock_blocked_by_active_ride():
    assert can_unlock(500, True, 25) is False

def test_unlock_under_16():
    assert can_unlock(500, False, 15) is False

def test_unlock_teen_with_balance():
    assert can_unlock(150, False, 17) is True

def test_unlock_adult_with_balance():
    assert can_unlock(60, False, 30) is True

def test_unlock_adult_low_balance():
    assert can_unlock(40, False, 30) is False

#Added test cases for branch coverage (condition combinations):
def test_peak_cargo_no_surcharge():
    assert ride_cost("cargo", 30, False, True) == 50

def test_electric_ride_no_peak():
    assert ride_cost("electric", 60, False, False) == 70

def test_subscriber_long_peak_ride():
    assert ride_cost("standard", 200, True, True) == 235

def test_too_many_bikes():
    with pytest.raises(ValueError):
        dock_status(11, 10)

def test_unlock_teen_low_balance():
    assert can_unlock(99, False, 17) is False

def test_unlock_exact_age_18():
    assert can_unlock(50, False, 18) is True
