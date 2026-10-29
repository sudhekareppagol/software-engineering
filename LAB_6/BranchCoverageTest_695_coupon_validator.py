import pytest
from coupon_validator import coupon_discount, best_discount, is_expired


def test_welcome_coupon_new_user():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20


def test_welcome_coupon_existing_user():
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0


def test_empty_cart():
    with pytest.raises(ValueError):
        coupon_discount("WELCOME10", 0, True, "mon")


def test_weekend20_large_cart():
    assert coupon_discount("WEEKEND20", 600, True, "sat") == 120


def test_weekend20_small_cart():
    assert coupon_discount("WEEKEND20", 300, True, "sun") == 50


def test_weekend20_weekday():
    assert coupon_discount("WEEKEND20", 600, True, "mon") == 0


def test_flat100_large_cart():
    assert coupon_discount("FLAT100", 400, True, "mon") == 100


def test_flat100_small_cart():
    assert coupon_discount("FLAT100", 300, True, "mon") == 0


def test_unknown_coupon():
    assert coupon_discount("INVALID", 500, True, "mon") == 0


def test_best_discount():
    assert best_discount(
        ["WELCOME10", "FLAT100"], 1000, True, "mon"
    ) == 100


def test_best_discount_cap():
    assert best_discount(
        ["WEEKEND20"], 1000, True, "sat"
    ) == 200


def test_zero_validity_expired():
    assert is_expired(10, 5, 0) is True


def test_valid_coupon_not_expired():
    assert is_expired(10, 5, 10) is False


def test_coupon_expired():
    assert is_expired(20, 5, 10) is True