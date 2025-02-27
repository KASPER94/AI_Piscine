import argparse

def main():
    parser = argparse.ArgumentParser(description="args from main")
    parser.add_argument('lines', nargs="+", type=str)  
    
    ret:str = []
    args = parser.parse_args()
    for word in args.lines:
        word = word.swapcase()
        ret.append(word[::-1])
    print(" ".join(ret))


if __name__ == "__main__":
    main()