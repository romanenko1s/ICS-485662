def func():
    x = 0
    while x < 1000:
        yield x
        x+=7
    print("Я воскрес, дякую")

while True:
    userinput = str(input("Я "))

    if userinput == "на чілі":
        for x in func():
            print(x)

    if userinput == "гуль":
        print("АХЇХАЇХААХХАХАЇАХЇАХ ГУЛЬ\nІДИ УРОКИ ВЧИ ШКІЛА")

    else:
        print("Ок, так і запишем")

    print("")