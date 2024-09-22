def median(lst):
    assert len(lst) > 0
    lista_ordenada = sorted(lst)
    n = len(lista_ordenada)
   
    if n % 2 == 1:
      return lista_ordenada[n // 2]
      
    else:
      meio1 = lista_ordenada[n // 2 - 1]
      meio2 = lista_ordenada[n // 2]
      return (meio1 + meio2) / 2


def ckeck(lst):
   backup = lst.copy()
   m = median(lst)
   return m, lst