def main():
    n = int(input('enter a number: '))
    print(sumOfNums(n))


def sumOfNums(number):
    if number == 1:
        return 1
    return number + sumOfNums(number - 1)


if __name__ == "__main__":
    main()
