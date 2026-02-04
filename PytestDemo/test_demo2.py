import pytest

@pytest.mark.skip(reason="Bug has beem raised for this method")
def test_third_program(setup):
    var="This is my third program"
    print(var)
    assert 'thirty' in var


def test_credit_card_bank_details(setup):
    print("This is my credit card bank details")

@pytest.mark.usefixtures("setup")
def test_cross_browser(crossBrowser):
    print(crossBrowser[1])

