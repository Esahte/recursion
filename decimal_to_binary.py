def main():
    no = 233
    print(findBinary(no))


def findBinary(num):
    if num == 0:
        return []
    return findBinary(num // 2) + [num % 2]


if __name__ == '__main__':
    main()
