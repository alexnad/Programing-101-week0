from prime_factorization import prime_factorization


def simplify_fraction(fraction):
    nominator = prime_factorization(fraction[0])
    denominator = prime_factorization(fraction[1])

    nominator = {key: value for key, value in nominator}
    denominator = {key: value for key, value in denominator}

    redusor = 0
    for key in nominator:
        if key in denominator:
            redusor += key ** min(nominator[key], denominator[key])

    if redusor == 0:
        redusor = 1

    return (fraction[0]/redusor, fraction[1]/redusor)
