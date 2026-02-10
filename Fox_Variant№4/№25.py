from fnmatch import *

def main():
    for i in range(33, 10 ** 8, 33):
        if fnmatch(str(i), '13*02?87') and i % 33 == 0:
            print(i, i//33)


if __name__ == '__main__':
    main()