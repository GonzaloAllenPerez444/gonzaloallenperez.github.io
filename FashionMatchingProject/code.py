import data

#starting = input("please select if you want to start with a Shirt (0) , Pants (1), or shoes (2)")
#starting = int(starting)
proper = data.proper


def clothes(color, item=0):
    your_list = []
    for outfit in data.master_list:

        if color == outfit[item]:
            your_list.append(outfit)
    # print(your_list)
    fancy_list = []
    for items in your_list:
        proper2 = iter(proper)

        fancy_list.append(("outfit option:"))
        for cloth in items:
            fancy_list.append((cloth, next(proper2)))
    return fancy_list

#color_input = input("pick a color of attire: ")
#clothes(color_input)