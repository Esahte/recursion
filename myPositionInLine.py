def getMyPositionInLine(line, name):
    """
    Returns the position of the name in the line.
    """
    if line == name:
        return 0
    elif line[0] == name:
        return 1
    else:
        return getMyPositionInLine(line[1:], name) + 1


''' create a main function to test the above function '''


def main():
    line = "This is a line of text.".split()
    name = "line"
    print(getMyPositionInLine(line, name))


if __name__ == "__main__":
    main()
