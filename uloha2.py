def fun(ret:str)->str:
    num=''
    for c in ret:
        if c.isdigit():
            num=num + c
    print("cisla v retazci:", num)
    str(num)
    print("pocet cisel v retazci:", len(num))

fun("Na farme mame od roku 2012 12 kráv a 230 oviec.")
fun("Skutok sa stal.")
fun("snehulienka a 7 trpazlikov.")

