
SIGNS = [
    [20, "Capricorn"],
    [19, "Aquarius"],
    [20, "Pisces"],
    [20, "Aries"],
    [21, "Taurus"],
    [21, "Gemini"],
    [22, "Cancer"],
    [22, "Leo"],
    [23, "Virgo"],
    [22, "Libra"],
    [21, "Scorpio"],
    [20, "Sagittarius"]
]

def what_is_my_sign(day, month):
    if day <= SIGNS[month-1][0]:
        return SIGNS[month-1][1]
    else:
        return SIGNS[month%12][1]
