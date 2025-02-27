
def kata1():
    languages:tuple = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
    if isinstance(languages, tuple) and len(languages) == 0:
        print("Dictionary is empty.")
    for x in languages:
        print("{} was created by {}".format(x, languages[x]))

def main():
    kata1()

if __name__ == "__main__":
    main()