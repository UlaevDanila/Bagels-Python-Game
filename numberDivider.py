def numberDivider(secret):
    dividedSecret = list()

    while secret > 10:
        currentFigure = secret % 10
        dividedSecret.append(currentFigure)
        secret = secret // 10

    dividedSecret.append(secret)

    dividedSecret.reverse()

    return dividedSecret
