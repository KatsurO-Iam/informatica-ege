with open('24') as f:
    s = f.read()

parts = s.split('CAT')
max_len = 0

for i in range(len(parts) - 4):
    w = 'CAT'.join(parts[i: i + 5])
    cur = w[:w.rfind('CAT') + 3]
    if cur.count('1') == 700:
        max_len = max(max_len, len(cur))

print(max_len)
#Ольга Анатольевна почему ничего не выводит?(