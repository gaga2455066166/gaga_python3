a = input()
b = input()


def CountAa(s):
    return s.lower().count(b)


if __name__ == "__main__":
    s = a
    print(CountAa(s))