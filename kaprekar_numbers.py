def kaprekarNumbers(p, q):
    # Complete this function
    result = []
    for i in range(p, q+1):
        d = str(i).__len__()
        n = str(i*i)
        try:
            if n.__len__() > 1:
                res = int(n.split(n[-d:])[0]) + int(n[-d:])
            else:
                res = int(n)
            if res == i:
                result.append(i)
        except:
            pass
    if result.__len__() == 0:
        result = ['INVALID RANGE']
    return result


p = int(raw_input().strip())
q = int(raw_input().strip())
result = kaprekarNumbers(p, q)
print " ".join(map(str, result))