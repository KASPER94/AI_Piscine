
def kata4():
    t:tuple = (0, 4, 132.42222, 10000, 12345.67)

    if (len(t) >= 5):
        print("module_0{}, ex_0{} : {:.2f}, {:.2e}, {:.2e}".format(t[0], t[1], t[2], t[3], t[4]))
    else:
        print("Tuple needs at least five parameters.")

def main():
    kata4()

if __name__ == "__main__":
    main()