import time

f = open('2sum.txt')
a = f.readlines()
d = {}
for n in range(len(a)):
    d.update({int(a[n]):None})
print 77575749614 in d
res = 0
time.clock()
for t in xrange(-10000,10001):
    p = time.clock()
    for n in d:
        if t-n in d:
            if t != 2*n:
                res += 1
                print 'res', res
                break
    print time.clock() - p
    
print res
