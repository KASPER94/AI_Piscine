
def kata2():
    t:tuple = (2019, 9, 25, 3, 30)
    if isinstance(t, tuple) and len(t) == 0:
        print("There are no numbers.")
    m = ""
    d = ""
    y = ""
    h = ""
    min = ""
    if (len(t) >= 5):
        if t[1] < 10:
            m = "0"
        if t[2] < 10:
            d = "0"
        if t[0] < 1000:
            y = "0"
        if t[0] < 100:
            y = "00"
        if t[0] < 10:
            y = "000"
        if t[3] < 10:
            h = "0"
        if t[4] < 10:
            min = "0"
        print("{}{}/{}{}/{}{} {}{}:{}{}"
            .format(m, t[1], d, t[2], y, t[0], h, t[3], min, t[4]))
    else:
        print("Tuple needs at least five parameters.")

def main():
    kata2()

if __name__ == "__main__":
    main()