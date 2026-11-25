#M11.p3       Nick     11/19

def calculateSalesReport(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05

    nextYearTarget = sales * 0.05
    return commission, nextYearTarget


def main():
    lastName = input("Enter salesperson's last name: ")
    sales = float(input("Enter sales amount: "))

    commission, nextYearTarget = calculateSalesReport(sales)

    print(f"Salesperson Last Name: {lastName}")
    print(f"Commission: ${commission:.2f}")
    print(f"Next Year's Target: ${nextYearTarget:.2f}")


main()
