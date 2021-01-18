def make_pretty(func):
    def inner():
        print('I got decorated')
        func()
    return inner

def ordinary():
    print('I am ordinary')

@make_pretty
def ordinary2():
    print('I am ordinary')

#µ
def work_for_all(func)
    def inner(*args, *kwargs):
        print('I can decorate any function')
        return func(*args, *kwargs)

if __name__ == "__main__":
    # ordinary()
    # pretty = make_pretty(ordinary)
    # pretty()
    ordinary2()