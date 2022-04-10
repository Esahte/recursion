def main():
    lt = [x for x in range(1, 10)]
    print(binarySearch(lt, 1))


def binarySearch(lst, x):
    mid = lst[len(lst) // 2]
    index = lst.index(mid)
    if mid == x:
        return mid
    elif mid < x:
        return binarySearch(lst[index + 1:], x)
    return binarySearch(lst[:index], x)


if __name__ == "__main__":
    main()
