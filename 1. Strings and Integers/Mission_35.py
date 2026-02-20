# https://py.checkio.org/en/mission/convert-date/

def convert_date(date: str) -> str:

    date_without_punc = date.replace("/", " ").split()
    year = int(date_without_punc[2])
    month = int(date_without_punc[1])
    day = int(date_without_punc[0])

    if len(date_without_punc) >= 4:
        return "Error: Invalid date."
    elif ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and (month == 2):
        if day > 1 and day < 30:
            new_date = date_without_punc[::-1]
            return "-".join(new_date)
        else: 
            return "Error: Invalid date."
    elif (month == 2 and day > 28) or (month >= 13):
        return "Error: Invalid date."
    elif (month == 4 or month == 6 or month == 9 or month == 11) and (day >= 31):
        return "Error: Invalid date."
    else:
        new_date = date_without_punc[::-1]
        return "-".join(new_date)


print("Example:")
print(convert_date("29/02/2019"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")
