from fnmatch import *
def f(n):
    s = 0
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if is_prime(i):
                s +=i
            if is_prime(n//i):
                s +=n//i
    return s


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    k = 0
    for i in range(1_325_000-1, 1, -1):
        ss = f(i)
        if ss != 0 and ss <= 30000 and ss % 5 == 0:
            print(i)
            k += 1
        if k == 5:
            break

if __name__ == '__main__':
    main()

print(f(10))

# 1324994
# 1324992
# 1324991
# 1324986
# 1324980