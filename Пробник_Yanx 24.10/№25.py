from fnmatch import *
def f(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if i % n == 0:
            s.add(i)
            s.add(n//i)
    return s

def main():
    for i in range(96437, 10 ** 10, 96437):
        if fnmatch(str(i), '7?2*4??9.txt?'):
            print(i, i // 96437)
if __name__ == '__main__':
    main()