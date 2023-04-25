import os


def my_note(main_switcher, name):
    """
    This function is DIY word. you can create yur file, read it, write an info into it  rename file, delete file.
    examples:
        q = my_note('write','test3')  -creating and writing mode
        q = my_note('read','test3')  - reading mode
        q(switcher='append', word='___Title___' ) - add info
        q(rename=['test3', 'test4'])  - rename
        q(switcher='pprint') -printing
    """
    chosen_mode = "r"
    if main_switcher == "write":
        chosen_mode = "a"
    my_file = open(name + ".yur", mode=chosen_mode)

    def inner_func(my_file=my_file, switcher="", word="", rename=[]):
        if switcher == "append":
            if word[:3] == word[-3:] and word[:3] == "***":
                my_file.write("###" + word[3:-3] + "  ")
            elif word[:3] == word[-3:] and word[:3] == "---":
                my_file.write("_" + word[3:-3] + "_")
            elif word[:3] == word[-3:] and word[:3] == "___":
                my_file.write("<u>" + word[3:-3] + "</u>")
            else:
                my_file.write(word)
        elif switcher == "pprint":
            print(my_file.read())
        elif switcher == "delete":
            my_file.close()
            os.remove(name + ".yur")
        elif len(rename) == 2:
            my_file.close()
            os.rename(rename[0] + ".yur", rename[1] + ".yur")
            my_file = open(rename[1] + ".yur", mode="r")

    return inner_func

