def my_list_print(list_to_print, title):
    print(" * " + title + " {", end='')
    for x in list_to_print:
        print(x, end='')
        if x != list_to_print[-1]:
            print(',', end='')
    # for i, item in enumerate(list_to_print):
    #     if i:  # print a separator if this isn't the first element
    #         print(',', end='')
    #     print(item, end='')
    print("}")
