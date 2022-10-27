from random import randint


def parse(str):
    indices = []
    values = []
    for char in str.split():
        if len(indices) < 1:
            indices = char.replace("(", "").replace(")", "").split(",")
        else:
            values = char.replace("(", "").replace(")", "").split(",")

    return [indices, values]


def SAT():
    X = []
    for i in range(20):
        X.append(randint(0, 1))

    f = open("3SAT.txt", "r")

    Y = 0
    for i in f:
        p = parse(i)
        indices = p[0]
        values = p[1]
        counter = 0
        for j in range(len(indices)):
            if X[int(indices[j]) - 1] == int(values[j]):
                counter += 1
        if counter == 3:
            Y += 1
    return 20 - Y


def main():
    Z = 0
    for i in range(20):
        sat_value = SAT()
        Z += sat_value
        print(f"{sat_value}, ", end="")
    print(Z/20)


if __name__ == '__main__':
    main()
