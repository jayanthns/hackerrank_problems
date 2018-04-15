def timeConversion(s):
    #
    # Write your code here.
    #
    am_or_pm = s[8:]
    s = s.rstrip(am_or_pm)
    if str(am_or_pm) == 'PM':
        hour = s[0:2]
        if hour != '12':
            hour = str(int(hour)+12)
            res = hour + s[2:8]
            s = res
    if str(am_or_pm) == 'AM':
        hour = s[0:2]
        if hour == '12':
            hour = '00'
            res = hour + s[2:8]
            s = res
    return s


s = raw_input()

result = timeConversion(s)
print result
