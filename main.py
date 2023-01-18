import random

from numberDivider import numberDivider
from gameCycle import gameCycle


def main():
    secret = random.randint(100, 999)
    dividedSecret = numberDivider(secret)
    gameCycle(True, dividedSecret, 0)


if __name__ == "__main__":
    main()
