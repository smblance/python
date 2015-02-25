from collections import defaultdict
import time

f = open('2sum.txt')
a = f.readlines()
d = {}
##d = OrderedDict()
for n in range(len(a)):
    a[n] = int(a[n])
    d.update({a[n]:None})
a.sort()
print len(a)
##for n in range(len(a)):
##    d.update({int(a[n]):None})

res = 0
time.clock()
good = {}

for n in d:
    p = 0
    c = time.clock()
    for v in range(1000000):
        if a[p] >= -10000 - n:
            p = v
            break
##    while a[p] < -10000 - n:
##        p+=1
    print '**',time.clock() - c
    c = time.clock()
    while a[p] <= 10000 - n:
        good.update({a[p] + n:None})
        #print a[p]+n
        p+=1
    #print time.clock() - c
    #print len(good)
    

print len(good)


##for t in xrange(-10000,10001):
##    p = time.clock()
##    for n in a:
##        if t-n in a:
##            if t != 2*n:
##                res += 1
##                print 'res', res
##                break
##    print time.clock() - p
##    
##print res
