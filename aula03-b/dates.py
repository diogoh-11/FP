
# isLeapYear(year) deve devolver True se year é um ano bissexto
# e False se é um ano comum.  Corrija-a.
# (See: https://en.wikipedia.org/wiki/Leap_year)
def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
  else:
        return False  # False?


# monthDays deve devolver o número de dias de um dado mês num dado ano.
# Por exemplo, monthDays(2004, 2) deve devolver 29.
# Corrija-a.
def monthDays(year, month):
   MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
   if isLeapYear(year) == True:
      MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
      days = MONTHDAYS[month]
      return days

# nextMonth deve devolver o mês seguinte ao mês (e ano) dado.
# Por exemplo, nextMonth(2016, 12) deve devolver (2017, 1).



def nextMonth(year, month):
        if  month == 12:
            month = 1
            year += 1
        else:
            month += 1
        return year, month
# nextDay deve devolver o dia a seguir a uma dada data.
# Por exemplo, nextDay(2017, 1, 31) deve devolver (2017, 2, 1)

def nextDay(year, month, day):
    days_in_month = monthDays(year, month)
    if day == days_in_month and month == 12:
        day = 1
        month = 1
        year += 1
    if day == days_in_month:
             day = 1
             month += 1
    else:
        day += 1
    return year, month, day
    


# Defina uma função dateIsValid que deve
# devolver True se os seus argumentos formarem uma data válida
# e devolver False no caso contrário.
# Por exemplo, dateIsValid(1980, 2, 29) deve devolver True,
# dateIsValid(1980, 2, 30) deve devolver False.

def dateIsValid(year, month, day):
    # Verifica se o ano é válido (entre 1 e 9999)
    if year < 1 or year > 9999:
        return False
    
    # Verifica se o mês está no intervalo válido (de 1 a 12)
    if month < 1 or month > 12:
        return False
    
    # Verifica o número de dias no mês
    if day < 1 or day > monthDays(year, month):
        return False
    else:
        return True

def monthDays(year, month):
    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if isLeapYear(year) and month == 2:
        return 29
    else:
        return MONTHDAYS[month]

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        
        

