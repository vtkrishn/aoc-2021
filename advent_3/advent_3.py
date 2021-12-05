def part_2(data):
    s = data
    for k in range(len(data[0])):
        m = {'0': 0 ,'1': 0}
        for entry in data:
            m[entry[k]] += 1
        if m['0'] > m['1']:
            s = [i for i in s if i[k] == '0']
        else:
            s = [i for i in s if i[k] == '1']
        if len(s) == 2:
            s = [s[1] if s[1][-1] == '1' else s[0]]
        if len(s) == 1:
            break
    oxygen = int(''.join(s[0]), 2)

    t = data
    for k in range(len(data[0])):
        m = {'0': 0, '1': 0}
        for entry in data:
            m[entry[k]] += 1
        if m['0'] > m['1']:
            t = [i for i in t if i[k] == '1']
        else:
            t = [i for i in t if i[k] == '0']
        if len(t) == 2:
            t = [t[1] if t[1][-1] == '0' else t[0]]
        if len(t) == 1:
            break

    co2 = int(''.join(t[0]), 2)
    print(oxygen * co2)


def part_1(data):
    s = []
    t = []
    for k in range(len(data[0])):
        m = {'0': 0 ,'1': 0}
        for entry in data:
            m[entry[k]] += 1

        if m['0'] > m['1']:
            s.append('0')
            t.append('1')
        else:
            s.append('1')
            t.append('0')

    gamma = int(''.join(s), 2)
    epsilon = int(''.join(t), 2)
    print(gamma * epsilon)




def parse(data):
    for line in open('inputs.txt'):
        line = line.strip()
        for i,c in enumerate(line):
            if c == '1':
                v1[i] += 1
            else:
                v0[i] += 1

# for line in open('inputs.txt'):
#     line = line.strip()
#     for i,c in enumerate(line):
#         print(c)

v0={}
v1={}
with open('inputs.txt', 'r') as fh:
    d = fh.read()#.splitlines()
    data = parse(d)
    print(data)

    # data = [
    #     '00100',
    #     '11110',
    #     '10110',
    #     '10111',
    #     '10101',
    #     '01111',
    #     '00111',
    #     '11100',
    #     '10000',
    #     '11001',
    #     '00010',
    #     '01010'
    # ]

    #part_1(data)
    #part_2(data)