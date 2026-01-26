from fnmatch import *
def f(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if i % n == 0:
            s.add(i)
            s.add(n//i)
    return s

def main():
    for i in range(2023, 10 ** 10, 2023):
        if fnmatch(str(i), '1?5719*6') and i % 2023 == 0:
            print(i, i//2023)


if __name__ == '__main__':
    main()