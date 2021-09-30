def thesaurus(*names):
    letter = {}
    for name in names:
        key = name[0].capitalize()
        if key not in letter:
            letter[key] = []
        letter[key].append(name)
    return letter


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
