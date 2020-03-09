import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    return {"Pen": {"qnt": 10, "unit_price": 3.75, "discount": 5},
            "Notebook": {"qnt": 5, "unit_price": 7.5, "discount": 10}}


def test_CanCalculateTotalImpurePrice(products):
    assert Invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(products):
    assert Invoice.totalDiscountPrice(products) == 5.62


def test_CanCalculateTotalPurePrice(products):
    assert Invoice.totalPurePrice(products) == 69.38
