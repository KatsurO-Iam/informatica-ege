from fnmatch import *
def f(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if i % n == 0:
            s.add(i)
            s.add(n//i)
    return s

def main():
    for i in range(53, 10 ** 7 + 1, 53):
        if str(i) == str(i)[::-1]:
            if fnmatch(str(i), '*2?2*'):
                k = f(i)
                if len(k) > 30:
                    print(i, sum(k))

if __name__ == '__main__':
    main()