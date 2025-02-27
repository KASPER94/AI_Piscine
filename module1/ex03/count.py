import argparse
import sys

def text_analyzer():
    parser = argparse.ArgumentParser(description="Check if a number is even, odd, or zero")
    parser.add_argument('line', nargs='?', help="text to analyze")
    args = parser.parse_args()
        
    if not args.line:
        print("What is the text to analyse?")
        print(">> ", end="")
        sys.stdout.flush()
        args.line = sys.stdin.readline().strip()

        upper = 0
        lower = 0
        punct = 0
        space = 0

        for char in args.line:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char in '.,!?;:':
                punct += 1
            elif char == ' ':
                space += 1
        
        print(f"Uppercase letters: {upper}")
        print(f"Lowercase letters: {lower}")
        print(f"Punctuation marks: {punct}")
        print(f"Spaces: {space}")

def main():
    text_analyzer()

if __name__ == "__main__":
    main()