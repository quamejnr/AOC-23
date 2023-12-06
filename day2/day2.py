from collections import defaultdict
from functools import reduce
import re

###########
# DAY 2A  #
###########
def cube_conundrum_a(input):
    with open(input) as f:
        sum = 0
        for idx, line in enumerate(f):
            _, outcomes = line.split(": ")
            words = re.findall("\w+", outcomes)
            i = iter(words)
            items = tuple(zip(i, i))
            if all([is_valid(item) for item in items]):
                sum += (idx + 1)

    return sum



def is_valid(item):
    valid_items = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    max_num = valid_items[item[-1]]
    return int(item[0]) <= max_num

###########
# DAY 2B  #
###########

def cube_conundrum_b(input):
    with open(input) as f:
        sum = 0
        for line in f:
            _, outcomes = line.split(": ")
            words = re.findall("\w+", outcomes)
            i = iter(words)
            items = tuple(zip(i, i))
            max_values = get_max_values(items)
            sum += reduce((lambda x, y: x * y), max_values)

    return sum

def get_max_values(items):
    d = defaultdict(int)
    for item in items:
        color, num = item[1], int(item[0])
        d[color] = max(d[color], num)

    return d.values()


