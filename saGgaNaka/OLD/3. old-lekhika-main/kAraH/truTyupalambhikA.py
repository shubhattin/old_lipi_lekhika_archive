from json import load

main = {}
try:
    file = open("mukhya.json", mode="r", encoding="utf-8")
    main = load(file)
    file.close()
except:
    input(
        "Errors in the database ! Can use VSCode to fix or also can be done mannualy."
    )
    exit()


class VAL:
    def __init__(self):
        self.val = ""


val = VAL()
for x in main:
    for y in main[x]:
        p = main[x][y]
        temp = set()
        l = True
        if y == "く":
            if p not in (1, 0):
                print(x, "Wrong Sanskrit mode code, Can only be 0 or 1", end="\t")
                input("fix!!!")
            continue
        if len(y) > 1 or not y.isascii():
            print("Wrong group Letter Used in ", x, y, end="\t")
            input("Remove it!!!")
        for m in p:
            if l:
                temp.add(m)
                l = False
                val.val = m
            next_chsrs = p[m][-2]
            if p[m][-1] not in (0, 1, 2):
                print("Invalid Group ID in ", x, y, m, end="\t")
                input("fix !!!")
            if len(p[m]) != 3 + (1 if p[m][-1] == 0 else 0):
                print("Invalid Group Stregnth in ", x, y, m, end="\t")
                input("fix !!!")
            for n in next_chsrs:
                if m + n not in p:
                    print(
                        "Unused 'next' chars assigned in ", x, val.val, m, n, end="\t"
                    )
                    input("Fix !!!")
                else:
                    temp.add(m + n)
        for g in p:
            if g not in temp:
                print("Character Not Mapped in ", x, val.val, g, end="\t")
                input("Fix !!!")
input("Database Checkup Finished .")
