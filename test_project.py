from project import personal_allowance, taxable_income_calc, income_tax, national_insurance

def test_personal_allowance():
    assert personal_allowance(100000) == 12570
    assert personal_allowance(125141) == 0
    assert personal_allowance(100002) == 12569


#def test_taxable_income_calc():


#def test_income_tax():


#def test_national_insurance():