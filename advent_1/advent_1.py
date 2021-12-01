def part_2(data):
    count = 0
    for i in range(len(data) - 3):
        if sum(data[i:i + 3]) < sum(data[i + 1:i + 4]):
            count += 1
    print(count)


def part_1(data):
    count = 0
    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            count += 1
    print(count)


def parse(data):
    pass


with open('inputs.txt', 'r') as fh:
    data = [int(x) for x in fh]
    part_1(data)
    part_2(data)