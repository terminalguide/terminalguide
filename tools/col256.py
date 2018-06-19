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

    right = []

    r = [Text('  0-15:  ')]
    for i in ([[SGR('48;5;{}'.format(i)), Text('  ')] for i in range(16)]
            ):
        r += i
    right.append(r)

    right.append([Text('     16 - 51        52 - 87       88 - 123')])

    for j in range(0, 6):
        r = []
        for i in ([[SGR('48;5;{}'.format(16 + j*6+i)), Text('  ')] for i in range(6)]
              + [[SGR(), Text("   ")]] + [[SGR('48;5;{}'.format(16 + 36 + j*6+i)), Text('  ')] for i in range(6)]
              + [[SGR(), Text("   ")]] + [[SGR('48;5;{}'.format(16 + 2*36 + j*6+i)), Text('  ')] for i in range(6)]
              ):
            r += i
        right.append([Text('  ')] + r)

    right.append([])
    right.append([Text('   124 - 159      160 - 195      196 - 231')])

    for j in range(0, 6):
        r = []
        for i in ([[SGR('48;5;{}'.format(16 + 3*36 + j*6+i)), Text('  ')] for i in range(6)]
              + [[SGR(), Text("   ")]] + [[SGR('48;5;{}'.format(16 + 4*36 + j*6+i)), Text('  ')] for i in range(6)]
              + [[SGR(), Text("   ")]] + [[SGR('48;5;{}'.format(16 + 5*36 + j*6+i)), Text('  ')] for i in range(6)]
              ):
            r += i
        right.append([Text('  ')] + r)

    right.append([])
    right.append([Text('  232 - 255')])

    r = []
    for i in ([[SGR('48;5;{}'.format(16 + 6*36 + i)), Text('  ')] for i in range(24)]
            ):
        r += i
    right.append([Text('  ')] + r)

    print('\033c')

    for r in right:
        s = to_string(r) + SGR().data

        print(s)

    print(SGR().data, end='')

if __name__ == '__main__':
    main()
