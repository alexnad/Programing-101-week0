import sys


def main():

    filename = ''
    for arg in sys.argv:
        if '.txt' in arg:
            filename = arg

    file = open(filename, 'r')
    for arg in sys.argv:
        if arg == 'chars':
            text = file.read()
            print(len(text))

        if arg == 'words':
            words = file.read().split()
            new_lines = words.count('\n')
            print(len(words) - new_lines)

        if arg == 'lines':
            lines = file.read().split('\n')
            print(len(lines))

    file.close()

if __name__ == "__main__":
    main()
