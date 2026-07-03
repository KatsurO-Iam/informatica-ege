def f(s,e):
    if s > e:
        return 0
    if s == e:
        return 1
    if len(str(s)) == 2:
        if int(str(s)[0]) < int(str(s)[1]):
            return f(s + 1, e) + f(int(str(s)[1] + str(s)[0]), e)
        else:
            return f(s + 1, e)
    elif len(str(s)) == 3:
        if int(str(s)[1]) < int(str(s)[2]):
            return f(s + 1, e) + f(int(str(s)[0] + str(s)[2] + str(s)[1]), e)
        else:
            return f(s + 1, e)
    else:
        return f(s + 1, e)

print(f(100, 150))