def tax_calc(medicine_sales, makeup_sales, other_sales):
    medicine_profit = medicine_sales * 15.19 / 100
    makeup_profit = makeup_sales * 16 / 100
    other_profit = other_sales * 20 / 100
    total_profit = medicine_profit + makeup_profit + other_profit
    total_income = medicine_sales + makeup_sales + other_sales
    outcome = total_income * 7.5 / 100
    net = total_profit - outcome
    if net <= 5000:
        total_tax = 0
    else:
        tax1 = first_tax(net)
        tax2 = second_tax(net)
        tax3 = third_tax(net)
        total_tax = tax1 + tax2 + tax3
    return total_tax


def first_tax(net):
    tax = 0
    if net > 20000:
        tax = (20000 - 5000) * 10 / 100
    elif net <= 20000:
        tax = (net - 5000) * 10 / 100
    return tax


def second_tax(net):
    tax = 0
    reminder_net = net - 20000
    if reminder_net >= 0:
        if reminder_net > 20000:
            tax = 20000 * 15 / 100
        elif net <= 20000:
            tax = reminder_net * 15 / 100
    return tax


def third_tax(net):
    tax = 0
    reminder_net = net - 40000
    if reminder_net >= 0:
        if reminder_net > 20000:
            tax = 20000 * 20 / 100
        elif net <= 20000:
            tax = reminder_net * 20 / 100
    return tax


medicine_sales = int(input("Medicine and Baby Milk Sales: "))
makeup_sales = int(input("Makeup and Accessories Sales: "))
other_sales = int(input("Other Sales: "))
overall_tax = tax_calc(medicine_sales, makeup_sales, other_sales)
print(overall_tax)
