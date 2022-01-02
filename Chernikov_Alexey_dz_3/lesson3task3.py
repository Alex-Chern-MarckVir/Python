def thesaurus(*args):
    """ a function that takes names or words as arguments
     and returns a dictionary in which the keys are the first letters of the names,
      and the values are lists containing names starting with the corresponding letter """
    dict_for_names = {}
    for i in args:
        if i[0] in dict_for_names:
            dict_for_names[i[0]].append(i)
        else:
            dict_for_names[i[0]] = [i]
    return dict_for_names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
