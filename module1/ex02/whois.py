import argparse

def main():
    parser = argparse.ArgumentParser(description="Check if a number is even, odd, or zero")
    parser.add_argument('line', help="An integer number")
    try:
        args, unknown = parser.parse_known_args()

        if unknown:
            raise AssertionError("AssertionError: more than one argument are provided")

        if not args.line.lstrip('-').isdigit():
            raise AssertionError("AssertionError: argument is not an integer")

        num = int(args.line)

        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
