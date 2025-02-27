import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Check if a number is even, odd, or zero")
    parser.add_argument('line', nargs=2, help="text to analyze")
    args = parser.parse_args()

    try:
        num1 = int(args.line[0])
        num2 = int(args.line[1])
    except ValueError:
        print("AssertionError: only integers")
        exit(1)

    print("Sum: {}".format(num1 + num2))
    print("Difference: {}".format(num1 - num2))
    print("Product: {}".format(num1 * num2))
    if not num2 == 0:
        print("Quotient: {}".format(num1 / num2))
        print("Remainder: {}".format(num1 % num2))
    else:
        print("ERROR (division by zero)")
        print("ERROR (modulo by zero)")

if __name__ == "__main__":
    main()