

def acronym(phrase):
    lists = phrase.split()
    s = ''
    for i in lists:
        s = s + i[0].upper()
    return s


phrase = input()
print(acronym(phrase))
