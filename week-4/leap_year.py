def main():
    example_1 = is_simple_year(2023)
    example_2 = is_simple_year2(2023)

    print(example_1)
    print(example_2)

def is_simple_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def is_simple_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
