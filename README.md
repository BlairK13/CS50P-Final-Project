# Basic UK Income Tax Calculator - Year 2022/2023
------------------------------------------------

## Video Demo:  <https://www.youtube.com/watch?v=e8Yobw74m0A&ab_channel=BlairKirkland>

## Description:

The program is designed to be run from the command line and will prompt the user to enter their income. The program will then calculate the key components and display the results to the user via the commandline.

The program is for tax year 2022/2023. The tax rates and thresholds are based on the information provided by the UK government website: https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2022-to-2023

------------------------------------------------

This program calculates the key components that make up the UK tax system. These are personal allowance, taxable income, income tax and national insurance.

The key components are detailed in different functions to aid the calculation of the various items.

These are:

- personal_allowance()
- taxable_income_calc()
- income_tax()
- national_insurance()

The functions all accept the users income as an argument and return the relevant value.

The output from personal_allowance() is a integer value or float value.

The output from taxable_income_calc() is a integer value or float value.

The output from income_tax() is a tuple containing the income tax amount, a dictionary that details how much tax is paid at each rate and taxable income.

The output from national_insurance() is a tuple containing the national insurance amount and a dictionary that details how much tax is paid in each band.

The program then uses the returned values to calculate the tax for the year and displays the results to the user.

### Personal Allowance:

The personal allowance is the amount of income you can earn before you start paying income tax. The personal allowance is currently £12,570. The personal allowance is reduced by £1 for every £2 earned over £100,000. This means that anyone earning over £125,140 will not receive a personal allowance.

### Taxable Income:

Taxable income is the amount of income you have left after you have deducted your personal allowance. This is the amount that you will pay income tax on.

### Income Tax:

Income tax is the amount of tax you pay on your taxable income. The amount of income tax you pay depends on how much you earn. The tax rates are as follows:

- 20% on taxable income between £12,571 and £50,270
- 40% on taxable income between £50,270 and £125,140
- 45% on taxable income over £125,140


### National Insurance:

National insurance is a tax on earnings. The amount of national insurance you pay depends on how much you earn. The tax rates are as follows:

- 12% on earnings between £12,570 and £50,270
- 2% on earnings over £50,270
------------------------------------------------

## Installation:

The program is written in Python 3.9.5 and requires no additional libraries to be installed.
