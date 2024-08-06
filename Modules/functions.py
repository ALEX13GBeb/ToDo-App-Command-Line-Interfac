def read_file(filepath):
    with open(filepath, "r") as file:
        list_read = file.readlines()
    return list_read


def write_file(list,filepath):
    with open(filepath, "w") as file:
        file.writelines(list)


def append_file(appendix,filepath):
    with open(filepath, 'a') as file:
        file.writelines(appendix)

