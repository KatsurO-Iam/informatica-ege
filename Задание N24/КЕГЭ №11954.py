s = open('24_11954.txt').readline()
s = s.replace('T','@')
s=s.replace('U','#')
s=s.replace('V','$')
s=s.replace('W','%')
s=s.replace('Z','&')
minn = float('inf')
for i in s.split('Y'):
    if i.count('X') >= 500:
        if minn > len(i):
            minn = min(len(i), minn)
        print(len(i))
        print(i)
print(minn) #ответ 68500, нужно убрать лишние справа и слева по одному и так как у нас 505 иксов можно убрать еще 5
