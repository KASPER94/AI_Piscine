
def kata():
    t:tuple = (19, 42, 21)

    if isinstance(t, tuple) and len(t) == 0:
        print("There are no numbers.")
    elif isinstance(t, int):
        print("The number is: {}".format(t))
    elif len(t) > 1:
        s = "{}".format(t[0])
        i = 1
        while i < len(t):
            s += ", {}".format(t[i])
            i+= 1
        print("The {} numbers are: {}".format(i, s))

def main():
    kata()

if __name__ == "__main__":
    main()