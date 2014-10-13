from time import time
from datetime import datetime


def finish(args):
    if not args['is_saved']:

        return False


def status(args):
    orders = args['orders']
    for name in orders:
        print("{0} - {1}".format(name, orders[name]))
    return True


def take(args):
    args['is_saved'] = False

    orders = args['orders']
    name = args['command'][1]
    price = args['command'][2]
    if name in orders:
        orders[name] += int(price)
    else:
        orders[name] = int(price)
    return True


def save(args):
    if not args['is_saved']:
        pass

    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = 'orders_' + stamp + '.txt'
    file = open(filename, 'w')

    for name in args['orders']:
        file.write('{0} {1}'.format(name, args['orders'][name]))
        file.write('\n')
    file.close()

    file = open('orders_list.txt', 'a')
    file.write(filename + '\n')
    file.close()

    args['is_saved'] = True
    return True


def list_orders(args):
    file = open('orders_list.txt', 'r')
    content = file.read().split('\n')
    del content[-1]
    for index, line in enumerate(content):
        print('[{0}] - {1}'.format(index + 1, line))

    return True


def load(args):
    if not args['is_saved']:
        command = input("Enter command>")
        if command == save:
            save(args)

    order = int(args['command'][1]) - 1
    new_order_list = {}

    file = open('orders_list.txt', 'r')
    content = file.read().split('\n')
    del content[-1]

    for index, line in enumerate(content):
        if index == order:
            file.close()

            file = open(line, 'r+')
            saved_orders = file.read().split('\n')
            del saved_orders[-1]

            for line in saved_orders:
                line = line.split()
                new_order_list[line[0]] = int(line[1])

            file.close()
            break
    args['orders'] = new_order_list
    return True

COMMANDS = {
    'finish': finish,
    'status': status,
    'take': take,
    'save': save,
    'list': list_orders,
    'load': load,
    }


def main():
    flag = True
    orders = {}
    command = []
    is_saved = True
    current_condition = {
        'command': command,
        'orders': orders,
        'is_saved': is_saved,
        'filename': None
        }

    while flag:
        command = input("Enter command>")
        current_condition['command'] = command.split()
        if current_condition['command'][0] in COMMANDS:
            flag = COMMANDS[current_condition['command'][0]](current_condition)


if __name__ == "__main__":
    main()
