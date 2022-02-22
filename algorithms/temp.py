def excel(columnTitle):
    n = len(columnTitle)
    if not columnTitle:
        return 0
    answer = []
    x = len(columnTitle) - 1
    for i in range(n):
        current = columnTitle[i]
        position = pos(current)
        answer.append(position * pow(26, x))
        x -= 1
    
    return sum(answer)

def pos(char):
    return ord(char) - 64


if __name__ == '__main__':
    print(excel('A'))
    print(excel('AB'))
    print(excel('ZY'))
    print(excel('AAA'))
    print(excel('AAAA'))
    