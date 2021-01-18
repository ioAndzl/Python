def make_multiplier_of(n):
    def multiplier(x):
        return x**n
    return multiplier

if __name__ == "__main__":
    times3 = make_multiplier_of(3)
    print(times3(2))
    #µ times3.__closure__[0].cell_contents
    #print(times3.__closure__[0].cell_contents)