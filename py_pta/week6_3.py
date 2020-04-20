def acronym(phrase):
    list_phrase = phrase.split()
    str_phrase = ""
    for i in list_phrase:
        str_phrase += i[0]
    return str_phrase.upper()


phrase = input()
print(acronym(phrase))
