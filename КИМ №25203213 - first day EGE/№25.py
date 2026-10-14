def f(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return [i]+f(n//i)
    return [n]
k = 0
for i in range(2_626_695_892, 2_726_695_892):
    t = f(i)
    if len(t) > 0:
        if len(t) == 2:
            if str(t[0]).count('67') == 1 and str(t[1]).count('67') == 1:
                print(i, min(t), t)
                k +=1
        elif len(t) == 1:
            if t[0] * t[0] == i:
                if str(t[0]).count('67') == 1:
                    print(i, min(t), t)
                    k+=1
    if k == 5:
        break