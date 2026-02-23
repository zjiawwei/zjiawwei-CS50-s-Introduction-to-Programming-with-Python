mouths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date:")
        if '/' in date:
            x, y, z = date.split('/')
            x = int(x)
            y = int(y)
            z = int(z)
            if 1 <= x <= 12 and 1 <= y <= 31:
                print(f"{z}-{x:02}-{y:02}")
                break
        elif ',' in date:
            mouths_name, day_year = date.split(' ',1)
            day, year = day_year.split(',')
            day = int(day)
            year = int(year)
            if mouths_name in mouths and 1 <= day <= 31:
                mouths = mouths.index(mouths_name) + 1
                print(f"{year:04}-{mouths:02}-{day:02}")
                break
    except (ValueError,IndexError):
        pass