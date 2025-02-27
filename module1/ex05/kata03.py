def kata3():
    phrase:str = "The right format"

    if (len(phrase) <= 42):
        s = (42 - len(phrase)) * "-"
        print(s + phrase, end="")
    else:
        print("Phrase is too long.")

def main():
    kata3()

if __name__ == "__main__":
    main()