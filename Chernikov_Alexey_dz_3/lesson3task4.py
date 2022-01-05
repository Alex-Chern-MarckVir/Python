def thesaurus_adv(*args):
    """ a function that takes as arguments strings in the format
        "First Name Last Name" and returning a dictionary in
        which the keys are the first letters of the last names,
        and the values are dictionaries """
    dict_for_last_names = {}
    for j in args:
        fst, snd = j[:j.index(' ')], j[j.index(' ') + 1:]
        if snd[0] in dict_for_last_names:
            if fst[0] in dict_for_last_names[snd[0]]:
                dict_for_last_names[snd[0]][fst[0]].append(j)
            else:
                dict_for_last_names[snd[0]].setdefault(fst[0], [j])
        else:
            dict_for_last_names.setdefault(snd[0], {fst[0]: [j]})
    return dict_for_last_names


help(thesaurus_adv)
result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)
for i in result:
    print(i + ":", result.get(i))
