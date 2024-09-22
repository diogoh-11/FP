def reverseDigits(value):
   return reverseAux(value, 0)

def reverseAux(partValue, partReversed):
    if partValue == 0:
      return partReversed
    else:
        lastDigit = partValue % 10
        remainingDigits = partValue // 10
        newReversed = partReversed * 10 + lastDigit
        return reverseAux(remainingDigits, newReversed)
    