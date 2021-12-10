def part_2(data):
    l = []
    k = 0
    flag = False
    t = []
    for i in data:
        for j in i.strip():
            if j in ['(', '{', '[', '<']:
                l.append(j)
            elif j == ')':
                if l[-1] != '(':
                    k += 3
                    flag = True
                    break
                else:
                    l.pop()
            elif j == ']':
                if l[-1] != '[':
                    k += 57
                    flag = True
                    break
                else:
                    l.pop()
            elif j == '}':
                if l[-1] != '{':
                    k += 1197
                    flag = True
                    break
                else:
                    l.pop()
            elif j == '>':
                if l[-1] != '<':
                    k += 25137
                    flag = True
                    break
                else:
                    l.pop()
        if not flag:
            s = 0
            p = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}
            for i in reversed(l):
                s = s*5 + p[i]
            t.append(s)

    t.sort()
    print(t[len(t)//2])



def part_1(data):
    l = []
    k = 0
    for i in data:
        for j in i.strip():
            if j in ['(','{','[','<']:
                l.append(j)
            elif j == ')':
                if l[-1] != '(':
                    k += 3
                    break
                else: l.pop()
            elif j == ']':
                if l[-1] != '[':
                    k += 57
                    break
                else: l.pop()
            elif j == '}' :
                if l[-1] != '{':
                    k += 1197
                    break
                else:
                    l.pop()
            elif j == '>':
                if l[-1] != '<':
                    k += 25137
                    break
                else:
                    l.pop()
    print(k)


def parse(data):
    return data


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)