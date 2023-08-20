from project import personal_allowance, taxable_income_calc, income_tax, national_insurance

def test_personal_allowance():
    assert personal_allowance(100000) == 12570
    assert personal_allowance(125141) == 0
    assert personal_allowance(100002) == 12569
    assert personal_allowance(34000) == 12570


def test_taxable_income_calc():
    assert taxable_income_calc(100000) == (100000 - 12570)
    assert taxable_income_calc(125141) == (125141 - 0)
    assert taxable_income_calc(100002) == (100002 - 12569)
    assert taxable_income_calc(34000) == (34000 - 12570)


def test_national_insurance():
    assert national_insurance(100000) == (5518.60, {'TwelvePer_Rate': 4524.0, 'TwoPer_Rate': 994.6})
    assert national_insurance(125141) == (6021.42, {'TwelvePer_Rate': 4524.0, 'TwoPer_Rate': 1497.42})
    assert national_insurance(100002) == (5518.64, {'TwelvePer_Rate': 4524.0, 'TwoPer_Rate': 994.64})
    assert national_insurance(34000) == (2571.60, {'TwelvePer_Rate': 2571.6, 'TwoPer_Rate': 0})



def test_income_tax():
    assert income_tax(100000) == (27432.0, {'BasicRate': 7540.0, 'HigherRate': 19892.0, 'AdditionalRate': 0}, 87430)
    assert income_tax(125141) == (37488.45, {'BasicRate': 7540.0, 'HigherRate': 29948.0, 'AdditionalRate': 0.45}, 125141)
    assert income_tax(100002) == (27433.2, {'BasicRate': 7540.0, 'HigherRate': 19893.2, 'AdditionalRate': 0}, 87433.0)
    assert income_tax(34000) == (4286.0, {'BasicRate': 4286.0, 'HigherRate': 0, 'AdditionalRate': 0}, 21430)
