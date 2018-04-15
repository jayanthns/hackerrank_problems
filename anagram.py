w1 = raw_input()
w2 = raw_input()
result = [w1, w2]
# result.sort(lambda x, y: cmp(len(y), len(x)))

w1 = list(result[0])
w2 = list(result[1])

i = 0
while i < w1.__len__():
    if w1[i] in w2:
        w2.remove(w1[i])
        w1.remove(w1[i])
    else:
        i = i +1

print str(w1.__len__() + w2.__len__())
