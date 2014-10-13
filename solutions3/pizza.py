from time import time
from datetime import datetime


def finish(*args):
    return False


def status(*args):
    orders = args[2]
    for name in orders:
        print("{0} - {1}".format(name, orders[name]))
    return True


def take(*args):
    orders = args[2]
    name = args[1][1]
    price = args[1][2]
    if name in orders:
        orders[name] += int(price)
    else:
        orders[name] = int(price)
    return True


def save(*args):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = stamp + '.txt'
    file = open(filename, 'w')

    for name in args[2]:
        file.write('{0},{1}'.format(name, args[2][name]))
    file.close()
    args[3].append(filename)
    return True


COMMANDS = {
    'finish': finish,
    'status': status,
    'take': take,
    'save': save
    }


def main():
    flag = True
    orders = {}
    saved_orders = []
    command = []
    is_saved = False
    current_status = [command, orders, saved_orders, is_saved]

    while flag:
        command = input("Enter command>")
        current_status[0] = command.split()
        if command[0] in COMMANDS:
            flag = commands[command[0]](current_status)


if __name__ == "__main__":
    main()
