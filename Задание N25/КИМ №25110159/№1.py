def f(n):
    s = set()
    for i in range(int(n**0.5), int(n**0.5) - 110, -1):
            if n % i == 0 and (n// i) - i <= 110:
                s.add(n//i)
    return s

def main():
    for i in range(1_000_000, 1_500_000):
        t = f(i)
        if len(t) >=3:
            print(i, max(t))

if __name__ == '__main__':
    main()