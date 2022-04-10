"""
create a function that returns True if a string is a palindrome, False otherwise.
"""


def isPalindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    return False


def main():
    word = input("Enter a word: ")
    if isPalindrome(word):
        print("{} is a palindrome".format(word))
    else:
        print("{} is not a palindrome".format(word))


if __name__ == "__main__":
    main()
