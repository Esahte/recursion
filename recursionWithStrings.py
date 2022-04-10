"""
create a function that takes a string and returns a string with the first and last characters swapped
"""


def reverseString(s):
    if len(s) <= 1:
        return s
    else:
        return reverseString(s[1:]) + s[0]


'''
create a main function to test the above function
'''


def main():
    s = "Hello"
    print(reverseString(s))


if __name__ == "__main__":
    main()
