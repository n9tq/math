import sys

def gcf(a,b):
    while b:
        a, b = b, a%b
    return a

def reduce(a,b):
    gf = gcf(a,b)
    if ( gf == 1 ):
        return ((a,b))
    else:
        return ((a/gf,b/gf))


def main(argv):
    i = 0
    slope = ""
    p1 = ""
    p2 = ""

    while i < len(argv):
        if argv[i] == '-m':
            slope = argv[i + 1]
            i += 2
        elif argv[i] == '-p1':
            p1 = argv[i + 1]
            i += 2
        elif argv[i] == '-p2':
            p2 = argv[i + 1]
            i += 2
        else:
            i += 1

    if slope:
        if '/' in slope:
            print('slope ' + slope)
            rise = int(slope.split('/')[0])
            run = int(slope.split('/')[1])
            print('rise ', rise)
            print('run ', run)
            if slope.split('/')[1] == '0':
                m=('x','x')
        else:
            print('rise ' + slope)
            print('run ' + '1')

    if p1:
        x1 = float(p1.split(',')[0])
        y1 = float(p1.split(',')[1])
        print('p1 ', x1,y1)
    if p2:
        x2 = float(p2.split(',')[0])
        y2 = float(p2.split(',')[1])
        print('p2 ', x2,y2)
    if p1 and p2:
        if x1 - x2 != 0:
            m = reduce(y1 - y2, x1-x2)
        else:
            m = ('x','x')

    if m[0] == 'x': # Vertical line, slope is undefined
        print('Equation of the line: x = ' + str(y1))
        print('Slope (m) is UNDEFINED')
        if x1 == 0:
            print('Y-Intercept (b) = ' + str(x1))
        else:
            print('Y-Intercept (b): NONE')
            print('X-Intercept = ' + str(x1))
    elif m[0] == 0:
        print('Equation of the line: y = ' + str(y1))
        print('Slope (m) = 0')
        if y1 == 0:
            print('X-intercept (b) = 0')
        else:
            print('Y-Intercept (b) = ' + str(y1))
            print('X-Intercept None')

    else:      
        by = y1 - float(m[0])/float(m[1]) * x1
        print('b ', by)

        bx = -1 * by * float(m[1])/float(m[0])
        print('bx ', bx)

        type(m)
        stringm = str(int(m[0])) + '/' + str(int(m[1]))
        #stringb = m[0] + '/' + m[1]
        print (stringm)

        print('Equation of the line: y = ' + stringm + 'x + ' + str(by))
        print('Slope (m) = ' + stringm)
        print('Y-Intercept (b) = ' + str(by))
        print('X-Intercept = ' + str(bx))

if __name__ == "__main__":
    main (sys.argv[1:]


)
