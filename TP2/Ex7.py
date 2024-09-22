def toStr(num):
    assert num >= 0 
    digits = "0123456789"
    if num < 10 :
        print( digits[num] )
    print( toStr(num // 10 ) + digits[num % 10 ] )

toStr(2983)

