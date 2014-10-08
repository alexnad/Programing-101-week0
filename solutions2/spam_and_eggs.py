def prepare_meal(number):
    meal = []
    while number % 3 == 0:
        number /= 3
        meal.append('spam')

    if number % 5 == 0:
        if meal:
            meal.append('and')
        meal.append('eggs')

    prepeared_meal = ' '.join(meal)
    return prepeared_meal
