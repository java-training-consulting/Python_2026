# 1
# 11
# 21
# 1211
# ???

# 3
# 13
# 1113


def lesen(text):
    if len(text) == 1:
        return "1" + text

    return text


def lesenListe(param):
    pass


if __name__ == '__main__':
    text = lesen("1")
    print(text)
    text = lesen(text)
    print(text)
    text = lesen(text)
    print(text)

    text = lesen("3")
    print(text)

    liste = lesenListe([1])   # [1,1]   -> [2,1]