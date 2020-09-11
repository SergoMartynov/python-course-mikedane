year = 1999
year_string = str(year)


def year_function():
    if len(year_string) == 1 or len(year_string) == 2:
        century = 1
        print(century)
    else:
        century = int(year_string[:-2]) + 1
        print(century)


year_function()
