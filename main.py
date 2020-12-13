
def main(*args):
    print(sum(args))

def status(par):
    print(type(par))


if __name__ == '__main__':
    main(*[5, 10, 51, 125])
