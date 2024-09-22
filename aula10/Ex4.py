def endX(s):
    if not s:
        return s

    if s[0] == 'x':
        return endX(s[1:]) + 'x'
    else:
        return s[0] + endX(s[1:])