def reverse(s):
    return  s  if len(s) <=1 else s[-1:]  + reverse( s[:-1] )