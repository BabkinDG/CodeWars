principal = 1000 # Let P be the Principal = 1000.00
interest = 0.05  # Let I be the Interest Rate = 0.05
tax = 0.18 # Let T be the Tax Rate = 0.18
desired = 1100.00 # Let D be the Desired Sum = 1100.00


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        years += 1
        principal += principal * interest - (principal * interest * tax)
    return years
    raise NotImplementedError("TODO: calculate_years")

print(calculate_years(principal, interest, tax, desired))