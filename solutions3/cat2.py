import sys


def main():
    for arg in sys.argv[1:]:
        file_name = arg

        file = open(file_name, 'r')
        content = file.read().split('\n')

        for line in content:
            print(line)

        file.close()

if __name__ == '__main__':
    main()
