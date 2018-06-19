#! /usr/bin/python3

import itertools

class SGR:
    def __init__(self, *args):
        # most stupid setup to avoid triggering any glitches in parsing
        self.data = '\033[0m'
        for arg in args:
            if type(arg) == int:
                self.data += '\033[{}m'.format(arg)
            elif type(arg) == str:
                self.data += '\033[{}m'.format(arg)

class Text:
    def __init__(self, text):
        self.data = text

def size(text):
    ret = 0
    if text is None:
        return ret
    for t in text:
        if type(t) == SGR:
            continue
        ret += len(t.data)
    return ret

def to_string(text):
    ret = ''
    if text is None:
        return ret
    for t in text:
        ret += t.data

    return ret

def main():
    teststr = "abc _ █▚"

    left = [
        [Text("normal " + teststr)],
        [Text(" faint "), SGR(2), Text(teststr)],
        [Text("normal "), Text(teststr)],
        [Text("  bold "), SGR(1), Text(teststr)],
        [],
        [Text("white on black")],
        [Text("normal "), SGR(40, 37), Text(teststr)],
        [Text(" faint "), SGR(40, 37, 2), Text(teststr)],
        [],
        [],
        [Text("colors plus B N F")],
        [Text("            "), SGR(30,1), Text('ab'), SGR(30), Text('ab'), SGR(30,2), Text('ab')],
        [Text("            "), SGR(31,1), Text('ab'), SGR(31), Text('ab'), SGR(31,2), Text('ab')],
        [Text("            "), SGR(32,1), Text('ab'), SGR(32), Text('ab'), SGR(32,2), Text('ab')],
        [Text("            "), SGR(33,1), Text('ab'), SGR(33), Text('ab'), SGR(33,2), Text('ab')],
        [Text("            "), SGR(34,1), Text('ab'), SGR(34), Text('ab'), SGR(34,2), Text('ab')],
        [Text("            "), SGR(35,1), Text('ab'), SGR(35), Text('ab'), SGR(35,2), Text('ab')],
        [Text("            "), SGR(36,1), Text('ab'), SGR(36), Text('ab'), SGR(36,2), Text('ab')],
        [Text("            "), SGR(37,1), Text('ab'), SGR(37), Text('ab'), SGR(37,2), Text('ab')],
    ]

    mid = [
        [Text("   normal " + teststr)],
        [Text("  italic  "), SGR(3), Text(teststr)],
        [Text("underline "), SGR(4), Text(teststr)],
        [Text("underlinD "), SGR(21), Text(teststr)],
        [Text(" overline "), SGR(53), Text(teststr)],
        [Text("   blink  "), SGR(5), Text(teststr)],
        [Text("  inverse "), SGR(7), Text(teststr)],
        [Text("   strike "), SGR(9), Text(teststr)],
        [Text("invisible "), SGR(8), Text(teststr)],
        [],
        [Text("B N F    B N F")],
        [SGR(90,1), Text('ab'), SGR(90), Text('ab'), SGR(90,2), Text('ab'),
            Text('   '), SGR('38;5;245',1), Text('ab'), SGR('38;5;245'), Text('ab'), SGR('38;5;245',2), Text('ab')],
        [SGR(91,1), Text('ab'), SGR(91), Text('ab'), SGR(91,2), Text('ab')],
        [SGR(92,1), Text('ab'), SGR(92), Text('ab'), SGR(92,2), Text('ab')],
        [SGR(93,1), Text('ab'), SGR(93), Text('ab'), SGR(93,2), Text('ab')],
        [SGR(94,1), Text('ab'), SGR(94), Text('ab'), SGR(94,2), Text('ab')],
        [SGR(95,1), Text('ab'), SGR(95), Text('ab'), SGR(95,2), Text('ab')],
        [SGR(96,1), Text('ab'), SGR(96), Text('ab'), SGR(96,2), Text('ab')],
        [SGR(97,1), Text('ab'), SGR(97), Text('ab'), SGR(97,2), Text('ab')],
    ]

    right = []
    r = []
    for i in ([[SGR(40+i), Text(' ')] for i in range(8)]
                +[[SGR(100+i), Text(' ')] for i in range(8)]):
        r += i
    right.append(r)
    for j in range(0, 16):
        r = []
        # SGR('48;2;{};0;0'.format(j*16+i)), SGR('48;2;{};0;0'.format(j*16+i))
        for i in ([[SGR('48;5;{}'.format(j*16+i)), Text(' ')] for i in range(16)]
                 + [[SGR(), Text('  ')]]
                 +[[SGR('38;2;{};0;0;48;2;{};0;0'.format(min((j*16+i+8),0xff), j*16+i)), Text('▄')] for i in range(16)]
                 + [[SGR(), Text(' ')]]
                 +[[SGR('38;2;{};0;0;48;2;{};0;0'.format(152+(j*2)+1, 152+(j*2))), Text('▄')] for i in range(1)]):
            r += i
        right.append(r)



    left_size = max((size(i) for i in left)) + 3
    mid_size = max((size(i) for i in mid)) + 3

    print('\033c')

    for l, m, r in itertools.zip_longest(left, mid, right):
        s = SGR().data + to_string(l) + SGR().data
        s += ' ' * (left_size - size(l))
        s += to_string(m) + SGR().data
        s += ' ' * (mid_size - size(m))

        s += to_string(r) + SGR().data

        print(s)

    print(SGR().data, end='')

if __name__ == '__main__':
    main()
