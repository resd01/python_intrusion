import os

def fibonacci(limit):
    res = 0
    x   = 0
    y   = 1
    while res < limit:
        print res
        res = x + y
        x   = y
        y   = res

def main():
    os.system('cls')
    print """
    +--------------------------------------------+
    |   ____  __  ____   __     ____     __      |
    |  (  __)(  )(  _ \\ /  \\   (___ \\   /  \\     |
    |   ) _)  )(  ) _ ((  O )   / __/ _(  0 )    |
    |  (__)  (__)(____/ \\__/   (____)(_)\\__/     |
    |                                            |
    |  > Author:  Glenn Le Gac                   |
    +--------------------------------------------+
    """
    fibonacci(int(raw_input("Limit: ")))

main()
