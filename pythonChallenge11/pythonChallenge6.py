# Write a function that removes repeated characters from a string.
# Sample strings are: a Hello: output should be Helo
# b. Concatenate: output should be Conaten


def fix(string):
    s = set()
    list = []
    for ch in string:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)


string = "Hello"
print(fix(string))


def fix(string1):
    s = set()
    list = []
    for ch in string1:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)


string1 = "Concatenate"
print(fix(string1))
