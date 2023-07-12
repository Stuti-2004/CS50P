
glist = {}
n = 1

while True:
    try:
        item = input("")

        if item in glist:
            #print("IN LIST")
            glist[item] += 1
            #print(list)
        else:
            n = 1
            glist.update({item: n})
            #print(list)

    except EOFError:
        myKeys = list(glist.keys())
        myKeys.sort()
        sorted_dict = {i: glist[i] for i in myKeys}

        for i in sorted_dict:
            print(sorted_dict[i], i.upper())
        break

    except KeyError:
        pass