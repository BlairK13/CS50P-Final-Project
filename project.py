'''
Program calculates the income tax, personal allowance and national insurance tax for the UK tax year 2023/24 (April 2023 - April 2024).
'''

def main():
    while True:
        try:
            income = float(input("Enter your income: "))

            if income >= 0:

                income_tax_calc, income_tax_in_each_band, taxable_income = income_tax(income)
                national_insurance_calc, national_insurance_tax_in_each_band = national_insurance(income)
                personal_allowance_calc = personal_allowance(income)
                total_tax = income_tax_calc + national_insurance_calc

                result_summary = (
                    f"\nResults Summary:\n"
                    f"-------------------------\n"
                    f"Your income before tax is: £{income:.2f}\n"
                    f"Your taxable income is: £{taxable_income:.2f}\n"
                    f"\nTax Calculation: \n"
                    f"Basic Rate: £{income_tax_in_each_band['BasicRate']:.2f}\n"
                    f"Higher Rate: £{income_tax_in_each_band['HigherRate']:.2f}\n"
                    f"Additional Rate: £{income_tax_in_each_band['AdditionalRate']:.2f}\n"
                    f"Total Income Tax: £{income_tax_calc:.2f}\n"
                    f"\nNational Insurance Calculation: \n"
                    f"12% Rate: £{national_insurance_tax_in_each_band['TwelvePer_Rate']:.2f}\n"
                    f"2% Rate: £{national_insurance_tax_in_each_band['TwoPer_Rate']:.2f}\n"
                    f"Total National Insurance: £{national_insurance_calc:.2f}\n"
                    f"\nPersonal Allowance: \n"
                    f"\nPersonal Allowance: £{personal_allowance_calc:.2f}\n"
                    f"\nTotal Tax Calculation: \n"
                    f"Total Tax: £{total_tax:.2f}\n"
                    f"Total Tax as a percentage of your income: {total_tax/income*100:.1f}%\n"
                    f"\nTake-home pay: \n"
                    f"Take-home pay: £{income - total_tax:.2f}\n"
                )

                print(result_summary)

            else:
                print("Please enter a positive valid number.")

        except ValueError:
            print("Please enter a valid number.")

        except KeyboardInterrupt:
            print("\n Program terminated by the user.")
            break

        else:
            break


def personal_allowance(income):

    if income <= 100000:
        personal_allowance = 12570

    elif income > 100000 and income <= 125140:
        personal_allowance = 12570 - (income - 100000)/2

    else:
        personal_allowance = 0

    return personal_allowance

def taxable_income_calc(income):

    personal_allowance_calc = personal_allowance(income)

    taxable_income = income - personal_allowance_calc

    return taxable_income


def income_tax(income):
    '''
    Calculate income tax based on UK tax bands for 2022/23
    '''

    'Define indicies for tax bands and defne the tax bands and rates'

    BASIC_RATE = 0
    HIGHER_RATE = 1
    ADDITIONAL_RATE = 2

    tax_bands = [12570, 50270, 125140]
    tax_rates = [0.2, 0.4, 0.45]

    'Calculate the taxable income using taxable_income_calc()'

    taxable_income = taxable_income_calc(income)

    'Initialise variables for the total tax and the tax in each band'

    total_tax = 0

    income_tax_in_each_band = {
        'BasicRate': 0,
        'HigherRate': 0,
        'AdditionalRate': 0
    }

    '''
    Calculate tax for the basic rate
    '''
    basic_rate_limit = tax_bands[HIGHER_RATE] - tax_bands[BASIC_RATE]

    if taxable_income <= basic_rate_limit:
        income_tax = taxable_income * tax_rates[BASIC_RATE]
        income_tax_in_each_band['BasicRate'] = income_tax
        total_tax += income_tax
    else:
        income_tax = basic_rate_limit * tax_rates[BASIC_RATE]
        income_tax_in_each_band['BasicRate'] = income_tax
        total_tax += income_tax

    '''
    Calculate tax for the higher rate
    '''
    higher_rate_limit = tax_bands[ADDITIONAL_RATE] - tax_bands[HIGHER_RATE]

    if basic_rate_limit < taxable_income <= tax_bands[ADDITIONAL_RATE]:
        income_tax = (taxable_income - basic_rate_limit) * tax_rates[HIGHER_RATE]
        income_tax_in_each_band['HigherRate'] = income_tax
        total_tax += income_tax
    elif taxable_income > tax_bands[ADDITIONAL_RATE]:
        income_tax = higher_rate_limit * tax_rates[HIGHER_RATE]
        income_tax_in_each_band['HigherRate'] = income_tax
        total_tax += income_tax

    '''
    Calculate tax for the additional rate
    '''
    if taxable_income > tax_bands[2]:
        income_tax = (taxable_income - tax_bands[ADDITIONAL_RATE]) * tax_rates[ADDITIONAL_RATE]
        income_tax_in_each_band['AdditionalRate'] = income_tax
        total_tax += income_tax

    return total_tax, income_tax_in_each_band, taxable_income


def national_insurance(income):

    PRIMARY_THRESHOLD = 0
    UPPER_EARNINGS_THRESHOLD = 1

    ni_bands = [12570, 50270]
    ni_rates = [0.12, 0.02]

    national_insurance_income = income

    primary_rate_limit = ni_bands[UPPER_EARNINGS_THRESHOLD] - ni_bands[PRIMARY_THRESHOLD]

    national_insurance_tax = 0
    national_insurance_tax_in_each_band = {'TwelvePer_Rate': 0,
                                            'TwoPer_Rate': 0}

    if ni_bands[PRIMARY_THRESHOLD] < national_insurance_income <= ni_bands[UPPER_EARNINGS_THRESHOLD]:
        national_insurance_tax = (national_insurance_income - ni_bands[PRIMARY_THRESHOLD]) * ni_rates[PRIMARY_THRESHOLD]
        national_insurance_tax_in_each_band['TwelvePer_Rate'] = national_insurance_tax

    if national_insurance_income > ni_bands[UPPER_EARNINGS_THRESHOLD]:
        primary_tax_portion = (primary_rate_limit) * ni_rates[PRIMARY_THRESHOLD]
        additional_tax_portion = (national_insurance_income - ni_bands[UPPER_EARNINGS_THRESHOLD]) * ni_rates[UPPER_EARNINGS_THRESHOLD]

        national_insurance_tax = primary_tax_portion + additional_tax_portion

        national_insurance_tax_in_each_band['TwelvePer_Rate'] = primary_tax_portion
        national_insurance_tax_in_each_band['TwoPer_Rate'] = additional_tax_portion

    return national_insurance_tax, national_insurance_tax_in_each_band

if __name__ == "__main__":
    main()