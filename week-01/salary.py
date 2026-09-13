def main():
    monthly = float(input("Monthly salary: ").removesuffix("€"))
    yearly_12 = annual_salary(monthly, 12)
    yearly_14 = annual_salary(monthly, 14)
    print(f"{yearly_12:,.2f}€ per year in 12 payments, {yearly_14:,.2f}€ in 14.")


def annual_salary(monthly, payments):
    return monthly * payments


main()
